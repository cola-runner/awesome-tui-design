# btop — TUI Design System

> Resource monitor that shows usage and stats for processor, memory, disks, network and processes. Based on [btop++](https://github.com/aristocratos/btop) — the beautiful system monitor with 22k+ stars.

## 1. Theme Overview

- **Mood**: Data-dense, gradient-rich, dashboard-style
- **Density**: Very dense — maximize metrics and graphs in every pixel
- **Target**: System monitors, resource dashboards, real-time data displays, IoT panels
- **Terminal**: TrueColor required for gradients, 256-color minimum

## 2. Color Palette

### Semantic Roles

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#000000` | `0` | `black` | Pure black bg |
| Foreground | `#cccccc` | `251` | `white` | Default text |
| Primary | `#eeeeee` | `255` | `bright white` | Titles, headers |
| Secondary | `#77ca9b` | `115` | `green` | CPU accent, healthy |
| Accent | `#dc4c4c` | `167` | `red` | High usage, alerts |
| Success | `#77ca9b` | `115` | `green` | Low usage, healthy |
| Warning | `#cbc06c` | `185` | `yellow` | Medium usage |
| Error | `#dc4c4c` | `167` | `red` | High usage, critical |
| Muted | `#555555` | `240` | `bright black` | Borders, labels |
| Surface | `#111111` | `233` | `black` | Panel interior |

### Box-Specific Accents

| Box | Accent | Hex | Usage |
|-----|--------|-----|-------|
| CPU | Muted green | `#556d59` | CPU panel header/border |
| Memory | Olive | `#6c6c4b` | Memory panel header/border |
| Network | Muted purple | `#5c588d` | Network panel header/border |
| Process | Muted red | `#805252` | Process panel header/border |

### Gradient Ramps (Key Feature)

```
CPU Usage:    #77ca9b → #cbc06c → #dc4c4c  (green → yellow → red)
Temperature:  #4897d4 → #ff40b6            (blue → pink)
Memory Used:  #dc4c4c ramp                 (red shades)
Memory Cache: #4897d4 ramp                 (cyan/blue shades)
Memory Free:  #77ca9b ramp                 (green shades)
```

## 3. Typography & ASCII Art

- **Header font**: None — box titles in panel borders
- **Body text**: plain terminal font, compact
- **Emphasis**: `bold` for titles, values
- **Code/values**: bold + accent color per box

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| Box title | BOLD + box accent color | `cpu`, `mem`, `net`, `proc` |
| Metric value | BOLD + gradient color | `45%`, `2.4 GiB` |
| Metric label | Muted | `cpu0`, `used`, `tx` |
| Process name | Foreground | `firefox`, `node` |
| Highlighted | BOLD + Error red bg | Selected process |

## 4. Borders & Box Drawing

### Primary Border

```
╭── cpu ─────────────────────────────╮
│                                     │
│  ▁▂▃▅▇█▇▅▃▂▁▁▂▄▆█▇▅▃  45%        │
│                                     │
╰─────────────────────────────────────╯
```

Rounded corners. Each box border colored by its accent.

### Parts Table

| Part | Character | Usage |
|------|-----------|-------|
| top_left | `╭` | Box corners |
| top_right | `╮` | |
| bottom_left | `╰` | |
| bottom_right | `╯` | |
| horizontal | `─` | |
| vertical | `│` | |
| cross | `┼` | |
| tee_down | `┬` | |
| tee_up | `┴` | |
| tee_right | `├` | |
| tee_left | `┤` | |

### Title Bracket Style (Signature Detail)

btop uses **inverted corners** for box titles — this is unique to btop:

```
╭─┐cpu┌──────────────────────╮
│                              │
╰────────��─────────────────────╯
```

- Top title: `┐` before title, `┌` after title (inverted!)
- Bottom title (if used): `┘` before, `└` after
- This creates a "notch" effect that makes titles feel embedded in the border

### Dividers

- Inside boxes: `╎` (dotted vertical, U+254E) for column separation
- No horizontal dividers inside boxes — data is packed tight
- Boxes can share edges when adjacent (zero gap)

## 5. Components

### CPU Box

```
╭─┐cpu┌────────────────────────────────────╮
│                                           │
│  ▁▃▅▇█▇▅▃▂▁▂▃▅▇█▇▅▃▂▁  45%  2.4 GHz    │
│                                           │
│  cpu0 ██████████░░░░░░░░░  52%            │
│  cpu1 ████████░░░░░░░░░░░  41%            │
│  cpu2 ████████████████░░░  87%            │
│  cpu3 ██████░░░░░░░░░░░░░  32%            │
│                                           │
╰───────────────────────────────────────────╯
```

- Braille graph at top (⣿⣷⣧⡇ characters)
- Per-core bars: gradient green → yellow → red based on usage
- Percentage values right-aligned in bold

### Memory Box

```
╭─┐mem┌──────────────────────╮
│                              │
│  Used: ████████████░░  4.2G  │
│  Cache: ██████░░░░░░░  2.1G  │
│  Free:  ██░░░░░░░░░░░  0.8G  │
│  Swap:  █░░░░░░░░░░░░  0.2G  │
│                              │
│  Total: 7.3G / 16.0G        │
│                              │
╰──────────────────────────────╯
```

- Used: red gradient bars
- Cache: blue/cyan bars
- Free: green bars
- Values right-aligned

### Network Box

```
╭─┐net┌──────────────────────╮
│                              │
│  ▁▂▃▅▇▅▃▂▁▁▂▅▇█▅▃  Upload  │
│  ▁▁▂▃▃▂▁▁▁▂▃▅▇▇▅▃  Down    │
│                              │
│  ▲ 12.4 MB/s  ▼ 45.2 MB/s   │
│                              │
╰──────────────────────────────╯
```

- Braille graphs for upload/download
- `▲` upload, `▼` download with speed values

### Process Table

```
╭─┐proc┌─────────────────────────────────╮
│ PID    Name         CPU%  MEM%  Status  │
│ 1234   firefox      12.3  4.5%  R       │
│ 5678   node         8.1   2.1%  S       │
│ 9012   postgres     3.2   6.8%  S       │
│ 3456   python3      2.1   1.2%  R       │
╰─────────────────────────────────────────╯
```

- Selected row: bold on Error red bg
- CPU/MEM values colored by gradient
- Status: R(unning) green, S(leeping) muted

### Graphs (3 Render Modes)

btop supports three graph rendering modes with increasing fidelity:

**Braille mode (default, highest resolution):**
```
  ⣿⣷⣧⡇⣿⣷⣧⡇⡇⣧⣷⣿⣿⣷⣧⡇⡇⣧⣷⣿
```
- Characters: `⣿ ⣷ ⣧ ⡇ ⡏ ⠟ ⠛ ⠉` etc. (2x4 dot matrix per cell)
- Each character cell = 8 individually addressable dots
- Effective resolution: 2× width, 4× height of character grid

**Block mode (medium resolution):**
```
  █▟▙▄█▀▟▙▄█▀▀█▟▙▄█▀▟
```
- Characters: `▄ █ ▟ ▙ ▀ ▐ ▌`
- Half-block rendering (2 rows per character height)

**TTY mode (basic, maximum compatibility):**
```
  █▓▒░█▓▒░░▒▓██▓▒░░▒▓█
```
- Characters: `░ ▒ ▓ █`
- 4 density levels per cell

All modes are gradient-colored: green (`#77ca9b`) → yellow (`#cbc06c`) → red (`#dc4c4c`) based on utilization value.

### Meters

```
  cpu0  [■■■■■■■■■■■■■■■░░░░░]  72%
```

- `■` for filled, `░` for empty
- Gradient colored by value

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `120+`
- **Padding inside boxes**: 0-1 lines, minimal
- **Gap between boxes**: 0 (boxes share borders or are adjacent)
- **Indent level**: 1 space

### Alignment Principles

- CPU box: top, full width or left half
- MEM + NET: middle row, side by side
- PROC: bottom or right side, full width
- Layout adapts via presets — multiple arrangements available
- Zero wasted space — every character matters

## 7. Icons & Indicators

| Purpose | Icon | Fallback (ASCII) |
|---------|------|-------------------|
| Upload | `▲` | `UP` |
| Download | `▼` | `DN` |
| Meter filled | `■` | `#` |
| Meter empty | `░` | `.` |
| Graph braille | `⣿⣷⣧⡇` | `█▓▒░` |
| Graph block | `▄█▟▙` | `#.` |
| Running | `R` | `R` |
| Sleeping | `S` | `S` |
| Superscript | `⁰¹²³⁴⁵⁶⁷⁸⁹` | `0-9` |
| Battery | `🔋` | `BAT` |
| Selected | reverse bg | reverse |
| Column sep | `╎` (dotted vert) | `\|` |
| Title left | `┐` (inverted) | `]` |
| Title right | `┌` (inverted) | `[` |

## 8. Animation & Motion

### Spinners

- No traditional spinners — data updates in real-time

### Transitions

- Graph scrolls left as new data arrives
- Values update in-place
- No animated transitions between views

### Progress / Meters

```
  [■■■■■■■■■■■■░░░░░░░░]  62%
```

- Gradient colored: green (<50%) → yellow (50-80%) → red (>80%)
- Updates in real-time
- Multiple graph styles: braille, block, tty

## 9. Agent Prompt Guide

### Quick Reference

```
Background: #000000  (pure black)
Foreground: #cccccc  (light gray)
Titles:     #eeeeee  (bright white)
CPU green:  #77ca9b  (healthy/low)
Warning:    #cbc06c  (medium usage)
Alert red:  #dc4c4c  (high/critical)
Cool blue:  #4897d4  (temperature/cache)
Hot pink:   #ff40b6  (high temperature)
Border:     ╭─╮│╰─╯  (rounded, colored per box)
Style:      dense dashboard, gradient-heavy, braille graphs, black bg, jewel-tone accents
```

### Example Prompts

- "Build a system monitor: btop style, pure black bg, rounded bordered boxes with colored headers, braille graphs colored green→yellow→red by usage, per-core CPU bars"
- "Create a resource dashboard: btop aesthetic, dense packed boxes, gradient colored meters (■░), real-time updating values, braille sparklines"
- "Design a server monitoring TUI: btop layout (CPU top, MEM+NET middle, PROC bottom), box-specific accent colors, gradient coloring by severity, zero wasted space"

## Do's and Don'ts

### Do

- Use gradient coloring — it's btop's signature (green=ok → yellow=warn → red=critical)
- Use braille characters for graphs — highest resolution in terminal
- Use rounded borders with box-specific accent colors
- Pack information as densely as possible
- Color every metric by its severity/value

### Don't

- Don't use flat colors for meters — gradients are essential
- Don't waste space with padding — btop is maximally dense
- Don't use light backgrounds — btop is pure black only
- Don't use single accent color — each box has its own hue
- Don't skip the graphs — sparklines and braille graphs are the visual identity
