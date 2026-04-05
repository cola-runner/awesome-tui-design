# Claude Code — TUI Design System

> The AI coding agent that lives in your terminal. Based on [Claude Code](https://claude.ai/claude-code) by Anthropic — warm, playful, and content-forward with a signature terracotta accent.

## 1. Theme Overview

- **Mood**: Warm, playful, content-forward
- **Density**: Balanced — clean conversation flow, minimal chrome
- **Target**: AI coding agents, conversational terminal interfaces, developer tools
- **Terminal**: TrueColor recommended for shimmer effects, 256-color acceptable

## 2. Color Palette

### Semantic Roles

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#1a1a1a` | `234` | `black` | Terminal default dark bg |
| Foreground | `#ffffff` | `15` | `bright white` | Default text, AI responses |
| Primary | `#d77757` | `173` | `yellow` | Terracotta — Anthropic brand accent |
| Secondary | `#fd5db1` | `206` | `bright magenta` | Hot pink — bash/tool borders |
| Accent | `#b1b9f9` | `147` | `bright blue` | Lavender — permission dialogs |
| Success | `#4eba65` | `71` | `green` | Green — completion |
| Warning | `#ffc107` | `220` | `yellow` | Amber/gold — caution |
| Error | `#ff6b80` | `204` | `red` | Soft red-pink — errors |
| Muted | `#888888` | `245` | `bright black` | Gray — input borders, inactive |
| Surface | `#373737` | `237` | `black` | User message background |

### Claude-Specific Colors

| Name | Hex | Usage |
|------|-----|-------|
| Claude shimmer | `#eb9f7f` | Lighter terracotta for shimmer animation |
| Bash border | `#fd5db1` | Hot pink tool execution borders |
| Permission | `#b1b9f9` | Lavender-blue permission dialogs |
| Auto-accept | `#af87ff` | Purple — YOLO/auto-accept mode |
| Inactive | `#999999` | Gray — disabled elements |
| Subtle | `#505050` | Dark gray — separators |
| Diff added bg | `#225c2b` | Green tint for added lines |
| Diff removed bg | `#7a2936` | Red tint for removed lines |

## 3. Typography & ASCII Art

- **Header font**: None — Claude Code doesn't use figlet; clean text only
- **Body text**: plain terminal font, monospaced
- **Emphasis**: `bold` for headers, `dim` for metadata
- **Code/values**: syntax-highlighted in response

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| H1 | BOLD + Primary (terracotta) | Session header |
| Body | Foreground (white) | AI response text |
| Code | Syntax highlighted | Code blocks |
| User input | `>` prefix on Surface bg | User messages |
| Caption | Muted + dim | Token counts, timestamps |
| Thinking | Primary (terracotta) + shimmer | Thinking verb |

## 4. Borders & Box Drawing

### Input Box (Dashed ASCII — Signature Style)

```
- - - - - - - - - - - - - - - -
| > your message here_          |
- - - - - - - - - - - - - - - -
```

**No Unicode box-drawing for input** — plain ASCII dashed lines (`-` horizontal, `|` vertical). Border is Muted gray with shimmer between `#888` and `#A6A6A6`. This is a deliberate design choice — casual, not corporate.

### Tool Call Border (Hot Pink)

```
┌─ Bash ─────────────────────────┐
│ $ npm test                      │
│                                 │
│ PASS  src/app.test.ts           │
│   ✓ handles input (12ms)       │
└─────────────────────────────────┘
```

Tool/bash output uses box-drawing with hot pink (`#fd5db1`) borders.

### Permission Dialog (Lavender)

```
┌─ Allow Edit to src/app.ts? ────┐
│                                 │
│  [Y]es  [N]o  [A]lways         │
│                                 │
└─────────────────────────────────┘
```

Permission prompts use lavender (`#b1b9f9`) borders.

### Parts Table

| Part | Character | Color | Usage |
|------|-----------|-------|-------|
| Input horizontal | `-` (dashed) | Muted gray | Input box |
| Input vertical | `\|` | Muted gray | Input box sides |
| Tool top_left | `┌` | Hot pink | Tool call blocks |
| Tool horizontal | `─` | Hot pink | Tool call blocks |
| Tool vertical | `│` | Hot pink | Tool call blocks |
| Tool bottom_left | `└` | Hot pink | Tool call blocks |
| Permission border | `┌─┐│└─┘` | Lavender | Permission dialogs |

### Dividers

- Between messages: subtle thin line in `#505050`
- No heavy separators — content flows naturally

## 5. Components

### User Prompt

```
- - - - - - - - - - - - - - - - -
|  > What does this function do?  |
- - - - - - - - - - - - - - - - -
```

- Dashed ASCII border in Muted gray (shimmering)
- `>` prefix
- Background: Surface (`#373737`)

### Thinking Indicator (Signature Feature)

```
  ✳ Percolating...
```

- Spinner cycles through 6 symbols: `· ✢ ✳ ✶ ✻ ✽` then reverses
- 120ms interval per frame
- Rendered in Primary terracotta with shimmer to `#eb9f7f`
- Paired with a random whimsical verb from ~184 options:
  "Cogitating...", "Percolating...", "Shenaniganing...", "Moonwalking...", "Ruminating..."

### AI Response

```
  This function parses the configuration file and returns
  a structured object. Here's what each part does:

  ...
```

- White text on terminal default background
- Markdown rendered with syntax highlighting
- No border, no prefix — clean content-forward

### Tool Call Block

```
  ┌─ Read: src/config.ts ─────────────────┐
  │                                         │
  │  1 │ export function parseConfig() {    │
  │  2 │   const raw = readFileSync(path);  │
  │  3 │   return JSON.parse(raw);          │
  │                                         │
  └─────────────────────────────────────────┘
```

- Hot pink (`#fd5db1`) border — visually distinct from text
- Tool name and file path in border header
- Code with syntax highlighting inside
- Background: `rgb(65,60,65)` for bash output

### Diff View

```
  ┌─ Edit: src/app.ts ─────────────────────┐
  │                                         │
  │  - const old = getValue();              │
  │  + const result = getNewValue();        │
  │  + logger.info('Updated');              │
  │                                         │
  └─────────────────────────────────────────┘
```

- Added lines: `+` prefix, `#225c2b` background tint
- Removed lines: `-` prefix, `#7a2936` background tint
- Hot pink border (same as tool calls)

### Permission Prompt

```
  ┌─ Allow Bash: npm test? ──────────────┐
  │                                       │
  │  [Y]es  [N]o  [A]lways               │
  │                                       │
  └───────────────────────────────────────┘
```

- Lavender (`#b1b9f9`) border
- Options with key highlighted in bold

### Status Bar (Bottom)

```
  Opus · 12.4K tokens · $0.04 · 3.2s · normal
```

- Persistent bottom line
- Token count, cost, elapsed time, effort level
- Muted color

### Subagent Indicators

Each subagent gets a unique color from a palette:
red, blue, green, yellow, purple, orange, pink, cyan

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `120`
- **Padding inside tool blocks**: 1 line top/bottom, 1 char left/right
- **Gap between messages**: 1 line with subtle separator
- **Indent level**: 2 spaces

### Alignment Principles

- Left-align all conversation content
- Tool call blocks are indented slightly
- Status bar persistent at bottom
- No centering except startup logo
- Conversation flows top-to-bottom

## 7. Icons & Indicators

| Purpose | Icon | Fallback (ASCII) |
|---------|------|-------------------|
| Success | `✓` | `+` |
| Error | `✗` | `x` |
| Warning | `⚠` | `!` |
| Thinking | `· ✢ ✳ ✶ ✻ ✽` | `*` |
| Prompt | `>` | `>` |
| Running | `▸` | `>` |
| Bullet | `•` | `-` |

## 8. Animation & Motion

### Thinking Spinner (Signature)

```
Frames: · → ✢ → ✳ → ✶ → ✻ → ✽ → ✻ → ✶ → ✳ → ✢ → · ...
```

- 120ms per frame
- Primary terracotta color with shimmer to lighter terracotta
- Reverse-mirror cycle (goes up then back down)
- Random whimsical verb: "Cogitating...", "Percolating...", "Moonwalking..."

### Input Border Shimmer

- Dashed input border shimmers between `#888888` and `#A6A6A6`
- Subtle, gentle animation

### Transitions

- No animated transitions between states
- Streaming text appears as received from API
- Tool blocks appear with distinct hot pink border

### Progress

- Counter-based: "Reading files... (3/12)"
- No progress bars
- Spinner + verb for indeterminate waits

## 9. Agent Prompt Guide

### Quick Reference

```
Background: terminal default (dark)
Foreground: #ffffff  (white)
Terracotta: #d77757  (brand primary — thinking, accents)
Hot pink:   #fd5db1  (tool/bash call borders)
Lavender:   #b1b9f9  (permission dialogs)
Green:      #4eba65  (success)
Red-pink:   #ff6b80  (errors)
Amber:      #ffc107  (warnings)
Purple:     #af87ff  (auto-accept mode)
Gray:       #888888  (input borders, muted)
Input:      - - | -  (dashed ASCII, NOT Unicode box-drawing)
Tool:       ┌─┐│└─┘  (single line, hot pink)
Style:      warm terracotta accent, dashed input, hot pink tools, whimsical thinking verbs
```

### Example Prompts

- "Build an AI chat CLI: Claude Code style, dashed ASCII input border, hot pink bordered tool call blocks, terracotta thinking spinner with random verbs, white response text"
- "Create a coding agent TUI: warm terracotta accent, lavender permission dialogs, hot pink for tool execution, whimsical spinner (· ✢ ✳ ✶ ✻ ✽), status bar with token count"
- "Design a conversational CLI: Claude Code aesthetic, minimal chrome, dashed input box, colored tool borders (pink=bash, lavender=permission), shimmer animations"

## Do's and Don'ts

### Do

- Use terracotta (`#d77757`) as the primary brand accent — it's warm and distinctive
- Use dashed ASCII borders for input — NOT Unicode box-drawing (this is deliberate)
- Use hot pink for tool call borders — makes them visually pop
- Use whimsical, playful language for loading states
- Keep response text pure white — readability is paramount

### Don't

- Don't use cold/corporate blues as primary accent — Claude Code is warm
- Don't use Unicode box-drawing for the input area — dashed ASCII is the signature
- Don't over-border — most content should flow without frames
- Don't use generic "Loading..." — the random verbs are part of the personality
- Don't colorize AI response body text — white for trust and readability
