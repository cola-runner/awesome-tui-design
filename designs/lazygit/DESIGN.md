# Lazygit — TUI Design System

> The simple terminal UI for git commands. Based on [Lazygit](https://github.com/jesseduffield/lazygit) — the most popular TUI git client with 54k+ stars.

## 1. Theme Overview

- **Mood**: Functional, clean, panel-driven
- **Density**: Dense — multi-panel layout maximizing information on screen
- **Target**: Git tools, version control UI, multi-panel dashboards, file managers
- **Terminal**: 16-color works, 256-color recommended

## 2. Color Palette

### Semantic Roles

| Role | Hex | ANSI 256 | ANSI 16 | Usage |
|------|-----|----------|---------|-------|
| Background | `#000000` | `0` | `black` | Terminal default (transparent) |
| Foreground | `#d4d4d4` | `252` | `white` | Default text |
| Primary | `#22c55e` | `34` | `green` | Active panel border, current branch |
| Secondary | `#3b82f6` | `33` | `blue` | Selected line bg, keybinding hints |
| Accent | `#06b6d4` | `38` | `cyan` | Search mode, branch recency, cherry-pick |
| Success | `#22c55e` | `34` | `green` | Upstream synced `✓`, added lines |
| Warning | `#eab308` | `220` | `yellow` | Diverged status `↓↑`, marked commits |
| Error | `#ef4444` | `196` | `red` | Unstaged changes, removed lines |
| Muted | `#6b7280` | `243` | `bright black` | Inactive borders, secondary text |
| Surface | `#1e3a5f` | `24` | `blue` | Selected line background |

### Git-Specific Colors

| Name | Hex | ANSI 16 | Usage |
|------|-----|---------|-------|
| Staged | `#22c55e` | `green` | Staged files |
| Unstaged | `#ef4444` | `red` | Unstaged/modified files |
| Untracked | `#ef4444` | `red` | New untracked files |
| Merged PR | `#d946ef` | `magenta` | Merged pull requests |
| Open PR | `#22c55e` | `green` | Open pull requests |
| Closed PR | `#ef4444` | `red` | Closed pull requests |
| Unknown remote | `#d946ef` | `magenta` | Unknown remote `?` |
| Cherry-picked | cyan bg + blue fg | `cyan` bg | Cherry-picked commit highlight |
| Marked base | yellow bg + blue fg | `yellow` bg | Marked base commit for rebase |
| Branch recency | `#06b6d4` | `cyan` | Time since last commit on branch |
| Commit graph | per-author color | varies | Colored lines in commit graph |

## 3. Typography & ASCII Art

- **Header font**: None — plain text panel titles
- **Body text**: plain terminal font
- **Emphasis**: `bold` for active panel titles, key shortcuts
- **Code/values**: default color, context from position

### Text Hierarchy

| Level | Style | Example Usage |
|-------|-------|---------------|
| Panel title | BOLD + positioned in border | `Status`, `Files`, `Branches` |
| Active content | Foreground | Selected panel content |
| Inactive content | Muted | Unselected panel content |
| Keybindings | Secondary (blue) | Bottom help bar |
| Branch name | Primary (green) + `*` | Current branch |
| Diff header | BOLD | File paths in diff |

## 4. Borders & Box Drawing

### Primary Border (Active Panel)

```
╭── Branches ──────────────╮
│ * main                    │
│   feature/auth            │
│   fix/typo                │
╰───────────────────────────╯
```

Rounded corners. Active panel: **green bold** border. Inactive panel: default/muted.

### Parts Table

| Part | Character | Usage |
|------|-----------|-------|
| top_left | `╭` | Panel corners |
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

### Border Style Options

Lazygit supports multiple border styles in config:

| Style | Characters | Look |
|-------|-----------|------|
| `rounded` (default) | `╭╮╰╯─│` | Modern, smooth corners |
| `single` | `┌┐└┘─│` | Classic straight corners |
| `double` | `╔╗╚╝═║` | Heavy, emphatic |
| `bold` | `┏┓┗┛━┃` | Thick single-line |
| `hidden` | no visible border | Borderless panels |

### Border States

- **Active panel**: Primary (green) + bold
- **Inactive panel**: Muted (gray / terminal default)
- **Search mode**: Accent (cyan) + bold

### Dividers

- Panel internal: no dividers — items are listed directly
- Panel title: embedded in top border

## 5. Components

### Multi-Panel Layout

```
╭─ Status ──╮╭─ Diff ──────────────────────╮
│ main      ││                              │
│ ↑0 ↓0     ││  @@ -1,3 +1,4 @@            │
╰───────────╯│  func main() {               │
╭─ Files ───╮│ -    old()                    │
│ M app.go  ││ +    new()                    │
│ A util.go ││ +    logger.Info("done")      │
╰───────────╯│  }                            │
╭─ Branches ╮│                              │
│ * main    ││                              │
│   dev     ││                              │
╰───────────╯╰──────────────────────────────╯
```

- Left sidebar (~33%): stacked panels (Status, Files, Branches, Commits, Stash)
- Right main area (~67%): diff view, commit details, merge panel
- `mainPanelSplitMode: flexible` — main panel can split horizontal/vertical
- Bottom: command log (collapsible, 8 lines default)
- `portraitMode: auto` — stacks all panels vertically in narrow terminals (<100 cols)

### Panel Navigation

```
  ╭─ Files (3) ────── 1 of 3 ─╮
  │ M src/app.go               │ ← active: green border
  │ A src/util.go              │
  │ D old/legacy.go            │
  ╰────────────────────────────╯
```

- Active panel: Primary (green bold) border
- Panel title: left-aligned in border
- Item count: `(3)` after title
- Position: `1 of 3` right-aligned in border

### File Status Icons

```
  M src/app.go        (modified — yellow or green if staged)
  A src/util.go       (added — green)
  D old/legacy.go     (deleted — red)
  R src/old → new.go  (renamed — purple)
  ? README.md         (untracked — red)
```

- Status letter prefix: colored by git status
- Staged: green background
- Unstaged: red text

### Branch List

```
  * main              ✓ origin ↑0 ↓0
    feature/auth      3d ago
    fix/typo          1w ago   PR #42 ●
```

- `*` for current branch in Primary (green)
- `✓` for synced, `↑↓` for ahead/behind in Warning (yellow)
- Recency in Accent (cyan)
- PR status circles: green (open), red (closed), magenta (merged)

### Diff View

```
  @@ -1,3 +1,4 @@
   func main() {
  -    old()
  +    new()
  +    logger.Info("done")
   }
```

- Added `+`: Success (green)
- Removed `-`: Error (red)
- Context: Foreground
- Hunk header `@@`: Accent (cyan)

### Keybinding Bar

```
  [q]uit  [enter] expand  [space] stage  [/] filter  [?] help
```

- Keys in `[]`: Secondary (blue)
- Description: Muted

### Status Bar

```
  main → origin/main · ✓ synced · 3 files changed
```

## 6. Layout & Spacing

- **Min terminal width**: `80`
- **Ideal terminal width**: `120+`
- **Padding inside panels**: 0 lines top/bottom, 1 char left
- **Gap between panels**: 0 (panels share borders)
- **Indent level**: 2 spaces

### Alignment Principles

- Left sidebar + right main area (resizable)
- Panels stack vertically in sidebar
- In narrow terminals (`portraitMode`): stack all panels vertically
- Zero wasted space — every pixel carries information

## 7. Icons & Indicators

| Purpose | Icon | Fallback (ASCII) |
|---------|------|-------------------|
| Success | `✓` | `+` |
| Error | `✗` | `x` |
| Warning | `!` | `!` |
| Current | `*` | `*` |
| Synced | `✓` | `ok` |
| Ahead | `↑` | `^` |
| Behind | `↓` | `v` |
| Unknown | `?` | `?` |
| Modified | `M` | `M` |
| Added | `A` | `A` |
| Deleted | `D` | `D` |
| Renamed | `R` | `R` |
| Copied | `C` | `C` |
| Spinner | `\|/-` | `\|/-` |
| PR Open | `●` | `o` |
| PR Merged | `●` | `*` |
| PR Closed | `●` | `x` |

### Nerd Fonts (Optional)

Disabled by default (`nerdFontsVersion: """`). When enabled (`"2"` or `"3"`):
- 700+ file-type icons with per-type hex colors
- Python: `\ued1b`, JavaScript: `\U000f031e`, etc.
- Each icon has a specific color matching the language/filetype

### Commit Graph

```
  * 2d4f8a1  feat: add auth module       (main)
  │ * a1b2c3  fix: handle edge case      (feature/auth)
  │/
  * 9e8d7c6  refactor: clean up utils
  * 1234567  initial commit
```

- Colored lines per author — each contributor gets a unique graph line color
- Commit length indicator shown by default
- Cherry-picked commits: cyan background + blue text
- Marked base commits (for rebase): yellow background + blue text

## 8. Animation & Motion

### Spinners

- Default: `\|/-` at 100ms — classic ASCII
- Loading: simple text "Loading..." with spinner prefix

### Transitions

- No animated transitions — instant panel switches
- Cursor moves between panels instantly
- `animateExplosion: true` (default) — plays a visual explosion effect when nuking the working tree (`git clean -fd`). A fun easter egg that rewards destructive operations with drama

### Progress

- No progress bars — use counters: `1 of 12`
- Spinner prefix for loading states

## 9. Agent Prompt Guide

### Quick Reference

```
Background: terminal default (transparent)
Foreground: terminal default
Active:     green bold  (active panel border, current branch)
Selected:   blue bg     (highlighted item)
Search:     cyan bold   (search mode border)
Staged:     green       (staged files)
Unstaged:   red         (unstaged changes)
Synced:     green ✓     (upstream ok)
Diverged:   yellow ↑↓   (ahead/behind)
Border:     ╭─╮│╰─╯    (rounded)
Style:      multi-panel, dense, functional, green=active cyan=search
```

### Example Prompts

- "Build a git TUI: Lazygit style, left sidebar with stacked panels (Status/Files/Branches/Commits), right diff panel, rounded borders, green active panel, blue selection highlight"
- "Create a multi-panel dashboard: Lazygit layout, rounded borders, green for active panel, muted for inactive, bottom keybinding bar in blue, zero-gap between panels"
- "Design a file manager TUI: Lazygit-inspired panel layout, rounded borders with embedded titles, M/A/D status prefixes, green/red for status colors"

## Do's and Don'ts

### Do

- Use rounded borders — it's the Lazygit signature
- Use green for the active panel border — immediately recognizable
- Use multi-panel layout — sidebar + main area
- Embed panel titles in the top border
- Show item counts and position in borders
- Use keyboard shortcut hints at the bottom

### Don't

- Don't use heavy/double borders — Lazygit is lightweight
- Don't waste space — panels should share borders, zero gap
- Don't colorize everything — use color for meaning (status), not decoration
- Don't use background colors for panels — only for selected line
- Don't hide keybinding hints — discoverability is key
