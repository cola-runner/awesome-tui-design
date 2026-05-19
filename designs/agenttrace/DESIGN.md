# Agenttrace — TUI Design System

> Dense terminal observability for AI coding agents: rounded dashboard panels, neon health colors, compact metrics, and source-level session triage.

## 1. Theme Overview

- **Mood**: Operational, diagnostic, compact, btop-inspired
- **Density**: Dense but scannable; dashboard-first with table/detail drill-downs
- **Target**: AI coding-agent observability, cost dashboards, local session inspectors
- **Terminal**: 256-color minimum, TrueColor optional
- **Framework**: Go with Bubble Tea, Bubbles table/viewport, and Lip Gloss

## 2. Color Palette

### Semantic Roles

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#07090b` | `232` | `black` | Main terminal/report background |
| Foreground | `#f4f0dd` | `230` | `bright white` | Primary text in reports and high-contrast values |
| Primary | `#5fff00` | `82` | `bright green` | Brand, primary metrics, health emphasis |
| Secondary | `#8a8a8a` | `245` | `bright black` | Help text, secondary labels, panel titles |
| Accent | `#00afff` | `39` | `bright blue` | Links, panel asides, latency charts |
| Success | `#00d787` | `42` | `green` | Positive deltas, good health, clean anomalies |
| Warning | `#ff8700` | `208` | `yellow` | Attention states, warning health |
| Error | `#ff0000` | `196` | `red` | Critical health, failing loops, hard errors |
| Muted | `#444444` | `238` | `bright black` | Borders, separators, inactive frames |
| Surface | `#303030` | `236` | `black` | Inline badges and control chips |

### Neutral Scale

| Step | Hex | Usage |
|------|-----|-------|
| 50 | `#101419` | HTML report panels, low-contrast surfaces |
| 100 | `#303030` | Control chips and status badge backgrounds |
| 200 | `#444444` | Rounded borders and table separators |
| 300 | `#5f5f5f` | Dim inactive affordances |
| 400 | `#8a8a8a` | Captions, help text, secondary labels |
| 500 | `#f4f0dd` | Body text and readable values |

## 3. Typography & ASCII Art

- **Header font**: Plain bold text; no large figlet in the shipped TUI
- **Body text**: Monospace terminal font
- **Emphasis**: `bold` for brand, metric values, panel titles
- **Code/values**: Colored numeric cells and compact abbreviations (`12.4k`, `$0.0842`, `91%`)

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| H1 | Bold + Primary | `agenttrace` dashboard title |
| H2 | Bold + Secondary | Panel titles such as `TOKEN USAGE` |
| H3 | Bold | Detail subsection headings |
| Body | Terminal default | Session names, model names, diagnostics |
| Caption | Secondary/Muted | Key hints, source labels, empty states |
| Label | Secondary + aligned width | Triage labels such as `Top cost` |

## 4. Borders & Box Drawing

### Primary Border

Agenttrace uses Lip Gloss rounded borders for the app frame, dashboard metric cards, panels, badges, and insight cards.

```
╭────────────────────╮
│  HEALTH SCORE      │
│                    │
│        91%         │
╰────────────────────╯
```

### Parts Table

| Part | Character | Usage |
|------|-----------|-------|
| top_left | `╭` | Rounded panel corner |
| top_right | `╮` | Rounded panel corner |
| bottom_left | `╰` | Rounded panel corner |
| bottom_right | `╯` | Rounded panel corner |
| horizontal | `─` | Panel and help separators |
| vertical | `│` | Panel sides |
| cross | `┼` | Tables if intersections are needed |
| tee_down | `┬` | Table header separator if needed |
| tee_up | `┴` | Table footer if needed |
| tee_right | `├` | Left junction |
| tee_left | `┤` | Right junction |

### Secondary Border

Use the same rounded border characters with ANSI `238` for low-emphasis cards. Inline control chips avoid borders and use Surface background instead.

### Dividers

- Horizontal: `────────────────────`
- Health bars: `━━━━━━━━━━━━`
- Token bars: `██████░░░░░`
- Section break: one empty line between dashboard rows

## 5. Components

### Buttons / Actions

Agenttrace uses command chips rather than heavy buttons.

```
  top cost   critical   anomalies   :command   /search
```

- Focused: Surface background (`236`) + Secondary foreground (`245`)
- Unfocused: Same chip style, separated by 1 leading space
- Disabled: Muted text without background

### Input Fields

```
╭────────────────────────────────────────────────────────╮
│ :health <80                                            │
╰────────────────────────────────────────────────────────╯
```

- Active: Rounded border in Muted, command feedback below or in status line
- Inactive: Hidden until `:` or `/` command mode
- Error: Error color for validation feedback; keep input layout stable

### Tables

```
SESSION            SOURCE        COST      TOKENS  HEALTH
01-healthy-ship    Claude Code   $0.0842   12.4k   91% good
02-loop-risk       Codex CLI     $0.2190   31.8k   44% crit
```

- Header: Bold table titles, sortable suffixes for active sort columns
- Numeric columns: Right-aligned
- Health: Green >= 80, orange 50-79, red < 50

### Lists / Menus

```
● 01-healthy-ship         12.4k  91%
● 02-loop-risk            31.8k  44%
● 03-slow-fixture          8.1k  72%
```

- Selected indicator: Table cursor from Bubbles table, or colored `●` in dashboard lists
- Selected style: Bold or table row focus
- Disabled style: Secondary/Muted text

### Panels / Cards

```
╭────────────────────╮
│ TOTAL COST USD     │
│ $0.42              │
│ estimated          │
╰────────────────────╯
```

- Border: Rounded, Muted (`238`)
- Padding: 1 row top/bottom, 2 columns left/right
- Value: Bold colored metric, usually Primary/Accent/Warning

### Tabs

```
Overview  Sessions  Detail  Diagnostics  Diff
```

- Active view: Brand/Primary
- Inactive view: Secondary
- Keep tab labels compact; avoid decorative framing

### Status Bar

```
↑↓:sel Enter:detail 0-4:jump h/c/t/e/a/n:sort /:filt f:health s:source d:diff w:diag Tab:next q:quit
```

- Background: ANSI `235`
- Foreground: ANSI `245`
- Top border: NormalBorder top edge in ANSI `238`

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `110-140`
- **Padding inside panels**: 1 row vertical, 2 columns horizontal
- **Gap between components**: 1 empty line between dashboard bands; 2 spaces between horizontal cards
- **Indent level**: 2 spaces

### Alignment Principles

- Put the high-level dashboard first, then lists and details
- Right-align money, tokens, duration, health, and latency values
- Use compact six-card metric rows on wide terminals; wrap into rows or vertical cards on narrow terminals
- Preserve panel widths with truncation instead of reflowing values unpredictably

## 7. Icons & Indicators

| Purpose | Icon | Fallback (ASCII) |
|---------|------|-------------------|
| Success | `●` | `*` |
| Error | `●` | `x` |
| Warning | `●` | `!` |
| Info | `·` | `-` |
| Pending | `○` | `o` |
| Running | `▶` | `>` |
| Anomaly | `△` | `!` |
| Trend up | `↑` | `^` |
| Trend down | `↓` | `v` |
| Arrow right | `→` | `->` |
| Bullet | `·` | `-` |
| Bar filled | `█` | `#` |
| Bar empty | `░` | `.` |
| Health bar | `━` | `-` |

## 8. Animation & Motion

### Spinners

- Default loading may use Bubble Tea ticks; keep spinner minimal and single-width
- Preferred fallback: `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` at 80ms, or ASCII `|/-\`

### Transitions

- No sliding or animated page transitions
- State changes are immediate; motion is limited to loading/progress feedback

### Progress

```
Reliability  ━━━━━━━━━━━━━━━━░░░░  82%
Performance  ━━━━━━━━━━━━━━░░░░░░  74%
Quality      ━━━━━━━━━━━━━━━━━░░░  88%
Efficiency   ━━━━━━━━━━━━━━━░░░░░  79%
```

- Filled: Primary (`82`) `━`
- Empty: Secondary (`245`) `━`
- Show percentage, no ETA

## 9. Agent Prompt Guide

### Quick Reference

```
Background: #07090b / ANSI 232
Primary:    #5fff00 / ANSI 82
Accent:     #00afff / ANSI 39
Success:    #00d787 / ANSI 42
Warning:    #ff8700 / ANSI 208
Error:      #ff0000 / ANSI 196
Border:     ╭─╮│╰─╯ rounded, ANSI 238
Style:      dense observability dashboard, rounded cards, colored health states
```

### Example Prompts

- "Build an agenttrace-style AI agent cost dashboard with six rounded metric cards, green brand values, cyan latency highlights, and orange/red health warnings."
- "Create a session list TUI using compact table rows: right-align cost/tokens/health, color health green/orange/red, and keep the help bar pinned at the bottom."
- "Design a diagnostics panel with rounded borders, `△` anomaly indicators, `█░` token bars, and `━` health component bars."
- "Make a responsive terminal dashboard that uses one-column cards below 70 columns and six compact cards on wide terminals."

---

## Do's and Don'ts

### Do

- Use rounded Lip Gloss-style borders for all dashboard cards and insight panels.
- Use Primary green only for brand, healthy states, and key values; use Accent cyan for secondary links/asides.
- Keep data dense: metric cards, compact lists, and aligned numeric columns are central to the design.
- Include ASCII fallbacks for symbols because agenttrace is a cross-platform terminal tool.

### Don't

- Do not use large ASCII logos or hero art; agenttrace prioritizes operational data.
- Do not put every line in a different color; use color to encode health, cost, latency, and anomalies.
- Do not rely on emoji-width rendering for core status indicators.
- Do not center table data; only center standalone health scores inside a card.
