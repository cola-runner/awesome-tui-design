# TUI DESIGN.md 标准模板 v0.1

> 将此文件复制为你的 TUI 项目的 `DESIGN.md`，填入你的设计规范。
> AI coding agent（Cursor、Claude Code 等）可以直接消费此文件来生成符合风格的 TUI 界面。

---

# {Theme Name} — TUI Design System

> {一句话描述这个主题的视觉氛围}

## 1. Theme Overview

- **Mood**: {e.g., minimal, warm, futuristic, retro}
- **Density**: {compact / balanced / spacious}
- **Target**: {e.g., developer tools, dashboards, games, AI agents}
- **Terminal**: {minimum requirement, e.g., 256-color, TrueColor}

## 2. Color Palette

### Semantic Roles

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#000000` | `0` | `black` | Main background |
| Foreground | `#ffffff` | `15` | `white` | Default text |
| Primary | `#______` | `___` | `___` | Key actions, focus |
| Secondary | `#______` | `___` | `___` | Supporting elements |
| Accent | `#______` | `___` | `___` | Highlights, links |
| Success | `#______` | `___` | `___` | Positive status |
| Warning | `#______` | `___` | `___` | Caution status |
| Error | `#______` | `___` | `___` | Error status |
| Muted | `#______` | `___` | `___` | Disabled, hints |
| Surface | `#______` | `___` | `___` | Panels, cards |

### Neutral Scale

| Step | Hex | Usage |
|------|-----|-------|
| 50 | `#______` | Subtle backgrounds |
| 100 | `#______` | Borders, dividers |
| 200 | `#______` | Disabled text |
| 300 | `#______` | Placeholder text |
| 400 | `#______` | Secondary text |
| 500 | `#______` | Body text |

## 3. Typography & ASCII Art

- **Header font**: {figlet font name, e.g., `slant`, `standard`, `small`}
- **Body text**: plain terminal font
- **Emphasis**: `bold`, `italic`, `underline`, `dim`
- **Code/values**: `reverse` or specific color

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| H1 | ASCII art / figlet | App title, splash screen |
| H2 | BOLD + Primary color | Section headers |
| H3 | BOLD | Subsection headers |
| Body | Default | Content text |
| Caption | Dim | Help text, timestamps |
| Label | BOLD + Muted | Form labels |

## 4. Borders & Box Drawing

### Primary Border (panels, dialogs)

```
{top_left}{horizontal}{top_right}
{vertical}  content  {vertical}
{bottom_left}{horizontal}{bottom_right}
```

Example:
```
┌──────────┐
│  content  │
└──────────┘
```

### Parts Table

| Part | Character | Usage |
|------|-----------|-------|
| top_left | `_` | |
| top_right | `_` | |
| bottom_left | `_` | |
| bottom_right | `_` | |
| horizontal | `_` | |
| vertical | `_` | |
| cross | `_` | Table intersections |
| tee_down | `_` | |
| tee_up | `_` | |
| tee_right | `_` | |
| tee_left | `_` | |

### Secondary Border (nested, less emphasis)

{Define if different from primary}

### Dividers

- Horizontal: `{e.g., ─────── or ═══════ or -------}`
- Vertical: `{e.g., │ or ║ or |}`
- Section break: `{e.g., ── ✦ ── or --- * ---}`

## 5. Components

### Buttons / Actions

```
[ OK ]    [ Cancel ]    [ ▸ Submit ]
  ↑            ↑             ↑
focused    unfocused     with icon
```

- Focused: `{style, e.g., reverse + Primary color}`
- Unfocused: `{style, e.g., bordered}`
- Disabled: `{style, e.g., dim + muted color}`

### Input Fields

```
Label: [user input here____]
       ↑ cursor blinks
```

- Active: `{border style + color}`
- Inactive: `{border style + color}`
- Error: `{border style + Error color}`

### Tables

```
{example table rendering}
```

### Lists / Menus

```
  Item one
▸ Item two (selected)
  Item three
  Item four (disabled)
```

- Selected indicator: `{e.g., ▸, >, ●, *}`
- Selected style: `{e.g., bold + Primary}`
- Disabled style: `{e.g., dim + strikethrough}`

### Panels / Cards

```
{example panel rendering with title}
```

### Tabs

```
{example tab bar rendering}
```

### Status Bar

```
{example status bar rendering}
```

## 6. Layout & Spacing

- **Min terminal width**: `{e.g., 80}`
- **Ideal terminal width**: `{e.g., 120}`
- **Padding inside panels**: `{e.g., 1 line top/bottom, 2 chars left/right}`
- **Gap between components**: `{e.g., 1 empty line}`
- **Indent level**: `{e.g., 2 spaces}`

### Alignment Principles

- {e.g., "Left-align content, center-align titles"}
- {e.g., "Right-align numbers in tables"}

## 7. Icons & Indicators

| Purpose | Icon | Fallback (ASCII) |
|---------|------|-------------------|
| Success | `✓` | `+` |
| Error | `✗` | `x` |
| Warning | `⚠` | `!` |
| Info | `ℹ` | `i` |
| Pending | `◯` | `o` |
| Running | `▶` | `>` |
| Spinner | `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` | `\|/-` |
| Arrow right | `→` | `->` |
| Arrow down | `↓` | `v` |
| Bullet | `•` | `*` |
| Checkbox on | `☑` | `[x]` |
| Checkbox off | `☐` | `[ ]` |
| Folder | `📁` | `[D]` |
| File | `📄` | `[F]` |

## 8. Animation & Motion

### Spinners

- Default spinner: `{frames and interval}`
- Thinking/AI: `{frames and interval}`

### Transitions

- {e.g., "No animation" / "Fade via dim→normal" / "Slide with cursor movement"}

### Progress

```
{example progress bar rendering}
```

- Style: `{e.g., █░ filled/empty}`
- Show percentage: `{yes/no}`
- Show ETA: `{yes/no}`

## 9. Agent Prompt Guide

> Copy-paste these prompts when asking an AI agent to build TUI components.

### Quick Reference

```
Primary: #______
Accent:  #______
Border:  {character set}
Style:   {mood keywords}
```

### Example Prompts

- "Build a dashboard panel with {theme} style: use {border} borders, {primary} for headers, {muted} for secondary text"
- "Create a form with {theme} style: {input style} inputs, {button style} buttons, {error color} for validation errors"
- "Design a list selector: {selected indicator} for current item, {primary} highlight, {dim} for disabled items"

---

## Do's and Don'ts

### Do

- {e.g., "Use the neutral scale for text hierarchy"}
- {e.g., "Always provide ASCII fallback for icons"}
- {e.g., "Keep layouts functional at 80 columns"}

### Don't

- {e.g., "Don't use more than 2 colors in a single line"}
- {e.g., "Don't rely on TrueColor — always define 256/16 fallbacks"}
- {e.g., "Don't use emoji as primary icons — they have inconsistent widths"}
