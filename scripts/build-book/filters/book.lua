--- book.lua — Pandoc Lua filter for Community Network Handbook
---
--- Handles:
---   - Admonition fenced divs -> LaTeX tcolorbox / HTML styled divs
---   - Raw \frontmatter, \mainmatter, \appendix passthrough

-- Admonition type -> colour mapping (LaTeX colour names)
local adm_colors = {
    tip     = "teal",
    info    = "cyan",
    warning = "orange",
    note    = "gray",
    danger  = "red",
    example = "violet",
}

-- Admonition type -> label prefix for non-LaTeX output
local adm_labels = {
    tip     = "Tip",
    info    = "Info",
    warning = "Warning",
    note    = "Note",
    danger  = "Danger",
    example = "Example",
}

--- Detect admonition type from div classes.
--- Returns (adm_type, title) or nil.
local function parse_admonition(el)
    if not el.classes:includes("admonition") then
        return nil, nil
    end
    local adm_type = nil
    for _, cls in ipairs(el.classes) do
        if cls ~= "admonition" then
            adm_type = cls
            break
        end
    end
    adm_type = adm_type or "note"
    local title = el.attributes.title or adm_labels[adm_type] or adm_type:gsub("^%l", string.upper)
    return adm_type, title
end


function Div(el)
    local adm_type, title = parse_admonition(el)
    if not adm_type then
        return nil  -- not an admonition, leave unchanged
    end

    local color = adm_colors[adm_type] or "gray"

    if FORMAT:match("latex") then
        -- Wrap content in a tcolorbox environment
        local open = string.format(
            "\\begin{admonitionbox}{%s}{%s}",
            color, title
        )
        local close = "\\end{admonitionbox}"

        local blocks = pandoc.List({pandoc.RawBlock("latex", open)})
        blocks:extend(el.content)
        blocks:insert(pandoc.RawBlock("latex", close))
        return blocks

    elseif FORMAT:match("html") or FORMAT:match("epub") then
        -- For HTML/EPUB, add a visible title and style class
        local title_block = pandoc.Div(
            pandoc.Para(pandoc.Strong(pandoc.Str(title))),
            pandoc.Attr("", {"admonition-title"})
        )
        local blocks = pandoc.List({title_block})
        blocks:extend(el.content)
        el.content = blocks
        -- Keep the classes for CSS styling
        return el

    else
        return nil
    end
end


--- Pass through raw LaTeX commands (\frontmatter, \mainmatter, \appendix)
--- that the pre-processor inserted. These are already handled by Pandoc's
--- markdown+raw_tex reader, so no filter action needed.
