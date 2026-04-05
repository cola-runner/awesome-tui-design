# Codex CLI — TUI Design System

> OpenAI's coding agent in the terminal. Based on [Codex CLI](https://github.com/openai/codex) — minimal, adaptive, text-forward with distinctive shimmer animations.

## 1. Theme Overview

- **Mood**: Minimal, monochrome, adaptive, text-forward
- **Density**: Balanced — clean conversation flow with bordered tool blocks
- **Target**: AI coding agents, conversational CLI tools, adaptive terminal apps
- **Terminal**: TrueColor recommended for shimmer effects, 256-color acceptable

## 2. Color Palette

### Semantic Roles

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#000000` | `0` | `black` | Terminal default (adaptive) |
| Foreground | `#e0e0e0` | `253` | `white` | Default text |
| Primary | `#e0e0e0` | `253` | `white` | Main text — monochrome first |
| Secondary | `#808080` | `244` | `bright black` | Dimmed text, continuation |
| Accent | `#22c55e` | `34` | `green` | Success checkmark |
| Success | `#22c55e` | `34` | `green` | Completion ✓, added lines |
| Warning | `#eab308` | `220` | `yellow` | Caution states |
| Error | `#ef4444` | `196` | `red` | Errors, removed lines |
| Muted | `#555555` | `240` | `bright black` | Borders, dim elements |
| Surface | `#1a1a1a` | `234` | `black` | Code block backgrounds |

### Diff Colors (GitHub-Style)

| State | Dark BG | Light BG | Usage |
|-------|---------|----------|-------|
| Added | `#213a2b` | `#dafbe1` | Added line background |
| Removed | `#4a221d` | `#ffebe9` | Removed line background |

### Adaptive Design (Core Principle)

Codex queries the terminal's **actual background color** at runtime using OSC 11 escape sequences and adjusts all styling accordingly. This is not just dark/light mode — it's continuous adaptation:

- Dark terminals: white-on-black blending, darker diff tints
- Light terminals: dark-on-white blending, lighter diff tints
- The shimmer animation blends toward the detected background color per-character
- No hardcoded brand palette — Codex is deliberately unbranded

Built in **Rust with ratatui** (not React Ink like Gemini CLI).

## 3. Typography & ASCII Art

- **Header font**: Animated ASCII art logo — block characters with 36-frame animation
- **Body text**: plain terminal font
- **Emphasis**: `bold` and `dim` — color is secondary to weight
- **Code/values**: dim or muted styling

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| Logo | Animated block art | Startup animation |
| Body | Foreground | AI response text |
| Code | Muted on Surface bg | Code blocks |
| Continuation | `│` prefix + Secondary | Multi-line output |
| End marker | `└` prefix | Output end |
| Caption | Muted + dim | Metadata |

## 4. Borders & Box Drawing

### Primary Border

```
╭──────────────╮
│   content    │
╰──────────────╯
```

Rounded borders for dialogs and onboarding. Minimal use elsewhere.

### Parts Table

| Part | Character | Usage |
|------|-----------|-------|
| top_left | `╭` | Dialog corners |
| top_right | `╮` | |
| bottom_left | `╰` | |
| bottom_right | `╯` | |
| horizontal | `─` | |
| vertical | `│` | Continuation lines (gutter) |
| end | `└` | Output end marker |

### Line Gutter (Primary Output Pattern)

```
  ▌ Running command...
  │ Output line 1
  │ Output line 2
  └ Done.
```

- `▌` (left half-block) as the primary gutter indicator (2-column prefix: `▌ `)
- `│` for continuation lines within tool output
- `└` for the final output line (end marker)
- This gutter pattern replaces traditional borders for most output — Codex avoids boxing content

## 5. Components

### Shimmer Animation (Signature Feature)

```
  • Working...
    ↑ bright spot moves →→→ across the text
```

- A **cosine-wave** sweep moves across the status text at constant speed
- For each character position, the foreground color is blended toward the terminal's background color based on the wave's amplitude at that position
- Creates a moving "spotlight" or "light sweeping across text" effect
- The wave function: `brightness = cos(position - time)`, mapped to color blend ratio
- TrueColor required for smooth gradient; falls back to `•`/`◦` alternating blink in basic terminals
- Spinner symbol is a single bullet `•` (not a frame-based spinner)

### AI Response

```
  Here is the fix for your function. I've updated
  the error handling to properly catch the edge case:
```

- Plain Foreground text
- No prefix, no border
- Minimal chrome

### Tool Execution

```
  │ $ npm test
  │
  │ PASS  src/app.test.ts
  │   ✓ handles valid input (12ms)
  │   ✓ rejects invalid input (3ms)
  │
  │ Tests: 2 passed
  └ ✓ Command completed
```

- Left gutter: `│` in Muted, `└` for end
- Command: `$` prefix, bold
- Output: dimmed
- Completion: `✓` in Success (green)

### Diff View

```
  │ - const old = getValue();
  │ + const result = getNewValue();
  │ + logger.info('Updated');
  └ ✓ Applied changes
```

- Added: Success green background tint
- Removed: Error red background tint
- GitHub-style diff colors

### Startup Animation (10 Variants × 36 Frames)

```
  ▄▀█ █▀█ █▀▀ █▄ █
  █▀█ █▀▀ ██▄ █ ▀█
```

- **10 animation variants**, each with **36 frames** at 80ms/tick:
  - `codex` — the Codex wordmark assembling
  - `openai` — OpenAI logo
  - `blocks` — abstract block patterns
  - `dots` — dot matrix patterns
  - `hash` — hash/grid patterns
  - `shapes` — geometric shapes
  - `lines` — line-based animation
  - `wave` — wave pattern
  - `spiral` — spiral assembly
  - `matrix` — matrix rain style
- Uses block characters: `▄ ▀ █ ▐ ▌ ▝ ▘ ▗ ▖` etc.
- A random variant is selected each session

### Permission Prompt

```
  ╭─────────────────────────────╮
  │ Run: npm test?              │
  │                             │
  │ [Y]es  [N]o  [A]lways      │
  ╰─────────────────────────────╯
```

- Rounded border
- Options with highlighted keys

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `100`
- **Padding inside blocks**: minimal
- **Gap between messages**: 1 empty line
- **Indent level**: 2 spaces (gutter prefix)

### Alignment Principles

- Left-aligned conversation flow
- Left gutter (│└) for tool output blocks
- No right-alignment, no centering (except startup animation)
- Adaptive layout — adjusts to terminal width

## 7. Icons & Indicators

| Purpose | Icon | Fallback (ASCII) |
|---------|------|-------------------|
| Success | `✓` | `+` |
| Error | `✗` | `x` |
| Working | `•` | `*` |
| Working alt | `◦` | `o` |
| Continuation | `│` | `|` |
| End | `└` | `\`` |
| Command | `$` | `$` |
| Gutter | `▌` | `|` |

Minimal icon set — Codex is deliberately sparse.

## 8. Animation & Motion

### Spinners

- Primary: Shimmer effect — cosine wave sweeps across "Working..." text (TrueColor)
- Fallback: `•` / `◦` alternating blink
- No traditional frame-based spinner

### Startup Animation

- 36-frame ASCII art animation at 80ms/frame
- Multiple variants: codex, openai, blocks, dots, hash, shapes
- Uses block characters (▄▀█)

### Transitions

- No animated transitions between states
- Streaming text appears as received from API
- Tool output appears with gutter markers

### Progress

- No progress bars
- Status text with shimmer effect: "Working..."
- Counter: "Reading files... (3/12)"

## 9. Agent Prompt Guide

### Quick Reference

```
Background: terminal default (adaptive)
Foreground: terminal default (adaptive)
Green:      #22c55e  (success ✓ only)
Red:        #ef4444  (errors only)
Muted:      #555555  (gutter, borders)
Diff add:   #213a2b bg  (GitHub green tint)
Diff del:   #4a221d bg  (GitHub red tint)
Border:     ╭─╮│╰─╯  (rounded, rare)
Gutter:     │ └       (tool output)
Style:      monochrome, adaptive, text-forward, shimmer animation, minimal color
```

### Example Prompts

- "Build an AI CLI: Codex style, monochrome text-forward design, │ gutter for tool output, └ end markers, ✓ completion, shimmer animation on working status"
- "Create an adaptive terminal app: Codex aesthetic, auto-detect dark/light terminal, minimal color (green for success, red for errors only), rounded borders for dialogs only"
- "Design a coding agent TUI: Codex-inspired, left gutter │└ for command output, GitHub-style diff colors, animated ASCII art startup, minimal monochrome body text"

## Do's and Don'ts

### Do

- Keep it monochrome — color is the exception, not the rule
- Use the │└ gutter pattern for structured output
- Adapt to the terminal's actual colors when possible
- Use green ✓ ONLY for success, red ONLY for errors
- Make text weight (bold/dim) do most of the visual hierarchy work

### Don't

- Don't use brand colors as persistent accents — Codex is deliberately unbranded
- Don't use background colors on text blocks (except diff highlights)
- Don't use borders around everything — only for dialogs
- Don't use multiple accent colors — monochrome is the identity
- Don't add decorative elements — every visual element must be functional
