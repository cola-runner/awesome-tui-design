# Nord — TUI Design System

> Arctic, north-bluish clean aesthetic. Based on the [Nord](https://www.nordtheme.com) color palette — inspired by the beauty of the arctic.

## 1. Theme Overview

- **Mood**: Clean, cool, serene
- **Density**: Balanced — structured with clear visual hierarchy
- **Target**: System tools, config editors, monitoring dashboards, professional CLI
- **Terminal**: 256-color minimum, TrueColor recommended

## 2. Color Palette

### Semantic Roles

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#2e3440` | `236` | `black` | Polar Night — darkest |
| Foreground | `#eceff4` | `255` | `white` | Snow Storm — brightest |
| Primary | `#88c0d0` | `110` | `cyan` | Frost — primary accent |
| Secondary | `#81a1c1` | `109` | `blue` | Frost — secondary |
| Accent | `#5e81ac` | `67` | `bright blue` | Frost — deep accent |
| Success | `#a3be8c` | `144` | `green` | Aurora — green |
| Warning | `#ebcb8b` | `222` | `yellow` | Aurora — yellow |
| Error | `#bf616a` | `131` | `red` | Aurora — red |
| Muted | `#4c566a` | `240` | `bright black` | Polar Night — lightest |
| Surface | `#3b4252` | `238` | `black` | Polar Night — raised |

### Extended Nord Palette

| Name | Hex | ANSI 256 | Usage |
|------|-----|----------|-------|
| Nord 7 (Teal) | `#8fbcbb` | `109` | Frost — standalone, classes |
| Nord 12 (Orange) | `#d08770` | `173` | Aurora — urgent, values |
| Nord 13 (Purple) | `#b48ead` | `139` | Aurora — special, decorative |
| Polar 2 | `#434c5e` | `239` | Selection background |

## 3. Typography & ASCII Art

- **Header font**: `small` (figlet) — clean, compact
- **Body text**: plain terminal font
- **Emphasis**: `bold` + Primary (Frost cyan)
- **Code/values**: Nord 7 (Teal)

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| H1 | figlet `small` + Primary | App title |
| H2 | BOLD + Primary | Section headers |
| H3 | BOLD + Secondary | Subsections |
| Body | Foreground (Snow Storm) | Content |
| Caption | Muted (Polar Night) | Help, metadata |
| Data | Teal (Nord 7) | Values, constants |

## 4. Borders & Box Drawing

### Primary Border

```
┌──────────────┐
│   content    │
└──────────────┘
```

Single-line in Muted (Polar Night). Clean and structured.

### Parts Table

| Part | Character | Usage |
|------|-----------|-------|
| top_left | `┌` | Panel corners |
| top_right | `┐` | |
| bottom_left | `└` | |
| bottom_right | `┘` | |
| horizontal | `─` | |
| vertical | `│` | |
| cross | `┼` | Table intersections |
| tee_down | `┬` | |
| tee_up | `┴` | |
| tee_right | `├` | |
| tee_left | `┤` | |

### Dividers

- Horizontal: `──────────────────` (Muted)
- Section break: `── ● ──`

## 5. Components

### Buttons / Actions

```
 ▸ Apply     Cancel     Help
   ↑           ↑         ↑
 focused     normal    muted
```

- Focused: `▸` prefix + reverse (Primary bg) + BOLD
- Normal: Foreground
- Disabled: Muted + dim

### Input Fields

```
  Hostname: ┌────────────────────────┐
            │ 192.168.1.1_           │
            └────────────────────────┘
```

- Active: Primary (Frost) border
- Inactive: Muted border
- Error: Error (Aurora red) border

### Tables

```
  ┌───────────────┬──────────┬─────────┐
  │ Service       │ Status   │ Uptime  │
  ├───────────────┼──────────┼─────────┤
  │ nginx         │ ✓ active │ 14d     │
  │ postgres      │ ✓ active │ 14d     │
  │ redis         │ ✗ down   │ --      │
  └───────────────┴──────────┴─────────┘
```

Full single-line borders. Structured and organized — the Nord way.

### Lists / Menus

```
    System settings
  ▸ Network config
    Security
    Logs
```

- Selected: `▸` + BOLD + Primary
- Normal: Foreground
- Disabled: Muted + dim

### Panels / Cards

```
┌── System Monitor ──────────────┐
│                                 │
│  CPU   ████████░░░░░░░░  52%   │
│  MEM   ██████████████░░  87%   │
│  DISK  ████░░░░░░░░░░░░  28%   │
│                                 │
└─────────────────────────────────┘
```

Title embedded in top border (Primary color). Body in Foreground.

### Status Bar

```
 ▸ connected · node-01 · uptime 14d 3h                   192.168.1.1
```

Primary status indicator. Muted separators.

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `100`
- **Padding inside panels**: 1 line top/bottom, 1 char left/right
- **Gap between components**: 1 empty line
- **Indent level**: 2 spaces

### Alignment Principles

- Left-align content
- Right-align numeric values in tables
- Structured grid feel — consistent spacing

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
| Bullet | `●` | `*` |
| Selected | `▸` | `>` |

## 8. Animation & Motion

### Spinners

- Default: `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` at 80ms in Primary (Frost)
- Subtle: `· ` → `··` → ` ·` → `  ` at 250ms in Secondary

### Transitions

- No animated transitions — instant, predictable state changes
- Spinners for async operations only

### Progress

```
  ▕████████████░░░░░░░░▏ 58%
```

- Filled: `█` in Primary (Frost), Empty: `░` in Muted
- Caps: `▕` `▏`
- Show percentage
- Color shifts to Success on completion

## 9. Agent Prompt Guide

### Quick Reference

```
Background: #2e3440  (Polar Night dark)
Foreground: #eceff4  (Snow Storm bright)
Primary:    #88c0d0  (Frost cyan)
Secondary:  #81a1c1  (Frost blue)
Accent:     #5e81ac  (Frost deep blue)
Success:    #a3be8c  (Aurora green)
Warning:    #ebcb8b  (Aurora yellow)
Error:      #bf616a  (Aurora red)
Muted:      #4c566a  (Polar Night light)
Border:     ┌─┐│└─┘  (single line, muted color)
Style:      arctic clean, cool blues, structured layout, single-line borders
```

### Example Prompts

- "Build a system monitor: Nord palette, single-line bordered panels, frost cyan headers, aurora colors for status, structured grid layout"
- "Create a config editor: dark polar background, frost blue accents, fully bordered tables, ▸ selector, clean and structured"
- "Design a network dashboard: Nord theme, muted borders, frost cyan for active connections, aurora red for errors, aurora green for healthy nodes"

## Do's and Don'ts

### Do

- Use the Frost palette (blues/cyans) as primary accents
- Use Aurora colors only for semantic meaning (green=ok, yellow=warn, red=error)
- Use single-line borders consistently — they are the Nord signature
- Keep the overall feel cool and structured
- Use full borders on tables — Nord is about structure

### Don't

- Don't use rounded corners — too soft, Nord is about clean lines
- Don't use double-line or heavy borders — Nord is understated
- Don't use warm colors as accents — stay in the cool spectrum
- Don't mix too many Aurora colors in one view — save them for meaning
- Don't use emoji — clean Unicode only
