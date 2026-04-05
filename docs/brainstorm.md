# TUI Art - 终端视觉资产库 构思记录

> 初始讨论时间: 2026-04-05

## 核心洞察

TUI/CLI 应用正在爆发（AI Agent CLI、DevOps 工具、创意工具等），但终端视觉素材生态几乎为零。每个项目都在重复造轮子。

## 现有方案及其不足

### Nerd Fonts
- 本质是给编程字体打补丁，把多个图标集的 glyph 塞进字体的 Private Use Area
- **不是专为终端设计**，只是在终端场景最常用
- 局限性：
  - 必须用户手动安装补丁字体
  - 无运行时检测能力（程序不知道用户装没装）
  - 部分 glyph 宽度渲染有问题
  - 只覆盖小图标，不涉及大型素材

### 各 TUI 框架自带符号
- Go (Bubbletea/Charm.sh)、Rust (Ratatui)、Python (Rich) 各自为战
- 没有统一标准

## 产品定位

**终端视觉资产平台** — 从小图标到大型装饰素材，一站式解决终端应用的视觉需求。

不是简单收集 Unicode 字符，而是解决实际问题。

## 需求光谱

```
图标            小素材              大素材/装饰
✓ ✗ ⟳          ┌──────┐           ╔══════════════╗
状态指示         │ 进度条 │          ║  ASCII Logo  ║
导航箭头         │ 表格框 │          ║  启动画面     ║
文件类型         └──────┘           ╚══════════════╝

← Nerd Fonts 覆盖 →  ←     空白市场      →
```

## 素材类型规划

| 类别 | 示例 | 主要用户 |
|------|------|----------|
| 状态图标 | ✓ ✗ ⟳ spinner | CLI 工具作者 |
| UI 组件 | 边框、进度条、表格 | TUI 应用开发者 |
| 品牌/Logo | ASCII Art Logo、启动画面 | 所有 CLI 产品 |
| 游戏精灵 | 角色、怪物、地图块 | TUI 游戏开发者 |
| 动画特效 | 爆炸、火焰、烟雾（逐帧） | 游戏/视觉应用 |
| 思考/加载动画 | AI 思考指示器、流式输出装饰 | Agent/AI CLI |
| 艺术字体 | 大号 ASCII 字（类似 figlet） | 通用 |

## 目标用户群体

| 群体 | 他们要什么 |
|------|-----------|
| CLI 工具作者 | 状态图标、spinner、品牌 logo 终端版 |
| TUI 应用开发者 | 边框样式、布局组件、装饰元素 |
| TUI 游戏开发者 | 角色精灵、地图块、动画特效 |
| Agent/AI CLI | 思考动画、工具调用指示、流式输出装饰 |

## 核心技术特性

### 1. 终端能力检测 + 自动 Fallback
检测链路: Nerd Fonts → Unicode 扩展 → Box Drawing → 纯 ASCII
程序自动选择当前终端能支持的最佳表现形式。

### 2. 多分辨率素材
同一素材提供不同精细度版本：
- 纯 ASCII（最大兼容性）
- Unicode Box Drawing
- 半角块字符 (▀▄█░▒▓)
- Braille 点阵（最高精细度）

### 3. 颜色适配
- 16 色 (基础 ANSI)
- 256 色
- TrueColor (24-bit)

### 4. 语义化命名
按用途分类，而非按码点：`icon.spinner`, `icon.success`, `icon.folder_open`

### 5. 动画支持
定义帧序列和建议帧率。

### 6. 多语言 SDK
同一套素材定义，生成 Go / Rust / Python / TypeScript 绑定。

### 7. Preview CLI
```bash
tui-art search "download"    # 搜索素材
tui-art preview warrior      # 终端内预览
tui-art info chest_open      # 查看素材详情
```

## 使用体验设想

```python
# Python
from tui_art import load_sprite
player = load_sprite("warrior", style="unicode", colors="256")
chest = load_sprite("chest_open", style="ascii")
```

```go
// Go
import "github.com/cola-runner/tui-art/go"
player := tuiart.Load("warrior", tuiart.Unicode, tuiart.Colors256)
```

```rust
// Rust
use tui_art::load_sprite;
let player = load_sprite("warrior", Style::Unicode, Colors::C256);
```

## 市场分析

### 趋势利好
- CLI 产品数量持续增多
- 现代终端能力增强（TrueColor、图片协议 Kitty/Sixel、GPU 加速）
- 用户审美要求提高（Charm.sh 系列的流行证明了这一点）
- Rogue-like TUI 游戏在 Reddit/HN 上热度持续上涨

### 竞争格局
- **直接竞品：几乎没有**
- 间接参考：Web 游戏素材有 kenney.nl、itch.io、OpenGameArt
- 终端领域完全没有对标产品

### 核心卖点
不是"有哪些图标"，而是"在任何终端都能可靠地显示合适的视觉素材"。

### 主要挑战
- 终端碎片化（iTerm2、Alacritty、Windows Terminal、SSH 环境表现各异）
- 素材格式标准化需要推动社区共识
- TUI 开发者群体相对小众，生态推广需要策略

## 对标项目

| 领域 | 对标 | 我们的差异 |
|------|------|-----------|
| Web 图标 | FontAwesome, Lucide, Heroicons | 我们面向终端，解决 fallback |
| Web 游戏素材 | kenney.nl, OpenGameArt | 我们面向字符终端 |
| 终端字体 | Nerd Fonts | 我们不改字体，运行时解决 |
| TUI 框架 | Charm.sh, Ratatui, Rich | 我们提供素材，不是框架 |

## 下一步

- [ ] 确定素材描述格式标准（JSON/TOML/自定义）
- [ ] 实现终端能力检测模块
- [ ] 制作第一批核心素材（状态图标 + 基础 UI 组件）
- [ ] 搭建 Preview CLI
- [ ] 选择首个 SDK 语言实现
- [ ] 建立素材贡献规范
