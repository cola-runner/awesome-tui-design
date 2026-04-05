# Dracula — TUI Design System

> Dark, colorful, and easy on the eyes. Based on the beloved [Dracula](https://draculatheme.com) color scheme used by millions of developers.

## 1. Theme Overview

- **Mood**: Dark, vibrant, comfortable
- **Density**: Balanced — clear hierarchy without crowding
- **Target**: Developer tools, code viewers, terminal dashboards, any dev-facing CLI
- **Terminal**: 256-color minimum, TrueColor recommended

## 2. Color Palette

### Semantic Roles

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#282a36` | `236` | `black` | Main background |
| Foreground | `#f8f8f2` | `253` | `white` | Default text |
| Primary | `#bd93f9` | `141` | `bright magenta` | Purple — primary accent |
| Secondary | `#6272a4` | `61` | `bright black` | Comment — muted text |
| Accent | `#ff79c6` | `212` | `magenta` | Pink — highlights, links |
| Success | `#50fa7b` | `84` | `green` | Green — positive |
| Warning | `#f1fa8c` | `228` | `yellow` | Yellow — caution |
| Error | `#ff5555` | `203` | `red` | Red — errors |
| Muted | `#6272a4` | `61` | `bright black` | Comment color — dim info |
| Surface | `#44475a` | `239` | `bright black` | Current line — raised surface |

### Extended Dracula Palette

| Name | Hex | ANSI 256 | Usage |
|------|-----|----------|-------|
| Cyan | `#8be9fd` | `117` | Types, parameters, info |
| Orange | `#ffb86c` | `215` | Constants, numbers |
| Selection | `#44475a` | `239` | Highlighted/selected items |
| Current Line | `#44475a` | `239` | Active row background |

## 3. Typography & ASCII Art

- **Header font**: `slant` or `standard` (figlet) — bold but readable
- **Body text**: plain terminal font
- **Emphasis**: `bold` + Purple or Pink
- **Code/values**: Cyan or Green

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| H1 | figlet `slant` + Purple | App title, splash |
| H2 | BOLD + Purple | Section headers |
| H3 | BOLD + Pink | Subsections |
| Body | Foreground | Content text |
| Caption | Comment (muted) | Help text, metadata |
| Data | Cyan | Numeric values, types |
| Strings | Yellow | String values, paths |

## 4. Borders & Box Drawing

### Primary Border

```
╭──────────────╮
│   content    │
╰──────────────╯
```

Rounded corners in Comment color. Dracula keeps borders subtle.

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

- Horizontal: `──────────────────` (Comment color)
- Section break: `── ◆ ──`

## 5. Components

### Buttons / Actions

```
 ▸ Submit    Cancel    Help
   ↑          ↑        ↑
 focused    normal    muted
```

- Focused: `▸` prefix + BOLD + reverse (Purple bg)
- Normal: Foreground
- Disabled: Comment + dim

### Input Fields

```
  Email: ╭────────────────────────╮
         │ user@example.com_      │
         ╰────────────────────────╯
```

- Active: Purple border
- Inactive: Comment border
- Error: Red border + Red error text below

### Tables

```
  Name              Role          Status
  ──────────────────────────────────────────
  Alice             Developer     ✓ Active
  Bob               Designer      ○ Away
  Carol             DevOps        ✗ Offline
```

No outer border. Comment-colored divider. Clean and readable.

### Lists / Menus

```
    File browser
  ▸ Terminal
    Settings
    Themes
```

- Selected: `▸` + BOLD + Purple
- Normal: Foreground
- Disabled: Comment + dim

### Panels / Cards

```
╭── Git Status ─────────────────╮
│                                │
│  ✓ main        3 ahead        │
│  M src/app.ts  +42  -12       │
│  A README.md   +85            │
│                                │
╰────────────────────────────────╯
```

Title in Purple. File status in Green (added), Red (deleted), Cyan (modified).

### Status Bar

```
 ▸ main · 3 files · ✓ clean                             ~/projects/app
```

Purple active dot. Comment separators. Cyan for paths.

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `120`
- **Padding inside panels**: 1 line top/bottom, 1 char left/right
- **Gap between components**: 1 empty line
- **Indent level**: 2 spaces

### Alignment Principles

- Left-align content
- Right-align status bar secondary info
- Comfortable spacing — readable, not cramped

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
| Bullet | `◆` | `*` |
| Selected | `▸` | `>` |
| Modified | `M` | `M` |
| Added | `A` | `A` |
| Deleted | `D` | `D` |

## 8. Animation & Motion

### Spinners

- Default: `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` at 80ms in Purple
- Processing: `◜ ◠ ◝ ◞ ◡ ◟` at 120ms in Pink

### Transitions

- No animated transitions — instant state changes
- Spinners for async operations only

### Progress

```
  ▕████████████████░░░░░░░░▏ 62%
```

- Filled: `█` in Purple, Empty: `░` in Comment
- Caps: `▕` `▏`
- Show percentage

## 9. Agent Prompt Guide

### Quick Reference

```
Background: #282a36  (dark blue-gray)
Foreground: #f8f8f2  (off-white)
Purple:     #bd93f9  (primary)
Pink:       #ff79c6  (accent/links)
Green:      #50fa7b  (success)
Cyan:       #8be9fd  (info/data)
Yellow:     #f1fa8c  (warning/strings)
Red:        #ff5555  (error)
Orange:     #ffb86c  (constants)
Comment:    #6272a4  (muted/borders)
Border:     ╭─╮│╰─╯  (rounded, comment color)
Style:      dark vibrant, purple+pink accents, rounded borders, dev-focused
```

### Example Prompts

- "Build a git dashboard: Dracula palette, rounded borders in comment gray, purple headers, green/red for diff stats, cyan for file paths"
- "Create a code viewer: dark bg #282a36, Dracula syntax colors (purple keywords, green strings, cyan types), comment-colored line numbers"
- "Design a process monitor: Dracula theme, purple progress bars, pink highlights on warnings, borderless tables with comment dividers"

## Do's and Don'ts

### Do

- Use Purple as the primary accent — it's the Dracula signature
- Use Comment color for all borders and muted elements
- Use the full color palette — Dracula is meant to be colorful
- Pair colors meaningfully: Green for positive, Red for negative, Cyan for info
- Use rounded corners for a modern feel

### Don't

- Don't use background colors other than Background and Current Line
- Don't use bright white — Foreground (#f8f8f2) is off-white by design
- Don't use heavy or double-line borders — too aggressive
- Don't overuse Pink — save it for actual highlights and links
- Don't use emoji — Dracula is clean Unicode
