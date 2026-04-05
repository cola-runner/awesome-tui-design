# Retro — TUI Design System

> Warm amber CRT glow. The feeling of logging into a mainframe at 2 AM. Inspired by classic terminals, roguelikes, and synthwave.

## 1. Theme Overview

- **Mood**: Nostalgic, warm, slightly mysterious
- **Density**: Compact — maximize information density like a real terminal
- **Target**: Retro-styled tools, TUI games, hacker aesthetics, fun CLI apps
- **Terminal**: 16-color works, 256-color recommended

## 2. Color Palette

### Semantic Roles

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#1a1200` | `232` | `black` | Main background |
| Foreground | `#ffb000` | `214` | `yellow` | Default text (amber) |
| Primary | `#ffcc00` | `220` | `bright yellow` | Key actions, headers |
| Secondary | `#cc8800` | `172` | `yellow` | Supporting text |
| Accent | `#ff6600` | `208` | `bright red` | Highlights, warnings |
| Success | `#33ff00` | `82` | `green` | Positive status |
| Warning | `#ffcc00` | `220` | `bright yellow` | Caution (same as Primary) |
| Error | `#ff0033` | `196` | `red` | Error, danger |
| Muted | `#665500` | `58` | `bright black` | Disabled, faded |
| Surface | `#2a2000` | `234` | `black` | Panels |

### CRT Variants

For an extra-authentic look, alternate between amber and green phosphor:

| Variant | Foreground | Muted | Accent |
|---------|-----------|-------|--------|
| Amber (default) | `#ffb000` | `#665500` | `#ff6600` |
| Green Phosphor | `#33ff00` | `#1a7700` | `#66ff33` |

## 3. Typography & ASCII Art

- **Header font**: `banner3` or `standard` (figlet) — big, bold, retro
- **Body text**: ALL CAPS optional for headers, normal case for body
- **Emphasis**: `bold` + `bright` color variant, or `reverse`
- **Code/values**: `reverse` video

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| H1 | figlet `banner3` + Primary | Splash screen |
| H2 | BOLD + ALL CAPS + Primary | Section headers |
| H3 | BOLD + Secondary | Subsections |
| Body | Foreground (amber) | Content |
| Caption | Muted + dim | System messages |
| Label | BOLD + Secondary + `:` suffix | Form labels |

## 4. Borders & Box Drawing

### Primary Border

```
╔══════════════╗
║   content    ║
╚══════════════╝
```

Double-line. Classic mainframe aesthetic.

### Parts Table

| Part | Character | Usage |
|------|-----------|-------|
| top_left | `╔` | Panel corners |
| top_right | `╗` | |
| bottom_left | `╚` | |
| bottom_right | `╝` | |
| horizontal | `═` | Horizontal lines |
| vertical | `║` | Vertical lines |
| cross | `╬` | Table intersections |
| tee_down | `╦` | Header separator |
| tee_up | `╩` | Footer |
| tee_right | `╠` | Left junction |
| tee_left | `╣` | Right junction |

### Secondary Border

Single-line for nested panels:

```
┌──────────┐
│  nested  │
└──────────┘
```

### Dividers

- Horizontal: `════════════════════`
- Section break: `══╡ SECTION ╞══`
- Inline: `···············` (dot leaders)

## 5. Components

### Buttons / Actions

```
╔══════════╗   ┌──────────┐   ┌──────────┐
║ > START  ║   │  CANCEL  │   │   HELP   │
╚══════════╝   └──────────┘   └──────────┘
    ↑               ↑              ↑
  focused       unfocused       muted
```

- Focused: double-line border + Primary + `>` prefix
- Unfocused: single-line border + Secondary
- Disabled: single-line + Muted + dim

### Input Fields

```
PLAYER NAME: [________________]
             ↑ blinking cursor
```

- Active: `[` `]` brackets + Primary color + blinking `_` cursor
- Inactive: `[` `]` + Muted
- Error: `[` `]` + Error color + `!` prefix on error text

### Tables

```
╔═══════════════╦════════╦═══════╗
║ PLAYER        ║ SCORE  ║ LEVEL ║
╠═══════════════╬════════╬═══════╣
║ PLAYER_1      ║ 12,450 ║    7  ║
║ PLAYER_2      ║  8,200 ║    5  ║
║ PLAYER_3      ║  3,100 ║    2  ║
╚═══════════════╩════════╩═══════╝
```

Full double-line borders. ALL CAPS headers.

### Lists / Menus

```
  ┌─────────────────┐
  │   NEW GAME      │
  │ > LOAD GAME     │
  │   OPTIONS       │
  │   QUIT          │
  └─────────────────┘
```

- Selected: `>` prefix + BOLD + Primary
- Normal: 3-space indent + Foreground
- Keyboard hint: right-aligned in Muted `(N)`, `(L)`, etc.

### Panels / Cards

```
╔══╡ SYSTEM STATUS ╞════════════╗
║                                ║
║  CPU .... 45%  ████░░░░░░     ║
║  MEM .... 72%  ███████░░░     ║
║  DSK .... 23%  ██░░░░░░░░     ║
║                                ║
╚════════════════════════════════╝
```

Title with `╡` `╞` inset markers. Dot leaders for labels.

### Status Bar

```
║ HP: ████████░░ 80/100 ║ LVL: 7 ║ GOLD: 1,250 ║ FLR: 3 ║
```

Or for CLI tools:

```
═══ CONNECTED: 192.168.1.1 ═══ UPTIME: 4h23m ═══ STATUS: OK ═══
```

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `80` (authentic!)
- **Padding inside panels**: 1 line top/bottom, 1 char left/right
- **Gap between components**: 1 empty line
- **Indent level**: 2 spaces

### Alignment Principles

- Center the main menu / splash screen
- Left-align body content
- Right-align numeric values
- Use dot leaders (`....`) to connect labels to values

## 7. Icons & Indicators

| Purpose | Icon | Fallback (ASCII) |
|---------|------|-------------------|
| Success | `✓` | `OK` |
| Error | `✗` | `ERR` |
| Warning | `!` | `!` |
| Info | `*` | `*` |
| Pending | `·` | `.` |
| Running | `>` | `>` |
| Spinner | `\|/-` | `\|/-` |
| Arrow | `>` | `>` |
| Bullet | `·` | `*` |
| Selected | `>` | `>` |
| Health full | `█` | `#` |
| Health empty | `░` | `.` |
| Door | `▒` | `D` |
| Player | `@` | `@` |

ASCII-native icons preferred. Keep the retro feel.

## 8. Animation & Motion

### Spinners

- Default: `\|/-` at 150ms — classic ASCII spin
- Processing: `[    ]` → `[=   ]` → `[==  ]` → `[=== ]` → `[ ===]` → `[  ==]` → `[   =]` → `[    ]` at 120ms

### Transitions

- Typewriter effect for important messages (print char by char, 30ms/char)
- Screen "flicker" for errors (rapid dim→bright→dim, 50ms each, 3 cycles)
- No smooth transitions — instant state changes

### Progress

```
  LOADING [████████████░░░░░░░░] 58%
```

- Filled: `█`, Empty: `░`, Frame: `[` `]`
- Show percentage
- Label prefix in ALL CAPS

## 9. Agent Prompt Guide

### Quick Reference

```
Background: #1a1200  (near black)
Foreground: #ffb000  (amber)
Accent:     #ff6600  (orange)
Border:     ╔═╗║╚═╝  (double line)
Style:      retro CRT, amber/green phosphor, double borders, ALL CAPS headers
```

### Example Prompts

- "Build a retro status panel: double-line borders, amber text on dark bg, ╡TITLE╞ inset headers, dot leaders for label-value pairs, ASCII progress bars"
- "Create a game menu: centered, bordered box, > selector, ALL CAPS items, keyboard hints in dim text"
- "Design a dashboard: 80-column layout, double-border panels, ████░░░░ bars for metrics, ASCII spinner for loading"

## Do's and Don'ts

### Do

- Use double-line borders for primary containers
- Use dot leaders for label-value pairs
- Keep to 80 columns — this is part of the aesthetic
- Use ALL CAPS for headers and labels
- Stick to ASCII-range characters where possible

### Don't

- Don't use emoji — breaks the retro immersion completely
- Don't use TrueColor gradients — the 16/256 palette IS the aesthetic
- Don't use rounded corners (`╭╮╰╯`) — too modern
- Don't over-color — amber/green monochrome is the goal, color is for status only
- Don't use smooth animations — the charm is in the chunkiness
