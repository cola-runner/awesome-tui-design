# Gruvbox — TUI Design System

> Retro groove color scheme with warm earthy tones. Based on [Gruvbox](https://github.com/morhetz/gruvbox) — designed to be easy on the eyes with a distinctive vintage feel.

## 1. Theme Overview

- **Mood**: Warm, earthy, retro-modern
- **Density**: Balanced — readable with strong contrast
- **Target**: Code editors, system tools, developer dashboards, any CLI that needs character
- **Terminal**: 256-color works well, TrueColor recommended

## 2. Color Palette

### Semantic Roles (Gruvbox Dark)

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#282828` | `235` | `black` | bg0 — main background |
| Foreground | `#ebdbb2` | `223` | `white` | fg1 — default text |
| Primary | `#fe8019` | `208` | `bright red` | Orange — primary accent |
| Secondary | `#d3869b` | `175` | `magenta` | Purple — secondary |
| Accent | `#fabd2f` | `214` | `yellow` | Yellow — highlights |
| Success | `#b8bb26` | `142` | `green` | Green |
| Warning | `#fabd2f` | `214` | `yellow` | Yellow |
| Error | `#fb4934` | `167` | `red` | Red |
| Muted | `#665c54` | `59` | `bright black` | bg4 — dim text |
| Surface | `#3c3836` | `237` | `black` | bg1 — raised surface |

### Extended Gruvbox Palette

| Name | Hex | ANSI 256 | Usage |
|------|-----|----------|-------|
| Aqua | `#8ec07c` | `108` | Paths, strings |
| Blue | `#83a598` | `109` | Functions, links |
| Gray | `#928374` | `102` | Comments |
| bg2 | `#504945` | `239` | Selection |
| fg0 (bright) | `#fbf1c7` | `229` | Bold text |
| fg4 (dim) | `#a89984` | `137` | Secondary text |

## 3. Typography & ASCII Art

- **Header font**: `standard` (figlet) — bold, readable
- **Body text**: plain terminal font
- **Emphasis**: `bold` + Orange or Yellow
- **Code/values**: Aqua or Blue

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| H1 | figlet `standard` + Orange | App title |
| H2 | BOLD + Orange | Section headers |
| H3 | BOLD + Yellow | Subsections |
| Body | Foreground (fg1) | Content |
| Caption | Gray | Comments, metadata |
| Data | Aqua | Paths, string values |
| Numbers | Purple | Numeric values |

## 4. Borders & Box Drawing

### Primary Border

```
┌──────────────┐
│   content    │
└──────────────┘
```

Single-line in Gray. Warm but structured.

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

- Horizontal: `──────────────────` (Gray)
- Section break: `── ◆ ──`
- Thick: `━━━━━━━━━━━━━━━━━━` (for emphasis)

## 5. Components

### Buttons / Actions

```
 ▸ Build     Test     Deploy
   ↑          ↑        ↑
 focused    normal   muted
```

- Focused: `▸` + BOLD + reverse (Orange bg)
- Normal: Foreground
- Disabled: Gray + dim

### Input Fields

```
  Search: ┌────────────────────────┐
          │ pattern here_           │
          └────────────────────────┘
```

- Active: Orange border
- Inactive: Gray border
- Error: Red border + Red text

### Tables

```
  ┌───────────────┬──────────┬─────────┐
  │ Package       │ Version  │ Status  │
  ├───────────────┼──────────┼─────────┤
  │ core          │ 2.1.0    │ ✓ ok    │
  │ utils         │ 1.4.2    │ ✓ ok    │
  │ legacy        │ 0.9.1    │ ! old   │
  └───────────────┴──────────┴─────────┘
```

Full single-line borders. Gruvbox loves structure.

### Lists / Menus

```
    src/
  ▸ main.rs
    lib.rs
    Cargo.toml
```

- Selected: `▸` + BOLD + Orange
- Normal: Foreground
- Directory: Blue + bold
- Disabled: Gray + dim

### Panels / Cards

```
┌── Build Output ────────────────┐
│                                 │
│  Compiling core v2.1.0          │
│  Compiling utils v1.4.2         │
│  ✓ Finished in 4.2s            │
│                                 │
└─────────────────────────────────┘
```

Title in Orange. Status in Green/Red. Paths in Aqua.

### Status Bar

```
 ▸ main · 4 crates · ✓ build ok                          target/debug
```

Orange indicator. Gray separators. Aqua for paths.

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `100`
- **Padding inside panels**: 1 line top/bottom, 1 char left/right
- **Gap between components**: 1 empty line
- **Indent level**: 2 spaces

### Alignment Principles

- Left-align content
- Right-align paths and numeric values
- Consistent borders — use them or don't, but be consistent per view

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

## 8. Animation & Motion

### Spinners

- Default: `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` at 80ms in Orange
- Build: `[    ]` → `[=   ]` → `[==  ]` → `[=== ]` → `[====]` at 100ms in Yellow

### Transitions

- No animated transitions
- Instant state changes
- Spinners for builds and async ops

### Progress

```
  [████████████░░░░░░░░] 58%
```

- Filled: `█` in Orange, Empty: `░` in Gray
- Frame: `[` `]` — Gruvbox is a bit more retro
- Show percentage
- Green on completion

## 9. Agent Prompt Guide

### Quick Reference

```
Background: #282828  (dark warm gray)
Foreground: #ebdbb2  (warm cream)
Orange:     #fe8019  (primary)
Yellow:     #fabd2f  (accent/warning)
Green:      #b8bb26  (success)
Red:        #fb4934  (error)
Aqua:       #8ec07c  (paths/strings)
Blue:       #83a598  (links/functions)
Purple:     #d3869b  (secondary)
Gray:       #928374  (comments/borders)
Border:     ┌─┐│└─┘  (single line, gray)
Style:      warm earthy, orange primary, single-line borders, retro-modern
```

### Example Prompts

- "Build a package manager TUI: Gruvbox palette, orange headers, single-line bordered tables, aqua for package names, green/red for status"
- "Create a build tool interface: warm dark bg, orange progress bars, yellow for warnings, [bracket] style progress, bordered output panels"
- "Design a file browser: Gruvbox theme, blue for directories, aqua for files, orange ▸ selector, fully bordered panels, gray separators"

## Do's and Don'ts

### Do

- Use Orange as the primary accent — it's the Gruvbox signature
- Use the warm cream foreground — never pure white
- Use Aqua and Blue for data/paths — they complement the warm tones
- Use full borders on tables and panels — Gruvbox is structured
- Embrace the warm, vintage feel

### Don't

- Don't use cool blues or cyans as primary colors — stay warm
- Don't use rounded corners — single-line straight corners fit better
- Don't use pure white (#ffffff) — the Gruvbox foreground is cream-toned
- Don't overuse Red — save it for actual errors
- Don't use emoji — ASCII/Unicode icons maintain the vintage feel
