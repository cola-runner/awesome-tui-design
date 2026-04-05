# Contributing to awesome-tui-design

We welcome contributions! Here's how you can help.

## Adding a New Theme

### For a color scheme (e.g., Solarized, Monokai)

1. Copy the template:
   ```bash
   cp TEMPLATE.md designs/your-theme/DESIGN.md
   ```

2. Fill in all 9 sections with accurate color values and component examples.

3. Make sure to include:
   - Hex + ANSI 256 + ANSI 16 color mappings for all semantic roles
   - Border character set
   - Component examples (buttons, inputs, tables, lists, panels)
   - Icons with ASCII fallbacks
   - Agent Prompt Guide with quick reference and example prompts
   - Do's and Don'ts

4. Test with the preview tool:
   ```bash
   python3 preview/preview.py designs/your-theme/DESIGN.md
   ```

5. Submit a PR.

### For a TUI application (e.g., Neovim, Spotify TUI)

The bar is higher here — we want **source-code-level accuracy**, not guesswork.

1. Research the application's actual colors and UI patterns:
   - Read the source code for color definitions
   - Check theme/config files for default values
   - Look at the actual rendering code for border styles, icons, layout

2. Document specific details:
   - Exact hex colors from source (not approximations)
   - Specific Unicode characters used for borders, icons, indicators
   - Layout patterns (panel splits, table styles, status bars)
   - Animation details (spinner frames, timing, colors)
   - The framework/library used (Bubbletea, Ratatui, tview, Ink, etc.)

3. Include source links in your PR description.

## Quality Checklist

Before submitting, verify:

- [ ] All 9 sections are filled in
- [ ] Color table has Hex + ANSI 256 + ANSI 16 for all semantic roles
- [ ] Border characters are specified in the parts table
- [ ] At least 4 component examples (buttons, inputs, tables, lists)
- [ ] Icons table with ASCII fallbacks
- [ ] Agent Prompt Guide has quick reference block and 3+ example prompts
- [ ] Do's and Don'ts section (3+ items each)
- [ ] Preview renders correctly: `python3 preview/preview.py designs/your-theme/DESIGN.md`
- [ ] No broken markdown formatting

## Requesting a Theme

Open an issue with:
- Theme/app name
- Why it would be a good addition
- Links to visual references

## Code Contributions

For preview tool improvements, gallery generator, or other tooling:
- Keep dependencies minimal (stdlib Python only for preview tools)
- Test with all existing themes before submitting

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
