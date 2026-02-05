---
name: converting-markdown
description: Convert Markdown documents to beautiful HTML with multiple themes, responsive design, and print optimization
---

# Converting Markdown to HTML

将 Markdown 文档转换为美观的 HTML，支持多主题切换，适合领导查阅和展示。

## Quick Start

```bash
# 指定文件，使用默认主题（purple）
python3 scripts/convert.py document.md

# 指定文件和主题
python3 scripts/convert.py document.md --theme blue

# 列出所有可用主题
python3 scripts/convert.py --list-themes
```

## Features

- ✅ **多主题支持**：purple（紫色）、blue（蓝色）、green（绿色）、minimal（极简灰度）
- ✅ 响应式设计（PC/平板/手机）
- ✅ 打印优化（自动移除渐变和阴影）
- ✅ **智能段落合并**：使用专业库，无多余`<br>`标签
- ✅ **ASCII图清晰显示**：用等宽字体保留，结构准确
- ✅ 稳定的转换逻辑（Python 脚本，依赖 markdown + PyYAML）

## Available Themes

| Theme | Name | Colors | Use Case |
|-------|------|--------|----------|
| **purple** | 紫色渐变主题 | #667eea → #764ba2 | 售前方案、商务文档 |
| **blue** | 蓝色科技主题 | #1890ff → #096dd9 | 技术文档、API 文档 |
| **green** | 绿色清新主题 | #52c41a → #389e0d | 内部报告、运营数据 |
| **minimal** | 极简灰度主题 | 灰度系 | 学术论文、正式报告 |

## Usage

### Command Line Options

```bash
# 基本用法
python3 scripts/convert.py [markdown_file] [options]

# 选项：
#   --theme, -t    主题名称（默认：purple）
#   --list-themes, -l  列出所有可用主题

# 示例：
python3 scripts/convert.py "文档.md"                    # 默认紫色主题
python3 scripts/convert.py "文档.md" --theme blue       # 蓝色主题
python3 scripts/convert.py "文档.md" --theme green      # 绿色主题
python3 scripts/convert.py "文档.md" --theme minimal    # 极简主题
python3 scripts/convert.py --list-themes               # 列出所有主题
```

### Interactive Mode

脚本为纯命令行工具，不接受交互式输入。所有参数通过命令行参数传入。

## AI 交互流程

当使用本 skill 时，AI Agent 应按以下流程与用户交互：

### ⚠️ AI Agent 执行规范

**执行脚本时的重要规则：**

1. **使用完整路径调用脚本**：确保脚本能被找到
2. **使用完整路径指定输入文件**：避免文件找不到
3. **不要 cd 切换目录**：保持当前工作目录不变
4. **明确输出位置**：告知用户 HTML 文件的生成位置

**❌ 错误示例：**
```bash
# 错误1：切换目录（会改变工作目录）
cd /path/to/skill && python3 scripts/convert.py document.md

# 错误2：使用相对路径（可能找不到文件）
python3 scripts/convert.py ../../document.md
```

**✅ 正确示例：**
```bash
# 方法1：使用绝对路径（推荐）
python3 /path/to/skill/scripts/convert.py /path/to/document.md --theme blue

# 方法2：先 cd 到项目目录，再执行
cd /path/to/project
python3 /path/to/skill/scripts/convert.py document.md --theme blue
```

**执行后告知用户：**
```
✅ 转换完成！
📄 输入文件：/path/to/document.md
📄 输出文件：/path/to/document.html
📊 文件大小：XX KB
💡 提示：HTML 文件与 Markdown 文件在同一目录
```

### 步骤1：选择 Markdown 文件

如果用户未指定文件，使用 `AskUserQuestion` 工具让用户选择。

### 步骤2：选择主题模板

**⚠️ 优先级：这是第2步，必须在询问ASCII图处理之前完成。**

使用 `AskUserQuestion` 工具展示主题选项：
- **purple** - 紫色渐变（售前方案、商务文档）
- **blue** - 蓝色科技（技术文档、API文档）
- **green** - 绿色清新（内部报告、运营数据）
- **minimal** - 极简灰度（学术论文、正式报告）

**重要：主题选择会影响后续图形的颜色，必须先确定主题。**

### 步骤3：询问 ASCII 图处理方式

**⚠️ 重要：必须先完成步骤2（选择主题），再执行此步骤。**

**检测文档是否包含ASCII图**（识别 ` ```ascii:类型 ` 代码块）

支持5种图形类型：
- `architecture` - 系统架构图
- `flowchart` - 流程图
- `ui` - UI界面图
- `timeline` - 时间线图
- `diagram` - 通用图

**统计各类型数量：**
```python
diagrams = {
    'architecture': 3,  # 找到3个架构图
    'flowchart': 2,     # 找到2个流程图
    'ui': 4,            # 找到4个UI图
    'timeline': 1,       # 找到1个时间线
}
```

如果包含ASCII图，询问用户：
- **保留原样** - 用等宽字体显示，快速稳定
- **智能转换 SVG** - 根据类型生成精美矢量图形

**选择1（保留原样）：**
- 直接调用 `python3 scripts/convert.py [file] --theme [theme]`
- ASCII图用等宽字体清晰显示
- 适合快速预览、不需要美化的场景

**选择2（智能转换 SVG）：**

⚠️ **重要**：完整的智能转换需要3个步骤（脚本化流程）

**步骤1：生成带占位符的HTML**
```bash
AI_SVG_CONVERSION=true python3 scripts/convert.py [file] --theme [theme]
```

脚本输出：
```
✅ AI占位符已生成
```

**步骤2：提取占位符到JSON**
```bash
python3 scripts/extract_placeholders.py [file.html]
```

生成JSON文件：
```json
{
  "total": 8,
  "placeholders": [
    {
      "id": 1,
      "type": "architecture",
      "raw_content": "┌────────┐\n│ 系统  │...",
      "svg_code": null  ← AI Agent填充这个字段
    }
  ]
}
```

**步骤3：AI Agent生成SVG并替换**

AI Agent需要：
1. **读取JSON文件**，获取所有占位符的`raw_content`
2. **智能理解结构**，为每个占位符生成`svg_code`
3. **保存JSON文件**
4. **调用替换脚本**：
   ```bash
   python3 scripts/replace_svg.py [file.json]
   ```

**输出结果**：生成包含精美SVG图形的最终HTML文件


**📖 参考文档：**
- 📄 输出格式和代码要求：见 `guides/output-specs.md`
- 🎨 ASCII识别和转换技巧：见 `guides/ascii-to-svg.md`
**职责分工：**
- **脚本负责**（机械工作）：提取、占位符替换、文件读写
- **AI Agent负责**（智能工作）：理解结构、生成SVG代码

**优点**：
- ✅ 稳定可靠：脚本处理文件操作，不会出错
- ✅ 可追溯：JSON保存中间结果
- ✅ 可验证：每步都有明确输出
- ✅ 职责分离清晰

适合演示、展示、汇报等需要美观图形的场景。


### 步骤4：验证转换结果

**⚠️ 重要：AI Agent 自行验证格式**

replace_svg.py 脚本**不验证**SVG/HTML格式，只负责替换。格式验证由 AI Agent 在生成代码时自行负责。

**AI Agent 验证清单：**

生成代码时检查：
1. ✅ SVG 以 `<svg` 开头，`</svg>` 结尾
2. ✅ HTML 使用语义化标签（`<div>`, `<button>` 等）
3. ✅ 使用主题色系（blue: #1890ff, purple: #667eea 等）
4. ✅ 包含必要属性（viewBox、xmlns 等）
5. ✅ 没有明显的语法错误

替换后检查：
```bash
# 检查是否还有未替换的占位符
grep -c "AI-SVG-PLACEHOLDER" output.html
# 输出应该为 0

# 统计SVG和HTML数量
echo "SVG: $(grep -c '<svg' output.html)"
echo "HTML界面: $(grep -c '<div style=\"font-family' output.html)"
```

**使用Read工具查看效果：**
- 读取生成的 HTML 文件
- 检查 SVG/HTML 是否正确渲染
- 如果发现问题，重新生成并替换

**输出结果**：
- 选择1：HTML文件（ASCII图用等宽字体）
- 选择2：HTML文件（ASCII图转换为精美图形）

## Adding Custom Themes

要添加新主题，只需在 `templates/` 目录创建新的 YAML 文件：

1. 复制现有主题文件作为模板：
   ```bash
   cp templates/purple.yaml templates/mytheme.yaml
   ```

2. 编辑 `mytheme.yaml`，修改颜色和样式配置

3. 立即使用：
   ```bash
   python3 scripts/convert.py document.md --theme mytheme
   ```

### Theme Configuration Format

每个主题 YAML 文件包含以下部分：

- **colors**: 颜色配置（主色、辅助色、背景等）
- **styles**: 样式配置（圆角、阴影、间距）
- **font_sizes**: 字体大小配置
- **spacing**: 间距配置
- **gradients**: 渐变定义
- **special_styles**: 特殊元素样式（表格、代码、引用）

## Output

- **File**: 与输入文件同目录，扩展名改为 `.html`
  - 例如：输入 `/path/to/document.md` → 输出 `/path/to/document.html`
  - ⚠️ **注意**：HTML 文件生成在 Markdown 文件所在目录，不是在 SKILL 或脚本目录
- **Encoding**: UTF-8
- **Size**: 通常 50-100 KB
- **Style**: 根据选择的主题应用不同样式

**AI Agent 执行注意事项：**
- ⚠️ **不要使用 cd 切换目录**
- ⚠️ 使用完整路径（绝对路径或从当前工作目录的相对路径）
- ✅ 执行后明确告知输出文件的完整路径

## Technical Details

- **Language**: Python 3.6+（使用 f-string 语法）
- **Dependencies**:
  - **必需**: PyYAML（配置文件解析）
  - **必需**: markdown（Markdown 转 HTML）
- **File encoding**: UTF-8
- **Input formats**: Markdown (.md)
- **Output format**: HTML5

### 安装依赖

```bash
# 安装必需依赖
pip3 install pyyaml markdown
```

**注意**: 本 SKILL 由 AI Agent 调用，Agent 应使用 `AskUserQuestion` 工具与用户交互，收集参数后调用脚本。

## Architecture

```
converting-markdown/
├── SKILL.md              # 本文档
├── LICENSE.txt           # MIT 许可证
├── guides/               # 技术指南目录
│   ├── output-specs.md   # 输出格式规范
│   └── ascii-to-svg.md   # ASCII图转换技巧
├── templates/            # 主题配置目录
│   ├── purple.yaml       # 紫色渐变主题
│   ├── blue.yaml         # 蓝色科技主题
│   ├── green.yaml        # 绿色清新主题
│   └── minimal.yaml      # 极简灰度主题
└── scripts/
    ├── convert.py        # 主转换脚本（支持 --theme 参数）
    ├── themes.py         # 主题加载工具
    ├── extract_placeholders.py  # 提取占位符到JSON
    └── replace_svg.py    # 替换占位符为SVG/HTML
```

## Examples

```bash
# 转换售前方案（使用默认紫色主题）
python3 scripts/convert.py "售前/官网及业务系统升级方案.md"

# 转换技术文档（使用蓝色主题）
python3 scripts/convert.py "技术文档.md" --theme blue

# 转换内部报告（使用绿色主题）
python3 scripts/convert.py "运营报告.md" --theme green

# 转换学术论文（使用极简主题）
python3 scripts/convert.py "论文.md" --theme minimal
```

## Notes

- 必须使用 `python3`（不是 `python`）因为使用了 f-string 语法
- Markdown 中已有的 SVG 图表会被原样保留
- 表格会自动应用主题的渐变表头
- 引用框会应用主题的半透明背景
- 链接样式根据主题变化
