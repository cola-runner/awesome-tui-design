# Cyberpunk — TUI Design System

> Neon lights in dark rain. High contrast, electric colors, data streams. Inspired by Blade Runner, Ghost in the Shell, and the CLI as a hacking interface.

## 1. Theme Overview

- **Mood**: Futuristic, electric, high-energy
- **Density**: Compact — dense information, multiple panels
- **Target**: Hacker tools, security dashboards, network monitors, creative CLI apps, TUI games
- **Terminal**: TrueColor required for best effect, 256-color acceptable

## 2. Color Palette

### Semantic Roles

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#0d0d1a` | `232` | `black` | Deep dark blue-black |
| Foreground | `#e0e0ff` | `189` | `white` | Default text, slight blue tint |
| Primary | `#00ffff` | `51` | `bright cyan` | Cyan neon — main accent |
| Secondary | `#ff00ff` | `201` | `bright magenta` | Magenta neon — secondary |
| Accent | `#ffff00` | `226` | `bright yellow` | Yellow — hot highlights |
| Success | `#00ff88` | `48` | `green` | Neon green |
| Warning | `#ffaa00` | `214` | `yellow` | Orange warning |
| Error | `#ff0044` | `197` | `red` | Hot red/pink |
| Muted | `#4a4a6a` | `60` | `bright black` | Faded blue-gray |
| Surface | `#1a1a2e` | `234` | `black` | Panel background |

### Neon Gradient (for decorative elements)

```
#00ffff → #00ff88 → #ffff00 → #ff00ff → #ff0044
  cyan      green     yellow    magenta     red
```

Use sparingly — for borders, headers, or decorative lines only.

## 3. Typography & ASCII Art

- **Header font**: `cyberlarge` or `slant` (figlet) — angular, aggressive
- **Body text**: plain terminal font
- **Emphasis**: BOLD + neon color, or `reverse` with Primary
- **Code/values**: Primary (cyan) color

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| H1 | figlet `slant` + Primary (cyan) | Splash screen, app title |
| H2 | BOLD + Primary | Section headers |
| H3 | BOLD + Secondary (magenta) | Subsections |
| Body | Foreground | Content text |
| Caption | Muted | Timestamps, metadata |
| Data | Primary (cyan) | Numbers, values, IP addresses |

## 4. Borders & Box Drawing

### Primary Border

```
╔══════════════════╗
║    content       ║
╚══════════════════╝
```

Double-line in Primary (cyan) color.

### Parts Table

| Part | Character | Usage |
|------|-----------|-------|
| top_left | `╔` | Main panels |
| top_right | `╗` | |
| bottom_left | `╚` | |
| bottom_right | `╝` | |
| horizontal | `═` | |
| vertical | `║` | |
| cross | `╬` | |
| tee_down | `╦` | |
| tee_up | `╩` | |
| tee_right | `╠` | |
| tee_left | `╣` | |

### Secondary Border

Heavy single-line in Secondary (magenta) for nested panels:

```
┏━━━━━━━━━━┓
┃  nested  ┃
┗━━━━━━━━━━┛
```

### Dividers

- Horizontal: `═══════════════════` (Primary color)
- Section break: `══╣ SECTION ╠══` (mixed Primary + Accent)
- Data stream: `▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪` (Muted, decorative)

## 5. Components

### Buttons / Actions

```
 ╔═══════════╗   ┏━━━━━━━━━━━┓   ┌───────────┐
 ║ > EXECUTE ║   ┃  CANCEL   ┃   │   HELP    │
 ╚═══════════╝   ┗━━━━━━━━━━━┛   └───────────┘
      ↑                ↑              ↑
  focused(cyan)   unfocused(mag)    muted
```

- Focused: double-border + Primary (cyan) + `>` prefix
- Unfocused: heavy single-border + Secondary (magenta)
- Disabled: single-border + Muted + dim

### Input Fields

```
  TARGET: ║ 192.168.1.1_          ║
          ╚════════════════════════╝
```

- Active: double-line bottom + Primary glow
- Inactive: single-line + Muted
- Error: Error color border + flashing `!`

### Tables

```
╔═══════════════════╦══════════╦═════════╗
║ NODE              ║ STATUS   ║ LATENCY ║
╠═══════════════════╬══════════╬═════════╣
║ node-alpha-01     ║ ● ONLINE ║   12ms  ║
║ node-beta-02      ║ ● ONLINE ║   34ms  ║
║ node-gamma-03     ║ ○ DOWN   ║    --   ║
╚═══════════════════╩══════════╩═════════╝
```

Full borders. Status dots `●` in Success/Error color. Numbers in Primary.

### Lists / Menus

```
  ╔══════════════════════╗
  ║  [1] SCAN NETWORK    ║
  ║  [2] PORT SWEEP      ║
  ║ >[3] TRACE ROUTE     ║
  ║  [4] PACKET CAPTURE  ║
  ║  [0] EXIT            ║
  ╚══════════════════════╝
```

- Selected: `>` + BOLD + Primary (cyan)
- Normal: Foreground
- Hotkey: `[n]` in Accent (yellow)

### Panels / Cards

```
╔══╣ NETWORK TRAFFIC ╠═══════════════════╗
║                                         ║
║  IN  ████████████████░░░░  845 MB/s     ║
║  OUT ██████████░░░░░░░░░░  412 MB/s     ║
║                                         ║
║  ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪  ║
║  PEAK: 1.2 GB/s  AVG: 623 MB/s         ║
║                                         ║
╚═════════════════════════════════════════╝
```

Title with `╣` `╠` markers. Data values in Primary. Labels in Secondary.

### Status Bar

```
║ ● CONNECTED ║ NODE: alpha-01 ║ LATENCY: 12ms ║ ▲ 845MB/s ▼ 412MB/s ║
```

Neon-colored segments. `●` status dot in Success/Error.

## 6. Layout & Spacing

- **Min terminal width**: `100`
- **Ideal terminal width**: `140`
- **Padding inside panels**: 1 line top/bottom, 1 char left/right
- **Gap between components**: 0-1 line (dense!)
- **Indent level**: 2 spaces

### Alignment Principles

- Split layout: multiple panels side by side (like tmux panes)
- Right-align all numbers and metrics
- Center splash screens and titles
- Dense tiling — minimize dead space

## 7. Icons & Indicators

| Purpose | Icon | Fallback (ASCII) |
|---------|------|-------------------|
| Online | `●` | `[*]` |
| Offline | `○` | `[ ]` |
| Success | `✓` | `OK` |
| Error | `✗` | `ERR` |
| Warning | `⚠` | `[!]` |
| Locked | `◆` | `[#]` |
| Unlocked | `◇` | `[.]` |
| Upload | `▲` | `UP` |
| Download | `▼` | `DN` |
| Signal | `█▓▒░` | `####..` |
| Spinner | `◐◓◑◒` | `\|/-` |
| Data | `▪` | `.` |
| Cursor | `▌` | `_` |
| Prompt | `›` | `>` |

## 8. Animation & Motion

### Spinners

- Default: `◐◓◑◒` at 100ms — rotating quarter circle
- Processing: `▰▱▱▱▱` → `▰▰▱▱▱` → `▰▰▰▱▱` → `▰▰▰▰▱` → `▰▰▰▰▰` → `▱▰▰▰▰` → `▱▱▰▰▰` → `▱▱▱▰▰` → `▱▱▱▱▰` → `▱▱▱▱▱` at 80ms

### Transitions

- "Matrix rain" — random characters falling for loading screens
- Text "decode" — random chars → real chars for reveals (30ms/char)
- Glitch — occasional random char replacement for atmosphere (subtle!)

### Progress

```
  ▐████████████░░░░░░░░▌ 58% ▸ SCANNING
```

- Filled: `█` in Primary, Empty: `░` in Muted
- Caps: `▐` `▌`
- Show percentage + action label
- Color shifts from Primary to Success on completion

## 9. Agent Prompt Guide

### Quick Reference

```
Background: #0d0d1a  (deep blue-black)
Foreground: #e0e0ff  (light blue-white)
Primary:    #00ffff  (neon cyan)
Secondary:  #ff00ff  (neon magenta)
Accent:     #ffff00  (electric yellow)
Border:     ╔═╗║╚═╝  (double line, cyan)
Style:      cyberpunk neon, high contrast, dense panels, data-heavy
```

### Example Prompts

- "Build a network dashboard: cyberpunk style, neon cyan borders, magenta secondary panels, dense tile layout, ● status dots, traffic bars, all numbers in cyan"
- "Create a system monitor: dark blue-black bg, double-line cyan borders, ╣TITLE╠ headers, real-time metrics with neon colors, glitch aesthetic"
- "Design a hacker-style menu: numbered options [1]-[9] in yellow, > selector in cyan, bordered box, ALL CAPS, keyboard-driven"

## Do's and Don'ts

### Do

- Use neon colors boldly — this theme IS about color
- Keep backgrounds dark — neon only pops on darkness
- Use double-line borders for main containers
- Pack information densely — multiple panels, split views
- Add decorative elements (▪ dot lines, signal bars) for atmosphere

### Don't

- Don't use light backgrounds — kills the neon effect
- Don't mix too many neon colors in one component (2 max)
- Don't use rounded corners — too soft for cyberpunk
- Don't use emoji — breaks the hacker aesthetic
- Don't use pastel colors — everything should be vivid and electric
