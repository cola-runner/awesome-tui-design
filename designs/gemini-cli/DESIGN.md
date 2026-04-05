# Gemini CLI — TUI Design System

> Google's AI assistant in the terminal. Based on [Gemini CLI](https://github.com/google-gemini/gemini-cli) — colorful, polished, with Google brand gradients and a comprehensive theme system.

## 1. Theme Overview

- **Mood**: Colorful, polished, branded
- **Density**: Balanced — clean conversation with bordered tool blocks
- **Target**: AI agents, branded CLI tools, interactive assistants, developer tools
- **Terminal**: TrueColor recommended for gradient effects, 256-color minimum

## 2. Color Palette

### Semantic Roles

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#1a1a2e` | `234` | `black` | Dark background |
| Foreground | `#e0e0e0` | `253` | `white` | Default text |
| Primary | `#87afff` | `111` | `bright blue` | Blue — primary accent |
| Secondary | `#d7afff` | `183` | `bright magenta` | Purple — secondary |
| Accent | `#87d7d7` | `116` | `bright cyan` | Cyan — info, highlights |
| Success | `#d7ffd7` | `194` | `green` | Green — success |
| Warning | `#ffffaf` | `229` | `yellow` | Yellow — caution |
| Error | `#ff87af` | `211` | `red` | Red/pink — errors |
| Muted | `#808080` | `244` | `bright black` | Borders, dim text |
| Surface | `#2a2a3e` | `236` | `black` | Tool call blocks |

### Google Brand Gradient

```
#4796E4 → #847ACE → #C3677F
  blue      purple     rose
```

Used for banners, spinner, and decorative brand elements. Applied as gradient text via `tinygradient` library where TrueColor is available.

### Built-in Theme System (15+ Themes)

Gemini CLI ships with a comprehensive theme system — users can switch between built-in themes or create custom ones:

| Theme | Style |
|-------|-------|
| Default Dark | Blue/purple/cyan on dark (shown above) |
| Default Light | Same hues on light background |
| Dracula | Purple/pink/green on `#282a36` |
| Tokyo Night | Blue/purple/teal on `#24283b` |
| Solarized Dark | Blue/yellow/green on `#002b36` |
| Solarized Light | Inverse of dark |
| GitHub Dark | Blue/green on `#0d1117` |
| GitHub Light | Same on white |
| Atom One Dark | Blue/green/orange |
| Ayu Dark/Light | Orange/blue accent |

Custom themes can be defined via JSON with a semantic color token architecture (e.g., `ui.active`, `status.warning`, `border.default`).

Built with **React Ink** (not ratatui like Codex).

### Tool Call Border Colors (Semantic)

| State | Color | Hex | Usage |
|-------|-------|-----|-------|
| Running shell | Primary (blue) | `#87afff` | Active shell command |
| Pending tool | Warning (yellow) | `#ffffaf` | Non-shell tool waiting |
| Focused shell | Success (green) | `#d7ffd7` | Shell with focus |
| Completed | Muted (gray) | `#808080` | Finished tool call |

## 3. Typography & ASCII Art

- **Header font**: Block character icon (`▝▜▄` pattern) + "Gemini" text
- **Body text**: plain terminal font
- **Emphasis**: `bold` + Primary, `italic` for status text
- **Code/values**: Accent (cyan)

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| Brand | Gradient text (blue→purple→rose) | Banner, branding |
| H1 | BOLD + Primary (blue) | Section headers |
| H2 | BOLD + Secondary (purple) | Subsections |
| Body | Foreground | AI response text |
| Status | Italic + Muted | Loading status with timer |
| Data | Accent (cyan) | Code, paths, values |
| Keys | BOLD | Keyboard shortcut hints |

## 4. Borders & Box Drawing

### Primary Border

```
╭──────────────╮
│   content    │
╰──────────────╯
```

Rounded borders throughout. Color changes by semantic state.

### Parts Table

| Part | Character | Usage |
|------|-----------|-------|
| top_left | `╭` | Tool call blocks |
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

### Border States

- **Running (shell)**: Primary blue border
- **Pending (non-shell)**: Warning yellow border
- **Focused**: Success green border
- **Completed**: Muted gray border

## 5. Components

### Gradient Spinner (Signature Feature)

```
  ⠋ Thinking... (3.2s)  (esc to cancel)
```

- Braille dots spinner (`⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏`)
- Spinner color cycles through 6-color Google brand gradient at 33fps:
  purple → blue → cyan → green → yellow → red
- Italic status text with elapsed timer
- `(esc to cancel)` hint in Muted

### Brand Banner

```
  ▝▜
  ▗▟▄  Gemini CLI
```

- Block character icon (`▝▜▄` quadrant pattern) — represents the Gemini sparkle
- "Gemini CLI" text in gradient (blue → purple → rose)
- Displayed at startup/header
- The icon uses Unicode quadrant block characters for a compact logo that works in any terminal

### AI Response

```
  Here's how to fix the import issue:

  The problem is that `utils` isn't exported from the
  package root. You need to import it directly:

  `import { helper } from '@pkg/utils/helper'`
```

- Plain Foreground text
- Inline code in Accent (cyan)
- Markdown rendered (bold, code blocks, lists)

### Tool Call Block

```
  ╭─ Shell: npm test ───────────────────╮
  │                                      │
  │  PASS  src/app.test.ts               │
  │    ✓ handles input (12ms)            │
  │    ✓ rejects invalid (3ms)           │
  │                                      │
  │  ✓ 2 passed                          │
  ╰──────────────────────────────────────╯
```

- Border color by state (blue=running, yellow=pending, gray=done)
- Tool name in border header
- Status icons inside:
  - `✓` success (green)
  - `x` error (red)
  - `⊷` executing (blue)
  - `?` confirming (yellow)
  - `o` pending (muted)
  - `-` canceled (muted)

### Permission Prompt

```
  ╭─ Run shell command? ────────────────╮
  │                                      │
  │  $ npm test                          │
  │                                      │
  │  [Y]es  [N]o  [A]lways              │
  ╰──────────────────────────────────────╯
```

- Warning (yellow) border for permission prompts
- Command preview in bold
- Options with highlighted keys

### Status Text

```
  ⠹ Thinking... (3.2s)  (esc to cancel)
```

- **Italic** status text (Gemini uses italic for all loading text)
- Elapsed timer in parentheses, auto-updating
- `(esc to cancel)` hint in Muted — always visible during operations
- Gradient-colored spinner prefix

### Semantic Color Token System

Gemini CLI's theme system uses semantic tokens (not raw colors). This allows themes to be swapped while maintaining meaning:

```
ui.active     → running tool border
ui.focus      → focused tool border
status.ok     → success states
status.warning → pending/caution
status.error  → error states
border.default → completed/inactive
text.primary  → main text
text.secondary → dimmed text
```

Custom themes map these tokens to actual colors. This is why Gemini supports 15+ themes out of the box.

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `120`
- **Padding inside blocks**: 1 line top/bottom, 1 char left/right
- **Gap between messages**: 1 empty line
- **Indent level**: 2 spaces

### Alignment Principles

- Left-aligned conversation flow
- Tool call blocks are full-width with rounded borders
- Brand banner centered at startup
- Status text left-aligned with timer right of text

## 7. Icons & Indicators

| Purpose | Icon | Fallback (ASCII) |
|---------|------|-------------------|
| Success | `✓` | `+` |
| Error | `x` | `x` |
| Executing | `⊷` | `~` |
| Confirming | `?` | `?` |
| Pending | `o` | `o` |
| Canceled | `-` | `-` |
| Spinner | `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` | `\|/-` |
| Cancel hint | `(esc)` | `(esc)` |

## 8. Animation & Motion

### Gradient Spinner (33fps)

- Uses `dots` spinner type from `cli-spinners` library: `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏`
- Spinner color cycles through a **6-color Google brand gradient** at 33fps (~30ms/frame):
  `purple → blue → cyan → green → yellow → red → purple → ...`
- Implemented with `tinygradient` library for smooth color interpolation
- In basic terminals: falls back to static colored dots

### Transitions

- No animated transitions between views
- Streaming text appears as received
- Tool call borders change color by state (blue → gray when done)

### Progress

- Elapsed timer in status text: `(3.2s)`
- No progress bar — timer-based feedback
- Spinner for all async operations

## 9. Agent Prompt Guide

### Quick Reference

```
Background: #1a1a2e  (dark blue-black)
Foreground: #e0e0e0  (light gray)
Blue:       #87afff  (primary, running tools)
Purple:     #d7afff  (secondary, brand)
Cyan:       #87d7d7  (info, code)
Green:      #d7ffd7  (success)
Yellow:     #ffffaf  (warning, pending)
Red/Pink:   #ff87af  (errors)
Gradient:   #4796E4 → #847ACE → #C3677F  (brand)
Border:     ╭─╮│╰─╯  (rounded, color by state)
Style:      colorful branded, gradient spinner, semantic border colors, polished
```

### Example Prompts

- "Build an AI assistant CLI: Gemini style, rounded borders that change color by state (blue=running, yellow=pending, green=focused, gray=done), gradient brand spinner, polished and colorful"
- "Create a branded CLI tool: Gemini aesthetic, gradient text banner, braille dots spinner cycling through brand colors, rounded tool call blocks, ✓/x/⊷ status icons"
- "Design a conversational agent: Gemini-inspired, colorful but structured, semantic border colors, italic status text with elapsed timer, (esc to cancel) hints"

## Do's and Don'ts

### Do

- Use semantic border colors — the state of a tool call should be visible from its border color
- Use the brand gradient for spinner and banner — it's the Google signature
- Use rounded borders for all framed content
- Show elapsed time during async operations
- Use a rich set of status icons (✓ x ⊷ ? o -)

### Don't

- Don't use the gradient everywhere — save it for brand elements and spinner
- Don't use plain monochrome — Gemini is intentionally colorful
- Don't use straight/heavy borders — rounded is the standard
- Don't hide cancel hints — always show `(esc to cancel)` during operations
- Don't skip the elapsed timer — users need feedback on long operations
