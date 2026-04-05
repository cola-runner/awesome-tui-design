# Ocean — TUI Design System

> Calm, deep, focused. The serenity of ocean depths. Inspired by deep-sea blues, soft greens, and the feeling of flow state.

## 1. Theme Overview

- **Mood**: Calm, professional, focused
- **Density**: Balanced — comfortable reading with clear hierarchy
- **Target**: Productivity tools, note-taking, task managers, documentation viewers
- **Terminal**: 256-color minimum, TrueColor recommended

## 2. Color Palette

### Semantic Roles

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#0b1929` | `233` | `black` | Deep ocean dark |
| Foreground | `#c8d6e5` | `152` | `white` | Soft blue-white |
| Primary | `#48dbfb` | `81` | `bright cyan` | Sky blue — main accent |
| Secondary | `#0abde3` | `38` | `cyan` | Deeper blue — supporting |
| Accent | `#55efc4` | `85` | `bright green` | Sea foam green |
| Success | `#00d2d3` | `44` | `cyan` | Teal success |
| Warning | `#feca57` | `221` | `yellow` | Sandy yellow |
| Error | `#ff6b6b` | `203` | `red` | Coral red |
| Muted | `#576574` | `60` | `bright black` | Storm gray |
| Surface | `#152d45` | `235` | `black` | Deeper blue surface |

### Depth Scale

| Depth | Hex | Usage |
|-------|-----|-------|
| Shallow | `#1e3a5f` | Active surface, hover |
| Mid | `#152d45` | Default surface |
| Deep | `#0b1929` | Background |
| Abyss | `#060f1a` | Deepest BG, overlays |

## 3. Typography & ASCII Art

- **Header font**: `small` or `mini` (figlet) — understated
- **Body text**: plain terminal font
- **Emphasis**: `bold` + Primary, or `underline` for links
- **Code/values**: Accent (seafoam green)

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| H1 | figlet `small` + Primary | App title |
| H2 | BOLD + Primary | Section headers |
| H3 | BOLD + Foreground | Subsections |
| Body | Foreground | Content |
| Caption | Muted | Timestamps, help |
| Data | Accent (green) | Values, counts |

## 4. Borders & Box Drawing

### Primary Border

```
╭──────────────╮
│   content    │
╰──────────────╯
```

Rounded corners. Soft and approachable.

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

### Secondary Border

Dim single-line (same characters, Muted color) for nested elements.

### Dividers

- Horizontal: `─ ─ ─ ─ ─ ─ ─ ─ ─` (dashed, like gentle waves)
- Section break: `── ~ ──`
- Subtle: `·   ·   ·   ·` (scattered dots, like bubbles)

## 5. Components

### Buttons / Actions

```
 ╭──────────╮   ╭──────────╮   ╭──────────╮
 │ ◆ Save   │   │  Cancel  │   │   Help   │
 ╰──────────╯   ╰──────────╯   ╰──────────╯
     ↑               ↑              ↑
 focused(pri)   unfocused(fg)    muted
```

- Focused: rounded border + Primary color + `◆` prefix
- Unfocused: rounded border + Foreground
- Disabled: rounded border + Muted + dim

### Input Fields

```
  Title: ╭────────────────────────╮
         │ My ocean project_      │
         ╰────────────────────────╯
```

- Active: Primary color border
- Inactive: Muted border
- Error: Error (coral) border

### Tables

```
  Name              Status         Updated
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
  project-alpha     ◆ Active       2h ago
  project-beta      ◇ Paused       1d ago
  project-gamma     ◆ Active       5m ago
```

No outer border. Dashed separator. Clean and open.

### Lists / Menus

```
    project-alpha
  ◆ project-beta
    project-gamma
    project-delta
```

- Selected: `◆` prefix + BOLD + Primary
- Normal: 4-space indent + Foreground
- Disabled: Muted + dim

### Panels / Cards

```
╭── Tasks ─────────────────────╮
│                               │
│  ◆ Review design spec         │
│  ◇ Update dependencies        │
│  ◇ Write tests                │
│                               │
│  3 remaining · 1 complete     │
╰───────────────────────────────╯
```

Title integrated in top border. Footer info in Muted.

### Tabs

```
 ◆ Overview   ◇ Tasks   ◇ Notes   ◇ Settings
 ─────────────────────────────────────────────
```

Active: `◆` + BOLD + Primary. Inactive: `◇` + Muted.

### Status Bar

```
 ◆ project-alpha · 3 tasks · last saved 2m ago                    ~/projects
```

Single line. `◆` status. Separated by ` · `. Right-aligned path.

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `100`
- **Padding inside panels**: 1 line top/bottom, 1 char left/right
- **Gap between components**: 1 empty line
- **Indent level**: 2 spaces

### Alignment Principles

- Left-align all content
- Right-align status bar secondary info
- Generous vertical spacing — don't crowd the interface
- Let the dark background serve as natural separation

## 7. Icons & Indicators

| Purpose | Icon | Fallback (ASCII) |
|---------|------|-------------------|
| Active | `◆` | `*` |
| Inactive | `◇` | `o` |
| Success | `✓` | `+` |
| Error | `✗` | `x` |
| Warning | `△` | `!` |
| Info | `○` | `-` |
| Spinner | `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` | `\|/-` |
| Arrow | `→` | `->` |
| Bullet | `·` | `-` |
| Wave | `~` | `~` |
| Separator | `·` | `.` |

Soft, rounded icons. No sharp edges.

## 8. Animation & Motion

### Spinners

- Default: `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` at 100ms — smooth dots
- Gentle: `○ ◔ ◑ ◕ ●` at 200ms — filling circle

### Transitions

- Gentle fade: dim → normal (text appears softly)
- No harsh flashes or blinks
- Smooth progress, no jumping values

### Progress

```
  ○○○○○○○○○○○○○○○○○○○○ 0%
  ●●●●●●●●●●○○○○○○○○○○ 50%
  ●●●●●●●●●●●●●●●●●●●● 100% ✓
```

- Filled: `●` in Primary, Empty: `○` in Muted
- No frame/caps — floating style
- Show percentage, checkmark on completion

## 9. Agent Prompt Guide

### Quick Reference

```
Background: #0b1929  (deep ocean)
Foreground: #c8d6e5  (soft blue-white)
Primary:    #48dbfb  (sky blue)
Accent:     #55efc4  (seafoam green)
Border:     ╭─╮│╰─╯  (rounded)
Style:      calm ocean, soft blues, rounded borders, generous spacing, no harsh elements
```

### Example Prompts

- "Build a task manager: ocean theme, rounded borders, ◆/◇ status diamonds, sky blue accent, dashed table separators, soft and spacious layout"
- "Create a note viewer: deep blue background, seafoam green for data/code, rounded panels with embedded titles, ── ~ ── section breaks"
- "Design a project dashboard: calm blue palette, ●○ circle progress, · separated status bar, rounded cards with padding"

## Do's and Don'ts

### Do

- Use rounded corners — they define this theme
- Use generous whitespace — the calm is in the breathing room
- Use dashed lines (`─ ─ ─`) for gentle separation
- Use `◆` / `◇` diamonds for selection states
- Keep animations smooth and slow

### Don't

- Don't use double-line or heavy borders — too aggressive
- Don't use ALL CAPS — too loud for this theme
- Don't use bright neon colors — keep everything soft
- Don't use emoji — clean Unicode symbols only
- Don't pack information too densely — this theme values clarity over density
