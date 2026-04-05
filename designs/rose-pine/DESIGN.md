# Rosé Pine — TUI Design System

> All natural, nothing artificial. Inspired by the popular [Rosé Pine](https://rosepinetheme.com) color palette. Soft, muted, elegant — the terminal equivalent of a cozy evening.

## 1. Theme Overview

- **Mood**: Warm, soft, cozy
- **Density**: Balanced — readable without feeling sparse
- **Target**: Code editors, note apps, personal tools, writing environments
- **Terminal**: 256-color minimum, TrueColor recommended

## 2. Color Palette

### Semantic Roles (Rosé Pine Main)

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background (Base) | `#191724` | `233` | `black` | Main background |
| Foreground (Text) | `#e0def4` | `189` | `white` | Default text |
| Primary (Rose) | `#ebbcba` | `181` | `bright red` | Key elements, focus |
| Secondary (Iris) | `#c4a7e7` | `183` | `bright magenta` | Supporting, links |
| Accent (Gold) | `#f6c177` | `222` | `yellow` | Highlights, attention |
| Success (Pine) | `#31748f` | `30` | `cyan` | Positive status |
| Warning (Gold) | `#f6c177` | `222` | `yellow` | Caution |
| Error (Love) | `#eb6f92` | `204` | `red` | Error, destructive |
| Muted (Subtle) | `#6e6a86` | `60` | `bright black` | Dim, inactive |
| Surface | `#1f1d2e` | `234` | `black` | Raised surfaces |

### Extended Palette

| Name | Hex | ANSI 256 | Usage |
|------|-----|----------|-------|
| Overlay | `#26233a` | `235` | Popups, menus |
| Highlight Low | `#21202e` | `234` | Subtle hover |
| Highlight Med | `#403d52` | `238` | Active selection |
| Highlight High | `#524f67` | `240` | Strong emphasis |
| Foam | `#9ccfd8` | `152` | Strings, paths |

## 3. Typography & ASCII Art

- **Header font**: `small` (figlet) — delicate, compact
- **Body text**: plain terminal font
- **Emphasis**: `bold` with Rose or Iris, `italic` if terminal supports
- **Code/values**: Foam color

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| H1 | figlet `small` + Rose | App title |
| H2 | BOLD + Rose | Section headers |
| H3 | BOLD + Iris | Subsections |
| Body | Text (foreground) | Content |
| Caption | Subtle (muted) | Help, metadata |
| Data | Foam | Paths, values, strings |

## 4. Borders & Box Drawing

### Primary Border

```
╭──────────────╮
│   content    │
╰──────────────╯
```

Rounded corners in Muted color. Soft and unobtrusive.

### Parts Table

| Part | Character | Color | Usage |
|------|-----------|-------|-------|
| top_left | `╭` | Muted | Panel corners |
| top_right | `╮` | Muted | |
| bottom_left | `╰` | Muted | |
| bottom_right | `╯` | Muted | |
| horizontal | `─` | Muted | |
| vertical | `│` | Muted | |
| cross | `┼` | Muted | Tables |
| tee_down | `┬` | Muted | |
| tee_up | `┴` | Muted | |
| tee_right | `├` | Muted | |
| tee_left | `┤` | Muted | |

Borders are always in Muted color — they frame, not compete.

### Dividers

- Horizontal: `──────────────────` (Muted)
- Section break: `── ◦ ──` (Muted + Rose dot)
- Subtle: dim `│` for vertical separation

## 5. Components

### Buttons / Actions

```
  ▸ Save     Cancel     Help
    ↑          ↑         ↑
 focused    normal     muted
```

- Focused: `▸` prefix + BOLD + Rose bg (reverse)
- Normal: Text color, no decoration
- Disabled: Subtle (muted) + dim

### Input Fields

```
  Title  ──────────────────
         My new note_
```

- Active: Rose color underline, visible cursor
- Inactive: Muted underline
- Error: Love (error) underline + error message in Love

Underline-style inputs — no box borders. Minimal.

### Tables

```
  Name             Role          Status
  ────────────────────────────────────────
  Alice            Developer     ▸ Active
  Bob              Designer      · Idle
  Carol            PM            ▸ Active
```

Borderless. Single divider line in Muted. Clean.

### Lists / Menus

```
    Morning routine
  ▸ Write documentation
    Review pull requests
    Update dependencies
```

- Selected: `▸` prefix + BOLD + Rose
- Normal: 4-space indent + Text
- Disabled: Subtle + dim

### Panels / Cards

```
╭── Notes ──────────────────────╮
│                                │
│  Today I worked on the new     │
│  design system. The colors     │
│  feel right this time.         │
│                                │
│  ◦ 2 min read · edited 1h ago │
╰────────────────────────────────╯
```

Rounded borders in Muted. Title in Rose. Footer metadata in Subtle.

### Tabs

```
 ▸ Notes    Journal    Archive    Settings
 ──────────────────────────────────────────
```

Active: `▸` + Rose + BOLD. Inactive: Subtle.

### Status Bar

```
 ▸ notes.md · 142 words · saved                          ~/documents
```

Rose for active indicator. `·` separators. Right-aligned path in Foam.

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `90`
- **Padding inside panels**: 1 line top/bottom, 1 char left/right
- **Gap between components**: 1 empty line
- **Indent level**: 2 spaces

### Alignment Principles

- Left-align everything
- Right-align only status bar secondary info
- Generous vertical margins
- Let the background breathe — less is more

## 7. Icons & Indicators

| Purpose | Icon | Color | Fallback |
|---------|------|-------|----------|
| Active | `▸` | Rose | `>` |
| Inactive | `·` | Subtle | `.` |
| Success | `✓` | Pine | `+` |
| Error | `✗` | Love | `x` |
| Warning | `!` | Gold | `!` |
| Info | `·` | Iris | `-` |
| Spinner | `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` | Iris | `\|/-` |
| Arrow | `→` | Rose | `->` |
| Bullet | `◦` | Subtle | `o` |
| Dot | `·` | Subtle | `.` |

Minimal, unobtrusive icons. Single-width only.

## 8. Animation & Motion

### Spinners

- Default: `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` at 100ms in Iris
- Gentle: `·  ` → `·· ` → `···` → `·· ` → `·  ` → `   ` at 300ms in Rose

### Transitions

- No animated transitions
- Instant state changes
- Spinner only for async operations

### Progress

```
  ·············◦◦◦◦◦◦◦◦ 58%
```

- Filled: `·` in Rose, Empty: `◦` in Subtle
- Minimal caps — no brackets
- Small, unobtrusive percentage

## 9. Agent Prompt Guide

### Quick Reference

```
Background: #191724  (dark purple-black)
Foreground: #e0def4  (lavender white)
Rose:       #ebbcba  (warm pink — primary)
Iris:       #c4a7e7  (soft purple — secondary)
Gold:       #f6c177  (warm gold — accent)
Foam:       #9ccfd8  (teal — data/code)
Border:     ╭─╮│╰─╯  (rounded, muted color)
Style:      warm, muted, cozy, minimal borders in dim color, lots of breathing room
```

### Example Prompts

- "Build a note-taking app: Rosé Pine palette, rounded dim borders, warm pink accents, underline-style inputs, generous spacing, ▸ for selection"
- "Create a task list: dark purple bg, lavender text, warm pink for active items, ◦ bullets, borderless tables with single dim divider"
- "Design a file browser: Rosé Pine colors, foam/teal for paths, muted borders, ▸ selector, · separators in status bar"

## Do's and Don'ts

### Do

- Use muted/dim borders — they should frame, not shout
- Use Rose sparingly — it's the accent, not the base
- Mix Rose (warm) and Iris (cool) for visual depth
- Use Foam for any data, paths, or code-like content
- Keep the overall feeling cozy and intimate

### Don't

- Don't use bright neon anything — this is a muted theme
- Don't use heavy or double-line borders — too aggressive
- Don't use ALL CAPS — too loud
- Don't use emoji — clean Unicode only
- Don't over-decorate — the beauty is in restraint
