# Tokyo Night — TUI Design System

> A clean, dark theme that celebrates the lights of downtown Tokyo. Based on [Tokyo Night](https://github.com/enkia/tokyo-night-vscode-theme) — crisp, modern, with neon city vibes.

## 1. Theme Overview

- **Mood**: Modern, crisp, urban night
- **Density**: Balanced — clean with focused contrast
- **Target**: Modern dev tools, AI agents, API clients, sleek CLI apps
- **Terminal**: TrueColor recommended, 256-color acceptable

## 2. Color Palette

### Semantic Roles (Storm variant)

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#24283b` | `236` | `black` | Storm bg — main |
| Foreground | `#c0caf5` | `153` | `white` | Default text |
| Primary | `#7aa2f7` | `111` | `bright blue` | Blue — primary accent |
| Secondary | `#bb9af7` | `141` | `bright magenta` | Purple — secondary |
| Accent | `#7dcfff` | `117` | `bright cyan` | Cyan — highlights |
| Success | `#9ece6a` | `149` | `green` | Green |
| Warning | `#e0af68` | `179` | `yellow` | Orange-yellow |
| Error | `#f7768e` | `210` | `red` | Red-pink |
| Muted | `#565f89` | `60` | `bright black` | Comment — dim |
| Surface | `#1a1b26` | `234` | `black` | Night bg — deeper |

### Extended Tokyo Night Palette

| Name | Hex | ANSI 256 | Usage |
|------|-----|----------|-------|
| Magenta | `#ff007c` | `198` | Hot accent (rare) |
| Teal | `#73daca` | `115` | Strings, paths |
| Dark Blue | `#3d59a1` | `61` | Subtle accent |
| Dark 5 | `#737aa2` | `103` | Inactive text |
| Terminal Black | `#414868` | `238` | Selection bg |

## 3. Typography & ASCII Art

- **Header font**: `small` or `slant` (figlet) — modern, sharp
- **Body text**: plain terminal font
- **Emphasis**: `bold` + Blue or Purple
- **Code/values**: Teal or Cyan

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| H1 | figlet `slant` + Blue | App title |
| H2 | BOLD + Blue | Section headers |
| H3 | BOLD + Purple | Subsections |
| Body | Foreground | Content |
| Caption | Comment (Muted) | Timestamps, help |
| Data | Teal | Strings, paths |
| Accent | Cyan | URLs, highlights |

## 4. Borders & Box Drawing

### Primary Border

```
╭──────────────╮
│   content    │
╰──────────────╯
```

Rounded corners in Comment (Muted) color. Modern and sleek.

### Parts Table

| Part | Character | Usage |
|------|-----------|-------|
| top_left | `╭` | Panel corners |
| top_right | `╮` | |
| bottom_left | `╰` | |
| bottom_right | `╯` | |
| horizontal | `─` | |
| vertical | `│` | |
| cross | `┼` | Table intersections |
| tee_down | `┬` | |
| tee_up | `┴` | |
| tee_right | `├` | |
| tee_left | `┤` | |

### Dividers

- Horizontal: `──────────────────` (Muted)
- Section break: `── ◦ ──`

## 5. Components

### Buttons / Actions

```
 ▸ Execute    Cancel    Info
   ↑           ↑        ↑
 focused     normal   muted
```

- Focused: `▸` + BOLD + reverse (Blue bg)
- Normal: Foreground
- Disabled: Comment + dim

### Input Fields

```
  Query: ╭────────────────────────╮
         │ SELECT * FROM users_   │
         ╰────────────────────────╯
```

- Active: Blue border
- Inactive: Comment border
- Error: Error (red-pink) border

### Tables

```
  Endpoint            Method    Status    Time
  ──────────────────────────────────────────────
  /api/users          GET       200 ✓     12ms
  /api/auth/login     POST      200 ✓     45ms
  /api/data/export    GET       500 ✗    120ms
```

Borderless. Comment divider. Clean API-style display.

### Lists / Menus

```
    GET  /api/users
  ▸ POST /api/auth/login
    GET  /api/data/export
    DEL  /api/sessions
```

- Selected: `▸` + BOLD + Blue
- Method: colored by type (Green=GET, Warning=POST, Error=DEL)
- Disabled: Comment + dim

### Panels / Cards

```
╭── API Response ────────────────╮
│                                 │
│  Status: 200 OK                 │
│  Time:   45ms                   │
│  Size:   2.4 KB                 │
│                                 │
│  {                              │
│    "user": "alice",             │
│    "role": "admin"              │
│  }                              │
│                                 │
╰─────────────────────────────────╯
```

Title in Blue. Status in Success/Error color. JSON keys in Blue, values in Teal.

### Status Bar

```
 ▸ connected · api.example.com · 200 OK                   12ms · TLS
```

Blue indicator. Comment separators. Teal for URLs.

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `120`
- **Padding inside panels**: 1 line top/bottom, 1 char left/right
- **Gap between components**: 1 empty line
- **Indent level**: 2 spaces

### Alignment Principles

- Left-align content
- Right-align metrics (time, size) in tables
- Clean grid — the night is organized, not chaotic

## 7. Icons & Indicators

| Purpose | Icon | Fallback (ASCII) |
|---------|------|-------------------|
| Success | `✓` | `+` |
| Error | `✗` | `x` |
| Warning | `▲` | `!` |
| Info | `●` | `*` |
| Pending | `○` | `o` |
| Running | `▸` | `>` |
| Spinner | `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` | `\|/-` |
| Arrow | `→` | `->` |
| Bullet | `◦` | `-` |
| Selected | `▸` | `>` |
| Lock | `◆` | `#` |
| Unlock | `◇` | `o` |

## 8. Animation & Motion

### Spinners

- Default: `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` at 80ms in Blue
- Network: `◐◓◑◒` at 100ms in Cyan

### Transitions

- No animated transitions — instant, crisp state changes
- Spinners for network/async operations

### Progress

```
  ▕████████████░░░░░░░░▏ 58%
```

- Filled: `█` in Blue, Empty: `░` in Comment
- Caps: `▕` `▏`
- Show percentage
- Green on completion

## 9. Agent Prompt Guide

### Quick Reference

```
Background: #24283b  (storm blue-black)
Foreground: #c0caf5  (soft lavender white)
Blue:       #7aa2f7  (primary)
Purple:     #bb9af7  (secondary)
Cyan:       #7dcfff  (accent/highlights)
Green:      #9ece6a  (success)
Orange:     #e0af68  (warning)
Red-pink:   #f7768e  (error)
Teal:       #73daca  (strings/paths)
Comment:    #565f89  (muted/borders)
Border:     ╭─╮│╰─╯  (rounded, comment color)
Style:      urban night, blue+purple primary, crisp modern, rounded borders
```

### Example Prompts

- "Build an API client TUI: Tokyo Night theme, blue headers, rounded panels, borderless tables with comment dividers, teal for URLs, green/red status codes"
- "Create a modern dashboard: storm blue bg, blue primary accent, purple secondary, rounded muted borders, crisp and clean layout"
- "Design an AI agent interface: Tokyo Night palette, blue for agent actions, purple for thinking indicators, teal for code/output, rounded panels"

## Do's and Don'ts

### Do

- Use Blue as the primary accent — it's the Tokyo Night signature
- Pair Blue with Purple for a cohesive dual-accent feel
- Use Teal for all data/string content
- Use rounded corners — modern and clean
- Keep the Comment color consistent for borders and dim text

### Don't

- Don't use the hot Magenta (#ff007c) as a primary color — it's a rare accent only
- Don't use heavy or double-line borders — too aggressive for this modern theme
- Don't use warm yellows or oranges as primary accents — Tokyo Night is cool-toned
- Don't overcrowd — keep the urban night spacious
- Don't use emoji — sleek Unicode symbols only
