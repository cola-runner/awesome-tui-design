#!/usr/bin/env python3
"""
Generate an HTML gallery page showing all themes in a terminal-style grid.
Open the output HTML in a browser and screenshot for the hero image.

Usage:
    python3 preview/gallery.py
    # Opens preview/gallery.html in browser
"""

import os
import re
import sys
import webbrowser

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def parse_design_md(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    theme = {"name": "", "tagline": "", "mood": "", "colors": {}, "borders": {}, "icons": {}}

    m = re.search(r"^#\s+(.+?)(?:\s*—|-)", content, re.MULTILINE)
    if m:
        theme["name"] = m.group(1).strip()

    m = re.search(r"^>\s*(.+)", content, re.MULTILINE)
    if m:
        theme["tagline"] = m.group(1).strip()
        # Remove markdown links from tagline
        theme["tagline"] = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', theme["tagline"])

    color_roles = [
        "Background", "Foreground", "Primary", "Secondary", "Accent",
        "Success", "Warning", "Error", "Muted", "Surface"
    ]
    for role in color_roles:
        pattern = rf"\|\s*{role}[^|]*\|\s*`(#[0-9a-fA-F]{{6}})`"
        m = re.search(pattern, content)
        if m:
            theme["colors"][role.lower()] = m.group(1)

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

    border_parts = ["top_left", "top_right", "bottom_left", "bottom_right",
                    "horizontal", "vertical"]
    for part in border_parts:
        pattern = rf"\|\s*{part}\s*\|\s*`(.+?)`"
        m = re.search(pattern, content)
        if m:
            theme["borders"][part] = m.group(1)

    icon_section = re.search(r"##\s*\d*\.?\s*Icons.*?\n(.*?)(?=\n##\s|\Z)", content, re.DOTALL)
    if icon_section:
        icon_text = icon_section.group(1)
        for purpose in ["Success", "Error", "Warning", "Running", "Active", "Selected", "Spinner"]:
            pattern = rf"\|\s*{purpose}\s*\|\s*`?([^`|]+?)`?\s*\|"
            m = re.search(pattern, icon_text)
            if m:
                val = m.group(1).strip()
                if not val.startswith("#"):
                    theme["icons"][purpose.lower()] = val

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

    return theme

def _helpers(theme):
    c = theme["colors"]
    def span(color, text, bold=False, dim=False):
        style = f"color:{color};"
        if bold: style += "font-weight:bold;"
        if dim: style += "opacity:0.6;"
        return f'<span style="{style}">{esc(text)}</span>'
    def esc(text):
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    def bg_span(bg_color, fg_color, text):
        return f'<span style="background:{bg_color};color:{fg_color};padding:0 2px;">{esc(text)}</span>'
    return c, span, esc, bg_span

def _card_wrap(theme, lines):
    c = theme["colors"]
    content = "\n".join(lines)
    return f'<div class="theme-card" style="background:{c["background"]};"><pre>{content}</pre></div>'

# ── Per-theme renderers ──────────────────────────────────────────────

def render_claude_code(theme):
    c, span, esc, bg_span = _helpers(theme)
    lines = [
        f'  {span("#d77757", "Claude Code", bold=True)}  {span(c["muted"], "Anthropic")}',
        "",
        f'  {span("#888888", "- - - - - - - - - - - - - - -")}',
        f'  {span("#888888", "|")} {span(c["foreground"], "> fix the auth bug_")}       {span("#888888", "|")}',
        f'  {span("#888888", "- - - - - - - - - - - - - - -")}',
        "",
        f'  {span("#d77757", "✳")} {span("#d77757", "Percolating...")}',
        "",
        f'  {span("#fd5db1", "┌─ Bash ──────────────────────┐")}',
        f'  {span("#fd5db1", "│")} {span(c["muted"], "$")} {span(c["foreground"], "npm test")}                   {span("#fd5db1", "│")}',
        f'  {span("#fd5db1", "│")} {span("#4eba65", "✓")} {span(c["foreground"], "4 passed")}                   {span("#fd5db1", "│")}',
        f'  {span("#fd5db1", "└────────────────────────────┘")}',
        "",
        f'  {span("#505050", "── Opus · 12K tokens · $0.04 ──")}',
    ]
    return _card_wrap(theme, lines)

def render_codex(theme):
    c, span, esc, bg_span = _helpers(theme)
    lines = [
        f'  {span(c["foreground"], "Codex CLI", bold=True)}  {span(c["muted"], "OpenAI")}',
        "",
        f'  {span(c["foreground"], "▄▀█ █▀█ █▀▀ █▄ █")}',
        f'  {span(c["foreground"], "█▀█ █▀▀ ██▄ █ ▀█")}',
        "",
        f'  {span(c["muted"], "•")} {span(c["foreground"], "Working...")}',
        "",
        f'  {span(c["muted"], "▌")} {span(c["foreground"], "$ npm test")}',
        f'  {span(c["muted"], "│")} {span(c["foreground"], "PASS src/app.test.ts")}',
        f'  {span(c["muted"], "│")}   {span("#22c55e", "✓")} {span(c["foreground"], "handles input (12ms)")}',
        f'  {span(c["muted"], "│")}   {span("#22c55e", "✓")} {span(c["foreground"], "rejects invalid (3ms)")}',
        f'  {span(c["muted"], "└")} {span("#22c55e", "✓")} {span(c["foreground"], "Done.")}',
        "",
    ]
    return _card_wrap(theme, lines)

def render_gemini(theme):
    c, span, esc, bg_span = _helpers(theme)
    lines = [
        f'  {span(c["primary"], "Gemini CLI", bold=True)}  {span(c["muted"], "Google")}',
        "",
        f'  {span("#4796E4", "▝▜")}',
        f'  {span("#847ACE", "▗▟▄")}  {span("#4796E4", "G")}{span("#6589D9", "e")}{span("#847ACE", "m")}{span("#A37FA6", "i")}{span("#C3677F", "n")}{span("#C3677F", "i")} {span(c["foreground"], "CLI")}',
        "",
        f'  {span("#847ACE", "⠹")} {span(c["muted"], "Thinking... (3.2s)  (esc)")}',
        "",
        f'  {span(c["primary"], "╭─ Shell: npm test ──────────╮")}',
        f'  {span(c["primary"], "│")} {span(c["foreground"], "PASS src/app.test.ts")}       {span(c["primary"], "│")}',
        f'  {span(c["primary"], "│")}   {span("#d7ffd7", "✓")} {span(c["foreground"], "4 passed")}              {span(c["primary"], "│")}',
        f'  {span(c["muted"], "╰────────────────────────────╯")}',
        f'  {span(c["muted"], "  ● done")}',
        "",
    ]
    return _card_wrap(theme, lines)

def render_lazygit(theme):
    c, span, esc, bg_span = _helpers(theme)
    g = "#22c55e"  # green active
    m = c["muted"]
    lines = [
        f'  {span(g, "Lazygit", bold=True)}  {span(m, "54k stars")}',
        "",
        f'  {span(g, "╭─ Files (3) ──╮")}{span(m, "╭─ Diff ──────────────╮")}',
        f'  {span(g, "│")} {span(c["error"], "M")} {span(c["foreground"], "app.go")}     {span(g, "│")}{span(m, "│")} {span("#06b6d4", "@@ -1,3 +1,4 @@")}    {span(m, "│")}',
        f'  {span(g, "│")} {span("#22c55e", "A")} {span(c["foreground"], "util.go")}    {span(g, "│")}{span(m, "│")}  {span(c["foreground"], "func main() {")}{" "*5}{span(m, "│")}',
        f'  {span(g, "│")} {span(c["error"], "D")} {span(c["foreground"], "legacy.go")}  {span(g, "│")}{span(m, "│")} {span(c["error"], "-    old()")}          {span(m, "│")}',
        f'  {span(g, "╰──────────────╯")}{span(m, "│")} {span("#22c55e", "+    new()")}          {span(m, "│")}',
        f'  {span(m, "╭─ Branches ───╮")}{span(m, "│")} {span("#22c55e", "+    log(\"done\")")}    {span(m, "│")}',
        f'  {span(m, "│")} {span(g, "*")} {span(g, "main", bold=True)}       {span(m, "│")}{span(m, "│")}  {span(c["foreground"], "}")}                  {span(m, "│")}',
        f'  {span(m, "│")}   {span(c["foreground"], "dev")}        {span(m, "│")}{span(m, "╰──────────────────────╯")}',
        f'  {span(m, "╰──────────────╯")}',
        f'  {span("#3b82f6", "[q]")}uit {span("#3b82f6", "[space]")}stage {span("#3b82f6", "[enter]")}expand',
    ]
    return _card_wrap(theme, lines)

def render_btop(theme):
    c, span, esc, bg_span = _helpers(theme)
    m = c["muted"]
    lines = [
        f'  {span(c["primary"], "btop", bold=True)}  {span(m, "22k stars")}',
        "",
        f'  {span("#556d59", "╭─┐")}{span("#556d59", "cpu")}{span("#556d59", "┌──────────────────────╮")}',
        f'  {span("#556d59", "│")} {span("#77ca9b", "⣿")}{span("#77ca9b", "⣷")}{span("#cbc06c", "⣧")}{span("#cbc06c", "⡇")}{span("#dc4c4c", "⣿")}{span("#cbc06c", "⣷")}{span("#77ca9b", "⣧")}{span("#77ca9b", "⡇")}{span("#77ca9b", "⡇")}{span("#cbc06c", "⣧")} {span(c["foreground"], "45%  2.4GHz")}   {span("#556d59", "│")}',
        f'  {span("#556d59", "│")} {span(m, "cpu0")} {span("#77ca9b", "██████████")}{span(m, "░░░░░░░░")}  {span(c["foreground"], "52%")} {span("#556d59", "│")}',
        f'  {span("#556d59", "│")} {span(m, "cpu1")} {span("#cbc06c", "██████████████")}{span(m, "░░░░")}  {span(c["foreground"], "78%")} {span("#556d59", "│")}',
        f'  {span("#556d59", "│")} {span(m, "cpu2")} {span("#dc4c4c", "████████████████")}{span(m, "░░")}  {span(c["foreground"], "91%")} {span("#556d59", "│")}',
        f'  {span("#556d59", "│")} {span(m, "cpu3")} {span("#77ca9b", "██████")}{span(m, "░░░░░░░░░░░░")}  {span(c["foreground"], "32%")} {span("#556d59", "│")}',
        f'  {span("#556d59", "╰──────────────────────────────╯")}',
        f'  {span("#6c6c4b", "╭─┐")}{span("#6c6c4b", "mem")}{span("#6c6c4b", "┌─────────────╮")} {span("#5c588d", "╭─┐")}{span("#5c588d", "net")}{span("#5c588d", "┌─────╮")}',
        f'  {span("#6c6c4b", "│")} {span(m, "Used")}  {span("#dc4c4c", "█████")}{span(m, "░░░")} {span(c["foreground"], "4.2G")} {span("#6c6c4b", "│")} {span("#5c588d", "│")} {span(c["foreground"], "▲ 12MB/s")} {span("#5c588d", "│")}',
        f'  {span("#6c6c4b", "│")} {span(m, "Cache")} {span("#4897d4", "███")}{span(m, "░░░░░")} {span(c["foreground"], "2.1G")} {span("#6c6c4b", "│")} {span("#5c588d", "│")} {span(c["foreground"], "▼ 45MB/s")} {span("#5c588d", "│")}',
        f'  {span("#6c6c4b", "╰───────────────────╯")} {span("#5c588d", "╰────────────╯")}',
    ]
    return _card_wrap(theme, lines)

def render_k9s(theme):
    c, span, esc, bg_span = _helpers(theme)
    lines = [
        f'  {span("#ffa500", "k9s", bold=True)}  {span(c["muted"], "28k stars")}',
        "",
        f'  {span("#ffa500", "██╗ ██╗ █████╗ ███████╗", bold=True)}',
        f'  {span("#ffa500", "█████╔╝╚█████╔╝███████╗", bold=True)}',
        "",
        f'  {span("#1e90ff", "Context:")} {span("#00ffff", "prod")} {span(c["muted"], ">")} {span("#1e90ff", "NS:")} {span("#00ffff", "default")} {span(c["muted"], ">")} {span(c["foreground"], "Pods")}',
        "",
        f'  {span("#00ffff", "NAME              READY  STATUS", bold=True)}',
        f'  {bg_span("#00ffff", "#000000", "api-server-7d4f   1/1    Running ")}',
        f'  {span("#5f9ea0", "worker-pool-a3c2  1/1")}    {span("#adff2f", "Running")}',
        f'  {span("#5f9ea0", "redis-cache-1b8e  0/1")}    {span("#ff4500", "Error")}',
        f'  {span("#5f9ea0", "job-runner-9f1a   1/1")}    {span("#ff8c00", "Pending")}',
        f'  {span("#ff00ff", "<0>")} {span("#5f9ea0", "all")} {span("#ff00ff", "<d>")} {span("#5f9ea0", "describe")} {span("#ff00ff", "<l>")} {span("#5f9ea0", "logs")}',
    ]
    return _card_wrap(theme, lines)

def render_retro(theme):
    c, span, esc, bg_span = _helpers(theme)
    bc = c["muted"]
    lines = [
        f'  {span(c["primary"], "Retro", bold=True)}  {span(bc, "CRT terminal")}',
        "",
        f'  {span(c["primary"], "╔══╡ SYSTEM STATUS ╞═══════════╗")}',
        f'  {span(c["primary"], "║")}                               {span(c["primary"], "║")}',
        f'  {span(c["primary"], "║")}  {span(c["foreground"], "CPU .... 45%")}  {span("#77ca9b", "████")}{span(bc, "░░░░░░")}   {span(c["primary"], "║")}',
        f'  {span(c["primary"], "║")}  {span(c["foreground"], "MEM .... 72%")}  {span("#cbc06c", "███████")}{span(bc, "░░░")}   {span(c["primary"], "║")}',
        f'  {span(c["primary"], "║")}  {span(c["foreground"], "DSK .... 23%")}  {span("#77ca9b", "██")}{span(bc, "░░░░░░░░")}   {span(c["primary"], "║")}',
        f'  {span(c["primary"], "║")}                               {span(c["primary"], "║")}',
        f'  {span(c["primary"], "╚═══════════════════════════════╝")}',
        "",
        f'  {span(c["primary"], "> NEW GAME", bold=True)}',
        f'    {span(c["foreground"], "LOAD GAME")}',
        f'    {span(c["foreground"], "OPTIONS")}',
        f'    {span(bc, "QUIT")}',
    ]
    return _card_wrap(theme, lines)

def render_cyberpunk(theme):
    c, span, esc, bg_span = _helpers(theme)
    lines = [
        f'  {span(c["primary"], "Cyberpunk", bold=True)}  {span(c["muted"], "neon night")}',
        "",
        f'  {span(c["primary"], "╔══╣ NETWORK ╠═══════════════╗")}',
        f'  {span(c["primary"], "║")} {span("#00ff88", "●")} {span(c["foreground"], "node-alpha-01")}  {span("#00ff88", "ONLINE")}  {span(c["foreground"], "12ms")} {span(c["primary"], "║")}',
        f'  {span(c["primary"], "║")} {span("#00ff88", "●")} {span(c["foreground"], "node-beta-02")}   {span("#00ff88", "ONLINE")}  {span(c["foreground"], "34ms")} {span(c["primary"], "║")}',
        f'  {span(c["primary"], "║")} {span(c["error"], "○")} {span(c["foreground"], "node-gamma-03")}  {span(c["error"], "DOWN")}    {span(c["foreground"], "--")}   {span(c["primary"], "║")}',
        f'  {span(c["primary"], "╚═════════════════════════════╝")}',
        "",
        f'  {span(c["foreground"], "IN")}  {span(c["primary"], "████████████████")}{span(c["muted"], "░░░░")} {span(c["foreground"], "845 MB/s")}',
        f'  {span(c["foreground"], "OUT")} {span(c["secondary"], "██████████")}{span(c["muted"], "░░░░░░░░░░")} {span(c["foreground"], "412 MB/s")}',
        "",
        f'  {span(c["accent"], "[1]")} {span(c["foreground"], "SCAN")} {span(c["accent"], "[2]")} {span(c["foreground"], "SWEEP")} {span(c["accent"], "[3]")} {span(c["foreground"], "TRACE")}',
        "",
    ]
    return _card_wrap(theme, lines)

def render_default_card(theme):
    """Default card for color scheme themes — shows core components."""
    c, span, esc, bg_span = _helpers(theme)
    b = theme["borders"]
    bc = c["muted"]
    tl, tr, bl, br, h, v = b["top_left"], b["top_right"], b["bottom_left"], b["bottom_right"], b["horizontal"], b["vertical"]
    success_icon = theme["icons"].get("success", "✓")
    error_icon = theme["icons"].get("error", "✗")
    warning_icon = theme["icons"].get("warning", "!")
    selector_raw = theme["icons"].get("selected", theme["icons"].get("active", "▸"))
    selector = selector_raw if len(selector_raw) <= 2 else "▸"

    lines = [
        f'  {span(c["primary"], theme["name"], bold=True)}',
        "",
        # Color swatches
        "  " + " ".join(bg_span(c.get(r, "#888"), c.get(r, "#888"), "  ") for r in ["primary", "secondary", "accent", "success", "warning", "error"]),
        "",
        # Panel with theme-appropriate border
        f'  {span(bc, tl + h)}{span(c["primary"], " Status ", bold=True)}{span(bc, h * 22 + tr)}',
        f'  {span(bc, v)} {span(c["success"], success_icon)} {span(c["foreground"], "api-server")}    {span(c["success"], "Ready")}   {span(c["muted"], " 2m")} {span(bc, v)}',
        f'  {span(bc, v)} {span(c["primary"], selector)} {span(c["foreground"], "web-app")}       {span(c["primary"], "Build")}   {span(c["muted"], "now")} {span(bc, v)}',
        f'  {span(bc, v)} {span(c["error"], error_icon)} {span(c["foreground"], "database")}      {span(c["error"], "Failed")}  {span(c["muted"], " 5m")} {span(bc, v)}',
        f'  {span(bc, v)} {span(c["warning"], warning_icon)} {span(c["foreground"], "cache")}         {span(c["warning"], "Warn")}    {span(c["muted"], " 1h")} {span(bc, v)}',
        f'  {span(bc, bl + h * 30 + br)}',
        "",
        # Progress bar (theme-colored)
        f'  {span(c["foreground"], "Progress")} {span(c["primary"], "█" * 16)}{span(c["muted"], "░" * 8)} {span(c["foreground"], "67%")}',
        "",
        # Menu
        f'    {span(c["foreground"], "Overview")}',
        f'  {span(c["primary"], selector + " Dashboard", bold=True)}',
        f'    {span(c["muted"], "Settings", dim=True)}',
    ]
    return _card_wrap(theme, lines)


# ── Dispatch ─────────────────────────────────────────────────────────

CUSTOM_RENDERERS = {
    "Claude Code": render_claude_code,
    "Codex CLI": render_codex,
    "Gemini CLI": render_gemini,
    "Lazygit": render_lazygit,
    "btop": render_btop,
    "k9s": render_k9s,
    "Retro": render_retro,
    "Cyberpunk": render_cyberpunk,
}

def render_theme_card(theme):
    renderer = CUSTOM_RENDERERS.get(theme["name"], render_default_card)
    return renderer(theme)


def generate_gallery_html(themes):
    cards = []
    for theme in themes:
        cards.append(render_theme_card(theme))

    cards_html = "\n".join(cards)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>awesome-tui-design — Theme Gallery</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    background: #0d0d0d;
    color: #e0e0e0;
    font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;
    padding: 40px 20px;
  }}

  .header {{
    text-align: center;
    margin-bottom: 48px;
  }}

  .header h1 {{
    font-size: 36px;
    color: #ffffff;
    margin-bottom: 10px;
    letter-spacing: -0.5px;
  }}

  .header p {{
    font-size: 16px;
    color: #888;
  }}

  .section-title {{
    text-align: center;
    font-size: 14px;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin: 36px 0 20px;
  }}

  .grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
    gap: 16px;
    max-width: 1400px;
    margin: 0 auto;
  }}

  .theme-card {{
    border-radius: 8px;
    padding: 4px 0;
    border: 1px solid #333;
    overflow: hidden;
  }}

  .theme-card pre {{
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 12.5px;
    line-height: 1.45;
    padding: 12px 8px;
    margin: 0;
    white-space: pre;
    overflow: hidden;
  }}

  .footer {{
    text-align: center;
    margin-top: 48px;
    color: #555;
    font-size: 12px;
  }}

  .footer a {{
    color: #888;
    text-decoration: none;
  }}
</style>
</head>
<body>

<div class="header">
  <h1>awesome-tui-design</h1>
  <p>DESIGN.md for Terminal UI — drop it in, AI builds matching TUI</p>
</div>

<div class="section-title">AI / Agent CLIs</div>
<div class="grid" id="ai-grid"></div>

<div class="section-title">Popular TUI Applications</div>
<div class="grid" id="app-grid"></div>

<div class="section-title">Color Schemes</div>
<div class="grid" id="scheme-grid"></div>

<div class="footer">
  <p>github.com/user/awesome-tui-design — 16 themes, zero dependencies</p>
</div>

<script>
// Distribute cards into sections
const cards = document.querySelectorAll('.theme-card');
// We'll do this server-side instead
</script>

</body>
</html>'''

    # Actually, let's place cards directly in sections
    ai_themes = ["Claude Code", "Codex CLI", "Gemini CLI"]
    app_themes = ["Lazygit", "btop", "k9s"]

    ai_cards = []
    app_cards = []
    scheme_cards = []

    for theme, card in zip(themes, [render_theme_card(t) for t in themes]):
        if theme["name"] in ai_themes:
            ai_cards.append(card)
        elif theme["name"] in app_themes:
            app_cards.append(card)
        else:
            scheme_cards.append(card)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>awesome-tui-design — Theme Gallery</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    background: #0d0d0d;
    color: #e0e0e0;
    font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;
    padding: 40px 20px;
  }}

  .header {{
    text-align: center;
    margin-bottom: 48px;
  }}

  .header h1 {{
    font-size: 36px;
    color: #ffffff;
    margin-bottom: 10px;
    letter-spacing: -0.5px;
  }}

  .header p {{
    font-size: 16px;
    color: #888;
  }}

  .section-title {{
    text-align: center;
    font-size: 15px;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 3px;
    margin: 44px 0 24px;
    font-weight: bold;
  }}

  .grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    max-width: 1500px;
    margin: 0 auto;
  }}

  .grid-2 {{
    grid-template-columns: repeat(2, 1fr);
    max-width: 920px;
  }}

  .theme-card {{
    border-radius: 8px;
    padding: 4px 0;
    border: 1px solid #222;
    overflow: hidden;
    transition: border-color 0.2s;
  }}

  .theme-card:hover {{
    border-color: #555;
  }}

  .theme-card pre {{
    font-family: 'JetBrains Mono', 'Menlo', 'Monaco', 'Courier New', monospace;
    font-size: 13px;
    line-height: 1.5;
    padding: 14px 10px;
    margin: 0;
    white-space: pre;
    overflow: hidden;
  }}

  .footer {{
    text-align: center;
    margin-top: 32px;
    padding-bottom: 16px;
    color: #444;
    font-size: 12px;
  }}

  html, body {{
    height: auto;
    overflow: visible;
  }}
</style>
</head>
<body>

<div class="header">
  <h1>awesome-tui-design</h1>
  <p>DESIGN.md for Terminal UI — drop it in your project, AI builds matching TUI</p>
</div>

<div class="section-title">AI / Agent CLIs</div>
<div class="grid">
{"".join(ai_cards)}
</div>

<div class="section-title">Popular TUI Applications</div>
<div class="grid">
{"".join(app_cards)}
</div>

<div class="section-title">Color Schemes</div>
<div class="grid">
{"".join(scheme_cards)}
</div>

<div class="footer">
  <p>16 themes &middot; zero dependencies &middot; works with any TUI framework</p>
</div>

</body>
</html>'''

    return html


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    designs_dir = os.path.join(project_dir, "designs")
    output_path = os.path.join(script_dir, "gallery.html")

    # Define order
    ordered_dirs = [
        "claude-code", "codex", "gemini-cli",
        "lazygit", "k9s", "btop",
        "dracula", "catppuccin", "nord", "gruvbox", "tokyo-night",
        "rose-pine", "minimal", "cyberpunk", "ocean", "retro"
    ]

    themes = []
    for name in ordered_dirs:
        path = os.path.join(designs_dir, name, "DESIGN.md")
        if os.path.isfile(path):
            theme = parse_design_md(path)
            themes.append(theme)

    html = generate_gallery_html(themes)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Gallery generated: {output_path}")
    print(f"Themes: {len(themes)}")

    # Try to open in browser
    if "--no-open" not in sys.argv:
        webbrowser.open(f"file://{output_path}")
        print("Opened in browser. Screenshot this for the hero image!")

if __name__ == "__main__":
    main()
