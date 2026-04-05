# TUI Art 素材格式规范 v0.1

## 概述

tui-art 使用 **TOML** 作为素材源文件格式，便于人工编辑和社区贡献。编译后生成 **JSON** 索引供 SDK 运行时加载。

设计原则：
- 字形（glyph）与颜色（color）分离
- 同一素材提供多分辨率变体
- 动画 = 帧序列 + 时间间隔
- 语义化命名，按用途分类

## 文件结构

每个素材一个 `.toml` 文件，放在对应分类目录下：

```
assets/
├── icons/
│   ├── status/
│   │   ├── success.toml
│   │   ├── error.toml
│   │   └── warning.toml
│   └── spinners/
│       ├── dots.toml
│       └── line.toml
├── components/
│   ├── borders/
│   └── progress/
├── logos/
├── sprites/
└── animations/
```

## 素材定义格式

### 基础结构

```toml
[meta]
id = "icon.status.success"       # 全局唯一 ID，使用点号分隔的命名空间
name = "Success"                  # 显示名称
description = "成功状态指示图标"    # 描述
category = "icon"                 # 分类: icon | component | logo | sprite | animation | font
tags = ["status", "success", "check"]
author = "tui-art"
license = "MIT"

[size]
width = 1                         # 字符宽度
height = 1                        # 字符高度
```

### 多分辨率变体

每个素材可提供多个渲染精度的变体，运行时根据终端能力自动选择：

```toml
[variants.ascii]
# 纯 ASCII，最大兼容性
content = "+"

[variants.unicode]
# Unicode 字符
content = "✓"

[variants.halfblock]
# 半角块字符组合（适用于较大素材）
content = "✓"

[variants.braille]
# Braille 点阵（最高精细度，适用于较大素材）
content = "✓"
```

Fallback 优先级：`braille` → `halfblock` → `unicode` → `ascii`

### 多行素材

使用 TOML 三引号字符串：

```toml
[variants.ascii]
content = """
+---+
| ? |
+---+"""

[variants.unicode]
content = """
┌───┐
│ ? │
└───┘"""

[variants.halfblock]
content = """
╔═══╗
║ ? ║
╚═══╝"""
```

### 颜色定义

颜色与字形分离，使用颜色映射表：

```toml
[colors.16]
# 16 色 ANSI — 使用颜色标记映射
map = """
.ggg.
g...g
.ggg."""
# 每个字符对应一个颜色
# . = 默认色（不着色）
[colors.16.palette]
g = "green"

[colors.256]
map = """
.ggg.
g...g
.ggg."""
[colors.256.palette]
g = "34"                          # 256 色码

[colors.truecolor]
map = """
.ggg.
g...g
.ggg."""
[colors.truecolor.palette]
g = "#22c55e"                     # Hex 颜色值
```

颜色映射与字形内容逐字符对齐。`.` 或空格表示使用终端默认前景色。

### 动画素材

```toml
[meta]
id = "spinner.dots"
name = "Dots Spinner"
category = "animation"

[animation]
interval_ms = 80                  # 建议帧间隔（毫秒）
loop = true                       # 是否循环

[[animation.frames]]
[animation.frames.variants]
ascii = "."
unicode = "⠋"

[[animation.frames]]
[animation.frames.variants]
ascii = ".."
unicode = "⠙"

[[animation.frames]]
[animation.frames.variants]
ascii = "..."
unicode = "⠹"

# ... 更多帧
```

### 组合素材 (Component)

用于可配置的 UI 组件，如边框：

```toml
[meta]
id = "component.border.rounded"
name = "Rounded Border"
category = "component"

[component]
type = "border"

[component.parts]
top_left = "╭"
top_right = "╮"
bottom_left = "╰"
bottom_right = "╯"
horizontal = "─"
vertical = "│"

[component.variants.ascii.parts]
top_left = "+"
top_right = "+"
bottom_left = "+"
bottom_right = "+"
horizontal = "-"
vertical = "|"
```

## 命名规范

### ID 命名

使用点号分隔的命名空间，全小写，下划线连接多词：

```
{category}.{subcategory}.{name}
```

示例：
- `icon.status.success`
- `icon.spinner.dots`
- `component.border.rounded`
- `component.progress.bar`
- `sprite.character.warrior`
- `animation.effect.explosion`
- `logo.brand.my_app`

### 标签规范

标签全小写，用于搜索和过滤：
- 用途标签：`status`, `navigation`, `loading`, `decoration`
- 风格标签：`minimal`, `retro`, `modern`, `pixel`
- 场景标签：`game`, `cli`, `dashboard`, `agent`

## 编译输出

源 TOML 文件通过构建工具编译为 JSON 索引：

```
dist/
├── index.json              # 完整素材索引（含元数据，不含内容）
├── assets/
│   ├── icon.status.success.json
│   ├── spinner.dots.json
│   └── ...
└── bundles/
    ├── icons.json           # 按分类打包
    ├── spinners.json
    └── components.json
```

这样 SDK 可以按需加载单个素材，也可以加载整个分类包。

## 版本兼容

格式版本号遵循 SemVer。每个素材文件可声明所需的最低格式版本：

```toml
[meta]
format_version = "0.1"
```
