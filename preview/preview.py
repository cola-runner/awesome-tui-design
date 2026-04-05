#!/usr/bin/env python3
"""
awesome-tui-design preview tool

Renders a live preview of a TUI DESIGN.md theme in the terminal.
Parses the Markdown to extract colors, borders, icons, and components,
then renders a sample dashboard showcasing the theme.

Usage:
    python3 preview/preview.py designs/minimal/DESIGN.md
    python3 preview/preview.py designs/retro/DESIGN.md
    python3 preview/preview.py --list
    python3 preview/preview.py --all
"""

import sys
import os
import re
import time

# ── ANSI helpers ─────────────────────────────────────────────────────────

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def fg(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    return f"\033[38;2;{r};{g};{b}m"

def bg(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    return f"\033[48;2;{r};{g};{b}m"

def bold():
    return "\033[1m"

def dim():
    return "\033[2m"

def reset():
    return "\033[0m"

def reverse():
    return "\033[7m"

# ── Markdown parser ──────────────────────────────────────────────────────

def parse_design_md(path):
    """Parse a DESIGN.md and extract theme data."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    theme = {
        "name": "",
        "tagline": "",
        "mood": "",
        "colors": {},
        "borders": {},
        "icons": {},
    }

    # Extract theme name from first heading
    m = re.search(r"^#\s+(.+?)(?:\s*—|-)", content, re.MULTILINE)
    if m:
        theme["name"] = m.group(1).strip()

    # Extract tagline (first blockquote)
    m = re.search(r"^>\s*(.+)", content, re.MULTILINE)
    if m:
        theme["tagline"] = m.group(1).strip()

    # Extract mood
    m = re.search(r"\*\*Mood\*\*:\s*(.+)", content)
    if m:
        theme["mood"] = m.group(1).strip()

    # Extract semantic colors from table
    color_roles = [
        "Background", "Foreground", "Primary", "Secondary", "Accent",
        "Success", "Warning", "Error", "Muted", "Surface"
    ]
    for role in color_roles:
        pattern = rf"\|\s*{role}[^|]*\|\s*`(#[0-9a-fA-F]{{6}})`"
        m = re.search(pattern, content)
        if m:
            theme["colors"][role.lower()] = m.group(1)

    # Also try "Base" and "Text" patterns for Rosé Pine style
    for alias, target in [("Base", "background"), ("Text", "foreground"),
                          ("Rose", "primary"), ("Iris", "secondary"),
                          ("Gold", "accent"), ("Pine", "success"),
                          ("Love", "error"), ("Subtle", "muted"),
                          ("Foam", "foam")]:
        if target not in theme["colors"]:
            pattern = rf"\|\s*{alias}\)?\s*\|\s*`(#[0-9a-fA-F]{{6}})`"
            m = re.search(pattern, content)
            if m:
                theme["colors"][target] = m.group(1)

    # Extract border characters from parts table
    border_parts = [
        "top_left", "top_right", "bottom_left", "bottom_right",
        "horizontal", "vertical", "cross", "tee_down", "tee_up",
        "tee_right", "tee_left"
    ]
    for part in border_parts:
        pattern = rf"\|\s*{part}\s*\|\s*`(.+?)`"
        m = re.search(pattern, content)
        if m:
            theme["borders"][part] = m.group(1)

    # Extract icons from the Icons & Indicators section
    icon_section = re.search(
        r"##\s*\d*\.?\s*Icons.*?\n(.*?)(?=\n##\s|\Z)", content, re.DOTALL
    )
    if icon_section:
        icon_text = icon_section.group(1)
        icon_purposes = [
            "Success", "Error", "Warning", "Info", "Pending", "Running",
            "Active", "Inactive", "Online", "Offline",
            "Spinner", "Arrow", "Bullet", "Selected"
        ]
        for purpose in icon_purposes:
            pattern = rf"\|\s*{purpose}\s*\|\s*`?([^`|]+?)`?\s*\|"
            m = re.search(pattern, icon_text)
            if m:
                val = m.group(1).strip()
                if not val.startswith("#"):  # skip hex colors
                    theme["icons"][purpose.lower()] = val

    # Defaults
    theme["colors"].setdefault("background", "#0a0a0a")
    theme["colors"].setdefault("foreground", "#ededed")
    theme["colors"].setdefault("primary", "#ffffff")
    theme["colors"].setdefault("secondary", "#888888")
    theme["colors"].setdefault("accent", "#0070f3")
    theme["colors"].setdefault("success", "#00c853")
    theme["colors"].setdefault("warning", "#f5a623")
    theme["colors"].setdefault("error", "#ee0000")
    theme["colors"].setdefault("muted", "#555555")
    theme["colors"].setdefault("surface", "#1a1a1a")

    theme["borders"].setdefault("top_left", "┌")
    theme["borders"].setdefault("top_right", "┐")
    theme["borders"].setdefault("bottom_left", "└")
    theme["borders"].setdefault("bottom_right", "┘")
    theme["borders"].setdefault("horizontal", "─")
    theme["borders"].setdefault("vertical", "│")
    theme["borders"].setdefault("tee_down", "┬")
    theme["borders"].setdefault("tee_up", "┴")
    theme["borders"].setdefault("tee_right", "├")
    theme["borders"].setdefault("tee_left", "┤")

    return theme

# ── Rendering ────────────────────────────────────────────────────────────

def box(theme, title, lines, width=50):
    """Render a bordered box with title."""
    c = theme["colors"]
    b = theme["borders"]
    border_color = c.get("muted", c["secondary"])

    out = []
    inner = width - 2

    # Top border with title
    title_str = f" {title} "
    remaining = inner - len(title_str)
    top = (f"{fg(border_color)}{b['top_left']}{b['horizontal']}"
           f"{fg(c['primary'])}{bold()}{title_str}{reset()}"
           f"{fg(border_color)}{b['horizontal'] * remaining}"
           f"{b['top_right']}{reset()}")
    out.append(top)

    # Empty line
    out.append(f"{fg(border_color)}{b['vertical']}{reset()}{' ' * inner}{fg(border_color)}{b['vertical']}{reset()}")

    # Content lines
    for line in lines:
        # Strip ANSI for length calculation
        visible = re.sub(r"\033\[[0-9;]*m", "", line)
        pad = inner - len(visible)
        if pad < 0:
            pad = 0
        out.append(f"{fg(border_color)}{b['vertical']}{reset()} {line}{' ' * (pad - 1)}{fg(border_color)}{b['vertical']}{reset()}")

    # Empty line
    out.append(f"{fg(border_color)}{b['vertical']}{reset()}{' ' * inner}{fg(border_color)}{b['vertical']}{reset()}")

    # Bottom border
    bottom = f"{fg(border_color)}{b['bottom_left']}{b['horizontal'] * inner}{b['bottom_right']}{reset()}"
    out.append(bottom)

    return "\n".join(out)

def render_preview(theme):
    """Render a full preview dashboard for the theme."""
    c = theme["colors"]
    R = reset()

    # Clear screen + set background
    print(f"{bg(c['background'])}\033[2J\033[H", end="")

    try:
        term_cols = os.get_terminal_size().columns
        term_rows = os.get_terminal_size().lines
    except OSError:
        term_cols = 80
        term_rows = 24

    # ── Header ───────────────────────────────────────────────────────
    print()
    print(f"  {fg(c['primary'])}{bold()}awesome-tui-design{R}{bg(c['background'])}"
          f"  {fg(c['muted'])}theme preview{R}{bg(c['background'])}")
    print()

    # ── Theme info ───────────────────────────────────────────────────
    print(f"  {fg(c['primary'])}{bold()}{theme['name']}{R}{bg(c['background'])}"
          f"  {fg(c['muted'])}{theme['tagline']}{R}{bg(c['background'])}")
    if theme["mood"]:
        print(f"  {fg(c['secondary'])}{theme['mood']}{R}{bg(c['background'])}")
    print()

    # ── Color Palette ────────────────────────────────────────────────
    palette_lines = []
    for role in ["primary", "secondary", "accent", "success", "warning", "error", "muted"]:
        hex_val = c.get(role, "#888888")
        swatch = f"{bg(hex_val)}    {R}{bg(c['background'])}"
        label = f"{fg(c['foreground'])}{role:<12}{R}{bg(c['background'])}"
        hex_str = f"{fg(c['muted'])}{hex_val}{R}{bg(c['background'])}"
        palette_lines.append(f"{swatch} {label} {hex_str}")

    panel_width = min(48, term_cols - 4)
    print(box(theme, "Color Palette", palette_lines, panel_width))
    print()

    # ── Components ───────────────────────────────────────────────────
    b = theme["borders"]
    success_icon = theme["icons"].get("success", "✓")
    error_icon = theme["icons"].get("error", "✗")
    warning_icon = theme["icons"].get("warning", "!")
    running_icon = theme["icons"].get("running",
                   theme["icons"].get("active", "▶"))

    comp_lines = [
        f"{fg(c['success'])}{success_icon}{R}{bg(c['background'])} {fg(c['foreground'])}deploy-api       {fg(c['success'])}Ready{R}{bg(c['background'])}      {fg(c['muted'])}2m ago{R}{bg(c['background'])}",
        f"{fg(c['primary'])}{running_icon}{R}{bg(c['background'])} {fg(c['foreground'])}deploy-web       {fg(c['primary'])}Building{R}{bg(c['background'])}   {fg(c['muted'])}just now{R}{bg(c['background'])}",
        f"{fg(c['error'])}{error_icon}{R}{bg(c['background'])} {fg(c['foreground'])}deploy-docs      {fg(c['error'])}Failed{R}{bg(c['background'])}     {fg(c['muted'])}5m ago{R}{bg(c['background'])}",
        f"{fg(c['warning'])}{warning_icon}{R}{bg(c['background'])} {fg(c['foreground'])}deploy-staging   {fg(c['warning'])}Warning{R}{bg(c['background'])}    {fg(c['muted'])}1h ago{R}{bg(c['background'])}",
    ]

    print(box(theme, "Deploy Status", comp_lines, panel_width))
    print()

    # ── Progress Bar ─────────────────────────────────────────────────
    bar_width = panel_width - 16
    filled = int(bar_width * 0.72)
    empty = bar_width - filled
    progress_lines = [
        f"{fg(c['foreground'])}Upload   {fg(c['primary'])}{'█' * filled}{fg(c['muted'])}{'░' * empty}{R}{bg(c['background'])} {fg(c['foreground'])}72%{R}{bg(c['background'])}",
        f"{fg(c['foreground'])}Build    {fg(c['success'])}{'█' * bar_width}{R}{bg(c['background'])} {fg(c['success'])}OK{R}{bg(c['background'])} ",
        f"{fg(c['foreground'])}Deploy   {fg(c['accent'])}{'█' * int(bar_width * 0.35)}{fg(c['muted'])}{'░' * (bar_width - int(bar_width * 0.35))}{R}{bg(c['background'])} {fg(c['foreground'])}35%{R}{bg(c['background'])}",
    ]

    print(box(theme, "Progress", progress_lines, panel_width))
    print()

    # ── Menu / List ──────────────────────────────────────────────────
    selector = theme["icons"].get("selected",
               theme["icons"].get("active",
               theme["icons"].get("arrow", "▸")))
    menu_lines = [
        f"  {fg(c['foreground'])}Overview{R}{bg(c['background'])}",
        f"{fg(c['primary'])}{bold()}{selector} Dashboard{R}{bg(c['background'])}",
        f"  {fg(c['foreground'])}Settings{R}{bg(c['background'])}",
        f"  {fg(c['muted'])}{dim()}Disabled item{R}{bg(c['background'])}",
    ]

    print(box(theme, "Navigation", menu_lines, panel_width))
    print()

    # ── Status bar ───────────────────────────────────────────────────
    bar = (f"  {fg(c['success'])}●{R}{bg(c['background'])} "
           f"{fg(c['foreground'])}Connected{R}{bg(c['background'])}"
           f"  {fg(c['muted'])}·{R}{bg(c['background'])}  "
           f"{fg(c['foreground'])}main{R}{bg(c['background'])}"
           f"  {fg(c['muted'])}·{R}{bg(c['background'])}  "
           f"{fg(c['muted'])}3 tasks{R}{bg(c['background'])}"
           f"  {fg(c['muted'])}·{R}{bg(c['background'])}  "
           f"{fg(c['muted'])}last saved 2m ago{R}{bg(c['background'])}")
    print(bar)
    print()

    # Reset terminal
    print(f"\033[0m", end="")

def list_themes(designs_dir):
    """List all available themes."""
    themes = []
    if os.path.isdir(designs_dir):
        for name in sorted(os.listdir(designs_dir)):
            design_path = os.path.join(designs_dir, name, "DESIGN.md")
            if os.path.isfile(design_path):
                theme = parse_design_md(design_path)
                themes.append((name, theme["name"], theme["tagline"]))

    print(f"\n  Available themes:\n")
    for dirname, name, tagline in themes:
        print(f"  \033[1m{dirname:<16}\033[0m {tagline[:60]}")
    print(f"\n  Usage: python3 preview/preview.py designs/<theme>/DESIGN.md\n")

def preview_all(designs_dir):
    """Preview all themes one by one."""
    if not os.path.isdir(designs_dir):
        print(f"Directory not found: {designs_dir}")
        return

    theme_dirs = sorted(os.listdir(designs_dir))
    for i, name in enumerate(theme_dirs):
        design_path = os.path.join(designs_dir, name, "DESIGN.md")
        if os.path.isfile(design_path):
            theme = parse_design_md(design_path)
            render_preview(theme)
            if i < len(theme_dirs) - 1:
                input(f"\033[2m  Press Enter for next theme... ({i+1}/{len(theme_dirs)})\033[0m")

# ── Main ─────────────────────────────────────────────────────────────────

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    designs_dir = os.path.join(project_dir, "designs")

    if len(sys.argv) < 2:
        print(__doc__)
        list_themes(designs_dir)
        sys.exit(0)

    arg = sys.argv[1]

    if arg == "--list":
        list_themes(designs_dir)
    elif arg == "--all":
        preview_all(designs_dir)
    else:
        path = arg
        if not os.path.isfile(path):
            # Try relative to project dir
            path = os.path.join(project_dir, arg)
        if not os.path.isfile(path):
            print(f"File not found: {arg}")
            sys.exit(1)
        theme = parse_design_md(path)
        render_preview(theme)

if __name__ == "__main__":
    main()
