# Catppuccin — TUI Design System

> Soothing pastel theme for the high-spirited. Based on [Catppuccin Mocha](https://catppuccin.com), the community-driven pastel palette loved for its gentle aesthetics.

## 1. Theme Overview

- **Mood**: Warm, pastel, soothing
- **Density**: Balanced — comfortable with gentle contrast
- **Target**: Personal tools, editors, music players, chat apps, any cozy CLI
- **Terminal**: TrueColor recommended, 256-color acceptable

## 2. Color Palette

### Semantic Roles (Mocha flavor)

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#1e1e2e` | `234` | `black` | Base |
| Foreground | `#cdd6f4` | `189` | `white` | Text |
| Primary | `#cba6f7` | `183` | `bright magenta` | Mauve — primary accent |
| Secondary | `#89b4fa` | `111` | `bright blue` | Blue — secondary |
| Accent | `#f5c2e7` | `218` | `magenta` | Pink — highlights |
| Success | `#a6e3a1` | `151` | `green` | Green |
| Warning | `#f9e2af` | `223` | `yellow` | Yellow |
| Error | `#f38ba8` | `211` | `red` | Red |
| Muted | `#585b70` | `240` | `bright black` | Surface2 — dim text |
| Surface | `#313244` | `236` | `black` | Surface0 — raised |

### Extended Catppuccin Mocha

| Name | Hex | ANSI 256 | Usage |
|------|-----|----------|-------|
| Rosewater | `#f5e0dc` | `224` | Links, special text |
| Flamingo | `#f2cdcd` | `224` | IDs, highlights |
| Peach | `#fab387` | `216` | Numbers, constants |
| Teal | `#94e2d5` | `152` | Paths, URLs |
| Sky | `#89dceb` | `117` | Operators |
| Lavender | `#b4befe` | `147` | Active indicators |
| Overlay0 | `#6c7086` | `243` | Comments, subtle |
| Mantle | `#181825` | `233` | Deeper background |
| Crust | `#11111b` | `232` | Deepest background |

## 3. Typography & ASCII Art

- **Header font**: `small` (figlet) — gentle, not aggressive
- **Body text**: plain terminal font
- **Emphasis**: `bold` + Mauve or Pink
- **Code/values**: Teal or Peach

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| H1 | figlet `small` + Mauve | App title |
| H2 | BOLD + Mauve | Section headers |
| H3 | BOLD + Blue | Subsections |
| Body | Text (foreground) | Content |
| Caption | Overlay0 | Help, metadata |
| Data | Teal | Paths, URLs |
| Numbers | Peach | Numeric values |

## 4. Borders & Box Drawing

### Primary Border

```
╭──────────────╮
│   content    │
╰──────────────╯
```

Rounded corners in Surface2 (Muted). Soft and inviting.

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
- Section break: `── 🌸 ──` or `── ◦ ──`

## 5. Components

### Buttons / Actions

```
 ▸ Save      Cancel     Help
   ↑           ↑         ↑
 focused     normal    muted
```

- Focused: `▸` prefix + reverse (Mauve bg) + BOLD
- Normal: Foreground
- Disabled: Muted + dim

### Input Fields

```
  Title: ╭────────────────────────╮
         │ My cozy project_       │
         ╰────────────────────────╯
```

- Active: Mauve border
- Inactive: Muted border
- Error: Red border

### Tables

```
  Name              Type          Status
  ──────────────────────────────────────────
  sunrise.mp3       Audio         ▸ Playing
  moonlight.flac    Audio         ○ Queued
  stars.mp3         Audio         ○ Queued
```

Borderless. Muted divider. Gentle presentation.

### Lists / Menus

```
    Library
  ▸ Now Playing
    Playlists
    Settings
```

- Selected: `▸` + BOLD + Mauve
- Normal: Foreground
- Disabled: Muted + dim

### Panels / Cards

```
╭── Now Playing ─────────────────╮
│                                 │
│  ♪ Moonlight Sonata             │
│  ── ◦ ──────────────── ◦ ──    │
│  ▕████████████░░░░░░░░▏ 3:24   │
│                                 │
╰─────────────────────────────────╯
```

Title in Mauve. Song name in Foreground. Progress in Lavender.

### Status Bar

```
 ♪ Playing · Moonlight Sonata · 3:24 / 5:12              ♥ Favorites
```

Lavender active indicator. Muted separators. Pink for favorites.

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `100`
- **Padding inside panels**: 1 line top/bottom, 1 char left/right
- **Gap between components**: 1 empty line
- **Indent level**: 2 spaces

### Alignment Principles

- Left-align content
- Right-align secondary status bar info
- Generous spacing — cozy, not cramped

## 7. Icons & Indicators

| Purpose | Icon | Fallback (ASCII) |
|---------|------|-------------------|
| Success | `✓` | `+` |
| Error | `✗` | `x` |
| Warning | `!` | `!` |
| Info | `●` | `*` |
| Pending | `○` | `o` |
| Running | `▸` | `>` |
| Spinner | `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` | `\|/-` |
| Arrow | `→` | `->` |
| Bullet | `◦` | `o` |
| Selected | `▸` | `>` |
| Music | `♪` | `#` |
| Heart | `♥` | `<3` |

## 8. Animation & Motion

### Spinners

- Default: `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` at 80ms in Mauve
- Gentle: `◜ ◠ ◝ ◞ ◡ ◟` at 150ms in Lavender

### Transitions

- No harsh transitions — instant but gentle state changes
- Spinners for async operations

### Progress

```
  ▕████████████░░░░░░░░▏ 58%
```

- Filled: `█` in Mauve, Empty: `░` in Muted
- Caps: `▕` `▏`
- Shifts to Green on completion

## 9. Agent Prompt Guide

### Quick Reference

```
Background: #1e1e2e  (Base — deep purple-black)
Foreground: #cdd6f4  (Text — soft blue-white)
Mauve:      #cba6f7  (primary accent)
Blue:       #89b4fa  (secondary)
Pink:       #f5c2e7  (highlights)
Green:      #a6e3a1  (success)
Yellow:     #f9e2af  (warning)
Red:        #f38ba8  (error)
Peach:      #fab387  (numbers)
Teal:       #94e2d5  (paths/URLs)
Muted:      #585b70  (borders, dim text)
Border:     ╭─╮│╰─╯  (rounded, muted)
Style:      warm pastels, rounded borders, cozy spacing, mauve primary
```

### Example Prompts

- "Build a music player TUI: Catppuccin Mocha palette, rounded borders in muted gray, mauve accents, ♪ music icons, gentle layout with breathing room"
- "Create a task manager: pastel Catppuccin theme, mauve for active items, peach for deadlines, teal for tags, borderless tables"
- "Design a chat interface: Catppuccin dark base, pink for mentions, blue for links, rounded message bubbles (bordered panels), lavender for timestamps"

## Do's and Don'ts

### Do

- Use Mauve as the signature color — it's the Catppuccin identity
- Use the extended palette (Peach, Teal, Lavender) for semantic color coding
- Use rounded corners — soft and inviting
- Keep the overall feeling warm and cozy
- Use pastel colors at full intensity — they're already soft by nature

### Don't

- Don't use harsh, saturated neon colors — pastels only
- Don't use heavy or double-line borders — too aggressive
- Don't use ALL CAPS headers — too loud
- Don't overcrowd — this theme values breathing room
- Don't use emoji as functional icons — keep ♪ and ♥ as special decorative touches only
