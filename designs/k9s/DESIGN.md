# k9s — TUI Design System

> Kubernetes CLI to manage your clusters in style. Based on [k9s](https://github.com/derailed/k9s) — the beloved Kubernetes terminal UI with 28k+ stars.

## 1. Theme Overview

- **Mood**: Cool, utilitarian, Kubernetes-native
- **Density**: Dense — full-width sortable tables with lots of data
- **Target**: Infrastructure dashboards, cluster management, resource monitoring, DevOps tools
- **Terminal**: 256-color minimum, TrueColor recommended

## 2. Color Palette

### Semantic Roles

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#000000` | `0` | `black` | Pure black |
| Foreground | `#5f9ea0` | `73` | `cyan` | CadetBlue — default text |
| Primary | `#00ffff` | `51` | `bright cyan` | Aqua — focused borders, table data |
| Secondary | `#1e90ff` | `33` | `bright blue` | DodgerBlue — borders, keys |
| Accent | `#ff00ff` | `201` | `bright magenta` | Fuchsia — highlights, num keys |
| Success | `#adff2f` | `118` | `bright green` | GreenYellow — modified, healthy |
| Warning | `#ff8c00` | `208` | `yellow` | DarkOrange — pending status |
| Error | `#ff4500` | `202` | `red` | OrangeRed — error status |
| Muted | `#808080` | `244` | `bright black` | Gray — disabled, off |
| Surface | `#1a1a2e` | `234` | `black` | Panel backgrounds |

### k9s-Specific Colors

| Name | Hex | ANSI 256 | Usage |
|------|-----|----------|-------|
| Logo | `#ffa500` | `214` | Orange — ASCII art logo |
| New status | `#87cefa` | `117` | LightSkyBlue — new resources |
| Kill status | `#9370db` | `140` | MediumPurple — terminating |
| Counter | `#ffefd5` | `230` | PapayaWhip — counters |
| Filter | `#2e8b57` | `29` | SeaGreen — active filter |
| Selected row | `#000000` on `#00ffff` | — | Black on Aqua — current row |
| Focused border | `#87cefa` | `117` | LightSkyBlue — focused panel |
| Toggle on | `#32cd32` | `77` | LimeGreen — toggle active |

## 3. Typography & ASCII Art

- **Header font**: Custom ASCII art logo — bold orange K9S
- **Body text**: plain terminal font
- **Emphasis**: `bold` for headers, values
- **Code/values**: Primary (Aqua) for data

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| Logo | ASCII art + Logo orange | K9S splash |
| H1 | BOLD + Primary (Aqua) | Resource type header |
| H2 | BOLD + Secondary (DodgerBlue) | Breadcrumb bar |
| Body | Foreground (CadetBlue) | Table data |
| Caption | Muted | Namespace, age |
| Keys | Accent (Fuchsia) | Keyboard shortcuts |
| Values | Counter (PapayaWhip) | Resource counts |

## 4. Borders & Box Drawing

### Primary Border

```
┌──────────────┐
│   content    │
└──────────────┘
```

Standard box-drawing (tview library style). Bold attribute.

### Parts Table

| Part | Character | Usage |
|------|-----------|-------|
| top_left | `┌` | Panel corners |
| top_right | `┐` | |
| bottom_left | `└` | |
| bottom_right | `┘` | |
| horizontal | `─` | |
| vertical | `│` | |
| cross | `┼` | |
| tee_down | `┬` | |
| tee_up | `┴` | |
| tee_right | `├` | |
| tee_left | `┤` | |

### Border States

- **Default**: Secondary (DodgerBlue)
- **Focused**: LightSkyBlue + bold
- **Search/Command**: Filter (SeaGreen)

## 5. Components

### ASCII Art Logo

```
  ██╗  ██╗ █████╗ ███████╗
  ██║ ██╔╝██╔══██╗██╔════╝
  █████╔╝ ╚█████╔╝███████╗
  ██╔═██╗ ██╔══██╗╚════██║
  ██║  ██╗╚█████╔╝███████║
  ╚═╝  ╚═╝ ╚════╝ ╚══════╝
```

Rendered in bold Logo orange (#ffa500). Displayed at top left with status indicator beside it.

### Breadcrumb Bar

```
  Context: prod-cluster > Namespace: default > Pods
```

- Context/Namespace labels in Secondary (DodgerBlue)
- Values in Primary (Aqua)
- `>` separator in Muted

### Resource Table

```
  NAME                 READY   STATUS    RESTARTS   AGE
  api-server-7d4f     1/1     Running   0          14d
  worker-pool-a3c2    1/1     Running   2          14d
  redis-cache-1b8e    0/1     Error     5          3d
  job-runner-9f1a     1/1     Pending   0          2h
```

- Selected row: **black on Aqua** (reverse highlight)
- Column headers: BOLD + Primary (Aqua)
- Status colored by state:
  - Running: Success (GreenYellow)
  - Pending: Warning (DarkOrange)
  - Error: Error (OrangeRed)
  - Terminating: Kill (MediumPurple)
  - New: LightSkyBlue

### Command Prompt

```
  🐶> /pods api-server
```

- Prompt symbol: `🐶>` in Logo orange (the dog emoji is part of k9s identity)
- `:` for command mode (vim-style)
- `/` for filter mode
- Filter text in Filter (SeaGreen)
- Overlays at top of screen, pushing content down
- Built with **tview** library (Go), using `tview.Flex` for layout

### Toggle Indicators (Log View)

```
  [Wrap: ON]  [Follow: ON]  [Timestamp: OFF]
```

- ON: LimeGreen (`#32cd32`)
- OFF: Gray (`#808080`)
- Used in log views for wrap, follow, timestamp toggles

### Keybinding Bar

```
  <0> all  <1> default  <2> kube-system  | <d> describe  <l> logs  <e> edit
```

- Number keys: Accent (Fuchsia)
- Action keys: Secondary (DodgerBlue)
- Description: Foreground (CadetBlue)
- Separator: `|` in Muted

### Status Indicator

```
  ● Connected to prod-cluster
```

- Info: Primary (Aqua)
- Warning: Warning (DarkOrange)
- Error: Error (OrangeRed)
- Status dot `●` colored by severity

### Resource Status Colors (Kubernetes-Specific)

| State | Color | Named Color | Usage |
|-------|-------|-------------|-------|
| New/Creating | `#87cefa` | LightSkyBlue | Newly created resources |
| Running/Ready | `#adff2f` | GreenYellow | Healthy, running |
| Pending | `#ff8c00` | DarkOrange | Waiting for scheduling |
| Error/CrashLoop | `#ff4500` | OrangeRed | Failed, error state |
| Terminating | `#9370db` | MediumPurple | Being deleted |
| Completed | `#5f9ea0` | CadetBlue | Jobs finished |
| Unknown | `#808080` | Gray | Status unknown |

These are k8s-specific semantic colors — when building any infrastructure dashboard, this color-to-state mapping is the industry standard.

### Log View

```
  2024-01-15 14:32:01 INFO  Starting server on :8080
  2024-01-15 14:32:02 WARN  Cache miss for key "user:123"
  2024-01-15 14:32:05 ERROR Connection refused: redis:6379
```

- Timestamps: Muted
- INFO: Success (GreenYellow)
- WARN: Warning (DarkOrange)
- ERROR: Error (OrangeRed)
- Toggle indicators: LimeGreen (on) / Gray (off) for wrap, follow, etc.

## 6. Layout & Spacing

- **Min terminal width**: `100`
- **Ideal terminal width**: `140+`
- **Padding inside panels**: minimal
- **Gap between components**: 0
- **Indent level**: 2 spaces

### Alignment Principles

- Top: Logo + status indicator + breadcrumbs
- Middle: full-width resource table (the main content)
- Bottom: keybinding hints
- Command prompt overlays at top when activated
- Table columns auto-sized to content
- Layout built with `tview.Flex` — all components are flex containers
- Table is the hero element — it takes 80%+ of screen space

## 7. Icons & Indicators

| Purpose | Icon | Fallback (ASCII) |
|---------|------|-------------------|
| Running | `●` | `*` |
| Pending | `◌` | `o` |
| Error | `●` | `!` |
| Terminating | `●` | `~` |
| New | `●` | `+` |
| Connected | `●` | `*` |
| Toggle on | `●` | `[x]` |
| Toggle off | `○` | `[ ]` |
| Prompt | `🐶>` | `:` |
| Filter | `/` | `/` |
| Selected | reverse bg | reverse |

## 8. Animation & Motion

### Spinners

- No traditional spinners — table data refreshes in real-time

### Transitions

- Table rows update in-place (real-time polling)
- Command prompt appears/disappears instantly
- View switching is instant (no animation)

### Progress

- No progress bars — status shown via colored `●` indicators
- Resource counts update in real-time

## 9. Agent Prompt Guide

### Quick Reference

```
Background: #000000  (pure black)
Foreground: #5f9ea0  (CadetBlue — primary text)
Primary:    #00ffff  (Aqua — focused, data)
Secondary:  #1e90ff  (DodgerBlue — borders, keys)
Accent:     #ff00ff  (Fuchsia — number keys, highlights)
Logo:       #ffa500  (Orange — logo, prompt)
Success:    #adff2f  (GreenYellow — running)
Warning:    #ff8c00  (DarkOrange — pending)
Error:      #ff4500  (OrangeRed — errors)
Selected:   black on Aqua  (reverse highlight)
Border:     ┌─┐│└─┘  (single line, DodgerBlue)
Style:      cool aqua/blue palette, full-width tables, orange logo, dense data
```

### Example Prompts

- "Build a k8s dashboard: k9s style, pure black bg, CadetBlue text, Aqua table headers, DodgerBlue borders, orange ASCII art logo, status-colored rows, fuchsia keybindings"
- "Create a resource manager TUI: k9s aesthetic, full-width sortable tables, breadcrumb navigation, command prompt overlay, reverse-highlight selected row (black on aqua)"
- "Design an infrastructure dashboard: k9s palette, cool blues on black, orange brand accent, status dots (green=ok, orange=pending, red=error, purple=terminating), keybinding bar at bottom"

## Do's and Don'ts

### Do

- Use the CadetBlue/Aqua/DodgerBlue cool palette — it's the k9s identity
- Use orange ONLY for the logo/brand element — it's the warm focal point
- Use full-width tables as the primary content display
- Use reverse highlighting (black on Aqua) for selected rows
- Color-code status indicators by severity

### Don't

- Don't use warm colors as primary palette — k9s is cool-toned
- Don't use rounded corners — k9s uses standard straight borders
- Don't add decorative elements — k9s is utilitarian
- Don't use background colors on table rows (except selected)
- Don't hide the keybinding bar — discoverability matters
