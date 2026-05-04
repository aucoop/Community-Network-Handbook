#!/usr/bin/env bash
# =================================================================
# Community Network Handbook — Book Build Script
#
# Orchestrates the full pipeline:
#   1. Convert .webp images to .png (ImageMagick)
#   2. Pre-process markdown into a single combined.md (Python)
#   3. Render extracted Mermaid diagrams to SVG (mmdc)
#   4. Generate PDF via Pandoc + XeLaTeX
#   5. Generate EPUB via Pandoc
#
# Usage:
#   ./scripts/build-book/build-book.sh          # build both PDF and EPUB
#   ./scripts/build-book/build-book.sh pdf       # build PDF only
#   ./scripts/build-book/build-book.sh epub      # build EPUB only
# =================================================================
set -euo pipefail

# ---------------------------------------------------------------------------
# Paths (relative to repo root)
# ---------------------------------------------------------------------------
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
DOCS_DIR="$REPO_ROOT/docs"
BUILD_DIR="$REPO_ROOT/build/book"
SCRIPTS_DIR="$REPO_ROOT/scripts/build-book"

COMBINED_MD="$BUILD_DIR/combined.md"
MERMAID_DIR="$BUILD_DIR/mermaid"
IMAGES_DIR="$BUILD_DIR/images"

PREAMBLE="$SCRIPTS_DIR/templates/preamble.tex"
LUA_FILTER="$SCRIPTS_DIR/filters/book.lua"
EPUB_CSS="$SCRIPTS_DIR/epub.css"

OUTPUT_PDF="$BUILD_DIR/Community-Network-Handbook.pdf"
OUTPUT_EPUB="$BUILD_DIR/Community-Network-Handbook.epub"

# What to build
TARGET="${1:-all}"  # all | pdf | epub

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
info()  { echo "==> $*"; }
warn()  { echo "WARNING: $*" >&2; }
die()   { echo "ERROR: $*" >&2; exit 1; }

check_tool() {
    command -v "$1" &>/dev/null || die "'$1' is required but not found in PATH"
}

detect_imagemagick() {
    if command -v magick &>/dev/null; then
        echo "magick"
        return
    fi

    if command -v convert &>/dev/null; then
        echo "convert"
        return
    fi

    die "ImageMagick is required but neither 'magick' nor 'convert' was found in PATH"
}

# ---------------------------------------------------------------------------
# Pre-flight checks
# ---------------------------------------------------------------------------
info "Checking required tools..."
check_tool python3
check_tool pandoc
IMAGEMAGICK_CMD="$(detect_imagemagick)"

if [[ "$TARGET" == "all" || "$TARGET" == "pdf" ]]; then
    check_tool xelatex
fi

# mmdc is optional — if missing, we skip Mermaid rendering and warn
HAS_MMDC=true
if ! command -v mmdc &>/dev/null; then
    warn "mmdc (mermaid-cli) not found; Mermaid diagrams will be skipped"
    HAS_MMDC=false
fi

# Detect system Chromium for Puppeteer (used by mmdc)
if [[ "$HAS_MMDC" == true ]] && [[ -z "${PUPPETEER_EXECUTABLE_PATH:-}" ]]; then
    for browser in chromium chromium-browser google-chrome; do
        if command -v "$browser" &>/dev/null; then
            export PUPPETEER_EXECUTABLE_PATH="$(command -v "$browser")"
            info "Using browser: $PUPPETEER_EXECUTABLE_PATH"
            break
        fi
    done
fi

# ---------------------------------------------------------------------------
# Step 1: Convert .webp images to .png
# ---------------------------------------------------------------------------
info "Converting .webp images to .png..."
mkdir -p "$IMAGES_DIR"

webp_count=0
while IFS= read -r -d '' webp_file; do
    # Compute the relative path from docs/ and mirror it in build/book/images/
    rel_path="${webp_file#"$DOCS_DIR/"}"
    png_path="$IMAGES_DIR/${rel_path%.webp}.png"
    png_dir="$(dirname "$png_path")"
    mkdir -p "$png_dir"

    if [[ "$png_path" -nt "$webp_file" ]]; then
        # PNG already up-to-date, skip
        continue
    fi

    "$IMAGEMAGICK_CMD" "$webp_file" "$png_path"
    webp_count=$((webp_count + 1))
done < <(find "$DOCS_DIR" -name '*.webp' -print0)

info "  Converted $webp_count .webp image(s) to .png"

# ---------------------------------------------------------------------------
# Step 2: Pre-process markdown
# ---------------------------------------------------------------------------
info "Pre-processing markdown files..."
python3 "$SCRIPTS_DIR/preprocess.py" \
    --docs-dir "$DOCS_DIR" \
    --output "$COMBINED_MD" \
    --mermaid-dir "$MERMAID_DIR"

# ---------------------------------------------------------------------------
# Step 3: Fix image paths in combined.md to point to build/book/images/
# ---------------------------------------------------------------------------
# The pre-processor outputs paths relative to docs/ (e.g., 3-Guide/Wireless-Mesh/images/foo.png).
# We need to make them absolute or relative to the build dir so Pandoc can find them.
info "Fixing image paths to point to converted PNGs..."

# Use sed to prepend the images dir path to relative image references
# Images in combined.md look like: ![alt](3-Guide/Wireless-Mesh/images/foo.png)
# We need them to be: ![alt](build/book/images/3-Guide/Wireless-Mesh/images/foo.png)
# But since Pandoc runs from REPO_ROOT, we use the full path from repo root.
sed -i -E "s|!\[([^]]*)\]\(([^)]*\.png)\)|![\1]($IMAGES_DIR/\2)|g" "$COMBINED_MD"

# Mermaid SVG paths are already absolute (set by preprocess.py to mermaid_dir)

# ---------------------------------------------------------------------------
# Step 4: Render Mermaid diagrams to SVG
# ---------------------------------------------------------------------------
mermaid_count=0
if [[ "$HAS_MMDC" == true ]]; then
    shopt -s nullglob
    mmd_files=("$MERMAID_DIR"/*.mmd)
    shopt -u nullglob
    if [[ ${#mmd_files[@]} -gt 0 ]]; then
        info "Rendering Mermaid diagrams to SVG..."
        for mmd_file in "$MERMAID_DIR"/*.mmd; do
            svg_file="${mmd_file%.mmd}.svg"
            if [[ "$svg_file" -nt "$mmd_file" ]]; then
                continue  # already up-to-date
            fi
            mmdc -i "$mmd_file" -o "$svg_file" --quiet || {
                warn "Failed to render $(basename "$mmd_file"), skipping"
                continue
            }
            mermaid_count=$((mermaid_count + 1))
        done
        info "  Rendered $mermaid_count Mermaid diagram(s)"
    else
        info "  No Mermaid diagrams to render"
    fi
else
    info "  Skipping Mermaid rendering (mmdc not available)"
fi

# Remove Mermaid image references that were not rendered successfully so Pandoc
# does not fail on missing SVG files in CI environments.
if [[ -f "$COMBINED_MD" ]]; then
    tmp_combined="${COMBINED_MD}.tmp"
    while IFS= read -r line; do
        if [[ "$line" =~ ^!\[Diagram\]\((.*\.svg)\)$ ]]; then
            svg_path="${BASH_REMATCH[1]}"
            if [[ ! -f "$svg_path" ]]; then
                warn "Removing unresolved Mermaid reference: $svg_path"
                continue
            fi
        fi
        printf '%s\n' "$line" >> "$tmp_combined"
    done < "$COMBINED_MD"
    mv "$tmp_combined" "$COMBINED_MD"
fi

# ---------------------------------------------------------------------------
# Step 5: Build PDF
# ---------------------------------------------------------------------------
if [[ "$TARGET" == "all" || "$TARGET" == "pdf" ]]; then
    info "Building PDF with Pandoc + XeLaTeX..."
    pandoc "$COMBINED_MD" \
        --from markdown+raw_tex+fenced_divs+bracketed_spans+yaml_metadata_block \
        --to pdf \
        --pdf-engine=xelatex \
        --top-level-division=part \
        --lua-filter="$LUA_FILTER" \
        --include-in-header="$PREAMBLE" \
        --toc \
        --toc-depth=3 \
        --number-sections \
        --shift-heading-level-by=0 \
        --variable documentclass=book \
        --variable geometry="margin=2.5cm" \
        --variable fontsize=11pt \
        --variable mainfont="DejaVu Serif" \
        --variable sansfont="DejaVu Sans" \
        --variable monofont="DejaVu Sans Mono" \
        --variable linkcolor=teal \
        --variable urlcolor=teal \
        --variable toccolor=black \
        --output "$OUTPUT_PDF" \
        2>&1 | while IFS= read -r line; do echo "  [pandoc] $line"; done

    if [[ -f "$OUTPUT_PDF" ]]; then
        pdf_size=$(du -h "$OUTPUT_PDF" | cut -f1)
        info "PDF built: $OUTPUT_PDF ($pdf_size)"
    else
        die "PDF build failed — output file not created"
    fi
fi

# ---------------------------------------------------------------------------
# Step 6: Build EPUB
# ---------------------------------------------------------------------------
if [[ "$TARGET" == "all" || "$TARGET" == "epub" ]]; then
    info "Building EPUB with Pandoc..."
    pandoc "$COMBINED_MD" \
        --from markdown+raw_tex+fenced_divs+bracketed_spans+yaml_metadata_block \
        --to epub3 \
        --lua-filter="$LUA_FILTER" \
        --css="$EPUB_CSS" \
        --toc \
        --toc-depth=3 \
        --number-sections \
        --top-level-division=part \
        --shift-heading-level-by=0 \
        --split-level=2 \
        --output "$OUTPUT_EPUB" \
        2>&1 | while IFS= read -r line; do echo "  [pandoc] $line"; done

    if [[ -f "$OUTPUT_EPUB" ]]; then
        epub_size=$(du -h "$OUTPUT_EPUB" | cut -f1)
        info "EPUB built: $OUTPUT_EPUB ($epub_size)"
    else
        die "EPUB build failed — output file not created"
    fi
fi

# ---------------------------------------------------------------------------
# Done
# ---------------------------------------------------------------------------
info "Build complete!"
[[ "$TARGET" == "all" || "$TARGET" == "pdf" ]]  && echo "  PDF:  $OUTPUT_PDF"
[[ "$TARGET" == "all" || "$TARGET" == "epub" ]] && echo "  EPUB: $OUTPUT_EPUB"
