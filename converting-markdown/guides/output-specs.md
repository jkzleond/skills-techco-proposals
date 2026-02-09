# 输出规范

本文档说明 AI Agent 如何为 ASCII 图生成代码。

## 概述

当用户选择"智能转换"时，AI Agent 需要将 ASCII 图转换为代码：

| 图形类型 | 输出格式 | 说明 |
|---------|---------|------|
| `architecture` | SVG | 系统架构图，使用方框、箭头、层级 |
| `flowchart` | SVG | 流程图，使用步骤框、连接线 |
| `ui` | **HTML/CSS** | UI界面图，生成真实可交互界面 |
| `timeline` | SVG | 时间线图，使用时间轴、节点 |
| `diagram` | SVG | 通用图，根据内容灵活处理 |

**⚠️ 重要：UI 类型输出 HTML，不是 SVG！**

## 输出要求

### 1. SVG 输出要求（architecture/flowchart/timeline/diagram）

#### 1.1 基本结构

```xml
<svg width="100%" style="max-width: 800px" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
  <!-- SVG内容 -->
</svg>
```

**必须包含：**
- `width="100%"` - 响应式宽度
- `style="max-width: 800px"` - 最大宽度（根据内容调整）
- `viewBox` - 视口，确保缩放不失真
- `xmlns` - SVG命名空间

#### 1.2 使用主题色系

**紫色主题（purple）：**
```python
primary = "#667eea"
secondary = "#764ba2"
```

**蓝色主题（blue）：**
```python
primary = "#1890ff"
secondary = "#096dd9"
```

**绿色主题（green）：**
```python
primary = "#52c41a"
secondary = "#389e0d"
```

**极简主题（minimal）：**
```python
primary = "#333333"
secondary = "#666666"
```

#### 1.3 添加渐变和阴影

```xml
<defs>
  <!-- 渐变 -->
  <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" style="stop-color:{primary};stop-opacity:1" />
    <stop offset="100%" style="stop-color:{secondary};stop-opacity:1" />
  </linearGradient>

  <!-- 阴影 -->
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
    <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.1"/>
  </filter>

  <!-- 箭头标记 -->
  <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
    <polygon points="0 0, 10 3, 0 6" fill="{secondary}" />
  </marker>
</defs>
```

#### 1.4 使用矢量元素

**方框：**
```xml
<rect x="50" y="50" width="200" height="100"
      fill="white" stroke="{primary}" stroke-width="2" rx="8"
      filter="url(#shadow)"/>
```

**文本：**
```xml
<text x="150" y="100" text-anchor="middle"
      font-family="-apple-system, BlinkMacSystemFont, sans-serif"
      font-size="16" font-weight="600" fill="#333">
  文本内容
</text>
```

**连接线：**
```xml
<line x1="250" y1="100" x2="350" y2="100"
      stroke="{secondary}" stroke-width="2" marker-end="url(#arrowhead)"/>
```

#### 1.5 美化效果

- 圆角：`rx="8"`（方框）
- 阴影：`filter="url(#shadow)"`
- 渐变：`fill="url(#grad1)"`
- 粗细：`stroke-width="2"`（主线条）

### 2. HTML 输出要求（ui 类型）

> **适用范围：** 本章节所有要求仅针对 **AI Agent 将 `ui` 类型 ASCII 图转换为 HTML 代码**时适用。

#### 2.0 核心原则：静态展示，非交互组件 ⚠️

**重要约束：**

❌ **错误：生成可交互组件**
```html
<!-- 错误：使用 JavaScript 实现弹窗 -->
<button onclick="document.getElementById('modal').style.display='block'">打开</button>
<div id="modal" style="display:none;">弹窗内容</div>

<!-- 错误：使用 CSS 实现悬停弹窗 -->
<div class="popup">悬停显示</div>
<style>
  .popup:hover .content { display: block; }
</style>
```

✅ **正确：生成静态展示代码**
```html
<!-- 正确：直接显示在文档中 -->
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            padding: 24px;
            max-width: 400px;">
  <h3>弹窗标题</h3>
  <p>弹窗内容</p>
  <button>确定</button>
</div>
```

**关键区别：**
| 特征 | 静态展示（✅ 正确） | 可交互组件（❌ 错误） |
|------|------------------|-------------------|
| **显示方式** | 直接显示在文档中 | 需要用户交互才显示 |
| **JavaScript** | 不使用 | 使用 onclick 等事件 |
| **CSS** | 仅用于样式美化 | 用于显示/隐藏控制 |
| **用途** | 文档展示 | 实际功能实现 |

**为什么必须静态？**
- 📄 HTML 文档用于**展示和演示**，不是功能应用
- 👥 领导/客户查看文档时，希望**直接看到所有内容**
- 🖨️ 静态代码支持**打印和导出 PDF**
- 🔒 避免复杂的 JavaScript 导致兼容性问题

#### 2.0.1 ⚠️ 必须生成 HTML 片段，不是完整文档

**适用范围：** 本章节的所有约束仅针对 **AI Agent 将 ASCII 图转换为 HTML 代码**时适用。

> **重要说明：**
> - converting-markdown 的最终输出是完整的 HTML 文档（包含 `<html>`, `<head>`, `<body>` 等）
> - 这些约束只适用于 AI 生成的、用来替换 ASCII 图的 **HTML 片段**
> - AI 生成的代码会被插入到完整 HTML 文档的 `<body>` 内部

**关键规范：** AI 生成的 HTML 代码必须是**HTML 片段（HTML fragment）**，不能是完整的 HTML 文档。

**❌ 禁止包含的标签：**
```html
<!DOCTYPE html>
<html>
<head>
  <title>...</title>
</head>
<body>
  <!-- 内容 -->
</body>
</html>
```

**✅ 正确的 HTML 片段：**
```html
<!-- 只包含实际的 UI 组件代码 -->
<div style="background: linear-gradient(135deg, {primary} 0%, {secondary} 100%);
            border-radius: 12px;
            padding: 24px;">
  <h3 style="color: white; margin-bottom: 12px;">标题</h3>
  <p style="color: rgba(255,255,255,0.9);">内容描述</p>
  <button style="padding: 10px 20px; background: white; color: {primary}; border: none; border-radius: 8px; font-weight: 600;">
    按钮
  </button>
</div>
```

**为什么不能生成完整文档？**
1. **避免标签嵌套**：生成的代码会被插入到已有的 HTML 文档中，如果包含 `<html>`、`<body>` 等标签，会导致标签嵌套错误
2. **保持结构正确**：最终文档只能有一套 `<html>` 和 `<body>` 标签
3. **避免样式冲突**：`<head>` 中的样式会影响整个文档
4. **确保功能正常**：嵌套的文档结构会导致 JavaScript 和 CSS 选择器失效

**允许的标签：**
- ✅ 语义化容器：`<div>`, `<section>`, `<article>`, `<header>`, `<footer>`
- ✅ 文本标签：`<h1>`~`<h6>`, `<p>`, `<span>`, `<strong>`, `<em>`
- ✅ 列表：`<ul>`, `<ol>`, `<li>`
- ✅ 表单元素：`<button>`, `<input>`, `<textarea>`, `<select>`
- ✅ 表格：`<table>`, `<tr>`, `<td>`, `<th>`
- ✅ 其他内联或块级元素

**禁止的标签：**
- ❌ `<!DOCTYPE html>`
- ❌ `<html>`, `</html>`
- ❌ `<head>`, `</head>`
- ❌ `<body>`, `</body>`
- ❌ `<title>`, `</title>`
- ❌ `<meta>`, `<link>`
- ❌ `<script>`, `<script src="...">`（禁止所有 script 标签）

**样式规范：**
- ✅ **允许内联 style 属性**：`<div style="...">`
- ✅ **允许 `<style>` 标签**：用于定义 class 样式、hover/focus 效果
- ❌ **禁止 `<script>` 标签**：包括内联脚本和外部脚本引用
- ❌ **禁止事件处理属性**：`onclick`、`onhover`、`onload` 等

**为什么禁止 script？**
1. 📄 文档用于**展示和演示**，不是功能应用
2. 👥 领导/客户查看时，希望**直接看到所有内容**
3. 🖨️ 支持**打印和导出 PDF**
4. 🔒 避免 JavaScript 导致的兼容性问题

**验证方法：**
生成的 HTML 代码应该能够直接插入到 `<body>` 标签内部，而不需要任何修改。

#### 2.1 使用语义化标签

```html
<!-- 卡片容器 -->
<div style="background: linear-gradient(135deg, {primary} 0%, {secondary} 100%);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            max-width: 400px;">

  <!-- 标题 -->
  <div style="color: white; font-size: 18px; font-weight: 600;">
    标题内容
  </div>

  <!-- 按钮 -->
  <button style="padding: 10px 20px;
                  background: white;
                  color: {primary};
                  border: none;
                  border-radius: 8px;
                  font-weight: 600;
                  cursor: pointer;
                  transition: all 0.2s;">
    按钮文字
  </button>
</div>
```

#### 2.2 使用主题色系

与 SVG 相同的色系（从转换时选择的主题获取）。

#### 2.3 响应式布局

```html
<!-- Flexbox布局 -->
<div style="display: flex; gap: 12px;">
  <div>项目1</div>
  <div>项目2</div>
</div>

<!-- Grid布局 -->
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
  <div>项目1</div>
  <div>项目2</div>
</div>
```

#### 2.4 交互效果

```css
/* Hover效果 */
<button style="transition: all 0.2s;">
button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
}

/* 焦点效果 */
button:focus {
  outline: 2px solid {primary};
  outline-offset: 2px;
}
```

#### 2.5 Class 命名隔离（必须遵守）⚠️

**问题：** 生成的 HTML 中的 class 会与主 HTML 文档的 class 冲突，导致样式错乱。

**解决方案：** 所有 class 必须加前缀，格式为：`[示意图类型]-[占位符ID]-`

**前缀规则：**

| 示意图类型 | 前缀示例 | 说明 |
|-----------|---------|------|
| `ui` | `ui-1-` | 第1个 UI 占位符 |
| `ui` | `ui-2-` | 第2个 UI 占位符 |
| `architecture` | `architecture-3-` | 第3个架构占位符（如需HTML） |

**错误示例（❌ 无前缀）：**

```html
<!-- ❌ 错误：class 无前缀，会与主文档冲突 -->
<div class="container">
  <button class="btn-primary">按钮</button>
</div>

<style>
.container { background: #f5f5f5; }
.btn-primary { background: #1890ff; }
</style>
```

**正确示例（✅ 有前缀）：**

```html
<!-- ✅ 正确：class 有前缀，完全隔离 -->
<div class="ui-1-container">
  <button class="ui-1-btn-primary">按钮</button>
</div>

<style>
.ui-1-container { background: #f5f5f5; }
.ui-1-btn-primary { background: #1890ff; }
</style>
```

**完整示例（包含 hover 效果）：**

```html
<!-- 假设这是 ui 类型的第 2 个占位符 -->
<div class="ui-2-card" style="display: flex; gap: 12px; padding: 20px;
                      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                      border-radius: 12px; max-width: 400px;">
  <div class="ui-2-title" style="color: white; font-size: 18px;">标题</div>
  <button class="ui-2-button">按钮</button>
</div>

<style>
.ui-2-button {
  padding: 10px 20px;
  background: white;
  color: #667eea;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.ui-2-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
}

.ui-2-button:focus {
  outline: 2px solid #667eea;
  outline-offset: 2px;
}
</style>
```

**验证清单：**
- [ ] 所有 class 都有前缀（`[类型]-[ID]-`）
- [ ] CSS 选择器都使用带前缀的 class
- [ ] 没有使用通配符选择器（如 `button { ... }`）
- [ ] 没有使用元素选择器（如 `div { ... }`）

## AI Agent 并行生成流程

当用户选择"智能转换"时，AI Agent 应该使用 Task 工具实现并行生成。

### 为什么一个 Task 处理一个占位符最好？

| 优势 | 说明 |
|------|------|
| **类型精准** | AI 可以为每种类型（architecture/flowchart/ui）生成专属的任务说明 |
| **效率更高** | 不同类型的示意图个数分布不均，灵活调度 |
| **容错性强** | 一个 Task 失败不影响其他 Task |

### 为什么必须用多 Task？

| 方式 | 耗时（8个图） | 说明 |
|------|----------|------|
| **顺序处理** | ~80秒 | AI 一个接一个生成 |
| **多 Task 并行** | ~10-15秒 | 8 个 Task 同时工作 |
| **加速比** | **5-8倍** | - |

### 生成流程

**步骤1：读取 extracted.json**
- 获取所有占位符信息（id, type, raw_content）
- 获取缓存目录路径

**步骤2：为每个占位符创建一个 Task**
- 使用 Task 工具，每个 Task 处理一个占位符
- 所有 Task 并行执行
- 每个 Task 生成对应的 SVG/HTML 文件

**步骤3：调用替换脚本**
- 等待所有 Task 完成
- 调用 `python3 scripts/replace_svg.py [extracted.json]`

### 质量要求（每个 Task 都必须满足）

| 检查项 | 要求 |
|--------|------|
| **圆角** | 方框必须有 `rx="8"` 或类似属性 |
| **主题色** | 必须使用 primary/secondary 颜色 |
| **字体** | 文本必须有 `font-family` 属性 |
| **viewBox** | SVG 必须使用 `viewBox`（非硬编码尺寸） |
| **代码长度** | SVG > 500 字符，HTML > 400 字符 |
| **结构** | 理解 ASCII 图结构，不是机械包装 |
| **无 ASCII** | 不能包含 `┌─┐` 等 ASCII 字符 |
| **HTML class** | HTML 类型必须有前缀：`[类型]-[ID]-` |

### ⚠️ 重要说明

**如果 AI 平台支持 Task 工具：**
- ✅ 必须使用 Task 工具，每个 Task 处理一个占位符
- ✅ 不要自己顺序处理所有占位符
- ✅ 不要一个 Task 处理多个占位符（效率低）

**如果 AI 平台不支持 Task 工具：**
- 顺序处理也可以，但每个图的质量必须完整
- 不能为了速度降低质量
        ext = "svg"
    elif diagram_type == "flowchart":
        svg_code = generate_flowchart_svg(raw_content)     # AI 生成
        ext = "svg"
    elif diagram_type == "ui":
        html_code = generate_ui_html(raw_content)         # AI 生成
        ext = "html"
    # ... 其他类型

    # 保存到独立文件（支持并行写入）
    output_file = cache_dir / f"{placeholder_id}.{ext}"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(svg_code if ext == "svg" else html_code)
```

**文件命名规则：**
- `{id}.svg` - architecture, flowchart, timeline, diagram 类型
- `{id}.html` - ui 类型

**示例文件结构：**
```
.cvt-caches/test/3140cf/
├── extracted.json   # 占位符映射
├── 1.svg           # AI 生成的架构图
├── 2.html          # AI 生成的 UI 界面
└── 3.svg           # AI 生成的流程图
```

### 步骤3：调用替换脚本

```bash
# 所有文件生成完成后，调用替换脚本
python3 scripts/replace_svg.py .cvt-caches/test/3140cf/extracted.json
```

**脚本会：**
1. 从缓存目录读取所有 `{id}.svg` 和 `{id}.html` 文件
2. 基于 `id` 精确匹配并替换 HTML 中的占位符
3. 自动清理缓存目录

### 并行优势

| 方案 | 8个图生成时间 | 说明 |
|------|--------------|------|
| **旧方案**（写回 JSON） | 80-100 秒 | 顺序生成，单一写入点 |
| **新方案**（文件系统） | 18-25 秒 | 并行生成，独立文件 |
| **加速比** | **4-5倍** | - |

### 职责分工

**脚本负责（机械工作）：**
- ✅ 提取占位符到 JSON
- ✅ 从缓存目录读取生成的文件
- ✅ 基于 ID 精确匹配和替换
- ✅ 自动清理缓存目录

**AI Agent 负责（智能工作）：**
- ✅ 理解 ASCII 图结构
- ✅ 生成 SVG/HTML 代码
- ✅ 并行写入独立文件
- ✅ 验证代码格式正确性

### 关键要点

1. **基于 ID 唯一匹配**：不依赖数组顺序，通过 `id` 字段精确匹配
2. **支持真正的并行**：每个占位符独立文件，无写入冲突
3. **自动清理**：转换完成后删除整个 `{session_id}` 目录
4. **容错性强**：部分失败不影响其他占位符

## 生成示例

### 示例1：架构图（architecture）

**输入（ASCII）：**
```
┌────────┐   →   ┌────────┐
│  系统A │       │  系统B │
└────────┘       └────────┘
```

**输出（SVG）：**
```xml
<svg width="100%" style="max-width: 400px" viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1890ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#096dd9;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.1"/>
    </filter>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#096dd9"/>
    </marker>
  </defs>

  <!-- 系统A -->
  <rect x="20" y="20" width="120" height="60" fill="white" stroke="#1890ff" stroke-width="2" rx="8" filter="url(#shadow)"/>
  <text x="80" y="55" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#333">系统A</text>

  <!-- 连接线 -->
  <line x1="140" y1="50" x2="260" y2="50" stroke="#096dd9" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- 系统B -->
  <rect x="260" y="20" width="120" height="60" fill="white" stroke="#1890ff" stroke-width="2" rx="8" filter="url(#shadow)"/>
  <text x="320" y="55" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#333">系统B</text>
</svg>
```

### 示例2：UI界面（ui）

**输入（ASCII）：**
```
┌──────────────────────────┐
│     我的积分              │
│      1,000 积分          │
│  [去兑换]  [查看明细]     │
└──────────────────────────┘
```

**输出（HTML）：**
```html
<div style="background: linear-gradient(135deg, #1890ff 0%, #096dd9 100%);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 12px rgba(24, 144, 255, 0.3);
            max-width: 400px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">

  <div style="color: white; font-size: 18px; font-weight: 600; margin-bottom: 12px;">
    我的积分
  </div>

  <div style="color: white; font-size: 32px; font-weight: 700; margin-bottom: 20px;">
    1,000 积分
  </div>

  <div style="display: flex; gap: 12px;">
    <button style="flex: 1;
                    padding: 10px 20px;
                    background: white;
                    color: #1890ff;
                    border: none;
                    border-radius: 8px;
                    font-weight: 600;
                    cursor: pointer;
                    transition: all 0.2s;">
      去兑换
    </button>
    <button style="flex: 1;
                    padding: 10px 20px;
                    background: rgba(255, 255, 255, 0.2);
                    color: white;
                    border: 1px solid rgba(255, 255, 255, 0.3);
                    border-radius: 8px;
                    font-weight: 600;
                    cursor: pointer;
                    transition: all 0.2s;">
      查看明细
    </button>
  </div>
</div>
```

## 验证规则

AI Agent 在生成代码后必须验证以下内容：

### SVG 验证清单（7 条）

1. ✅ 以 `<svg` 开头，`</svg>` 结尾
2. ✅ 包含 `xmlns="http://www.w3.org/2000/svg"`
3. ✅ 有 `viewBox` 属性（不要用硬编码的 width/height）
4. ✅ 使用主题色系（见 SKILL.md "配色速查表"）
5. ✅ 所有文本元素都有 `font-family` 属性
6. ✅ 方框有圆角（`rx="8"` 或类似属性）
7. ✅ 所有标签正确闭合

### HTML 验证清单（10 条）

1. ✅ 使用语义化 HTML5 标签（`<div>`, `<button>`, `<input>` 等）
2. ✅ 所有样式用内联 `style` 属性或 `<style>` 标签
3. ✅ **所有 class 有前缀：`[类型]-[ID]-`** ⚠️
4. ✅ **静态展示：不使用 JavaScript 控制显示/隐藏** ⚠️
5. ✅ **内容直接可见：无需用户交互（点击/悬停）** ⚠️
6. ✅ 使用 flexbox 或 grid 布局（不要用 float）
7. ✅ 响应式设计（`max-width`、必要时用 `@media`）
8. ✅ 可访问性（input 有 label，适当的地方有 alt）
9. ✅ 主题色应用一致
10. ✅ 标签正确闭合

**⚠️ 特别注意（第3-5条）：**
- ❌ 不使用 `onclick`、`onhover` 等事件处理
- ❌ 不使用 `display: none` 等隐藏内容的 CSS
- ❌ 不使用 JavaScript 控制显示状态
- ❌ **所有 class 必须加前缀（如 `ui-1-container`），避免与主文档冲突**
- ✅ 所有内容应该直接显示在文档中
- ✅ 目标是展示设计效果，不是实现功能

### 输出文件验证（5 条）

1. ✅ 没有残留的 `AI-SVG-PLACEHOLDER` 标记
2. ✅ 文件大小合理（典型文档 <500 KB）
3. ✅ UTF-8 编码
4. ✅ 在浏览器中能正确打开
5. ✅ **所有图形质量一致** ⚠️

**⚠️ 质量一致性检查（必须全部满足）：**
- 所有 SVG 都使用 `viewBox`（响应式）
- 所有 SVG 都使用主题色系
- 所有方框都有圆角（`rx` 属性）
- 所有文本都有 `font-family` 属性
- 没有"简略版"或"低质量"的图形
- 每个 SVG 代码长度 > 500 字符（包含完整结构）

**质量一致性标准：**

| 图形 | viewBox | 圆角 | 主题色 | 字体 | class前缀 | 最小长度 |
|------|--------|------|--------|------|-----------|----------|
| **SVG（每个都必须）** | ✅ | ✅ | ✅ | ✅ | - | > 500字符 |
| **HTML（每个都必须）** | - | ✅ | ✅ | - | ✅ | > 400字符 |

**如果有任何一个图形不达标：**
- ❌ 整个转换失败
- ❌ 必须重新生成不达标的图形
- ✅ 不能为了速度降低质量

## 常见错误预防

### 错误 1：硬编码尺寸

❌ **错误：**
```xml
<svg width="800px" height="400px">
  <!-- 内容 -->
</svg>
```
**问题**：不响应式，小屏幕会溢出

✅ **正确：**
```xml
<svg width="100%" style="max-width: 800px" viewBox="0 0 800 400">
  <!-- 内容 -->
</svg>
```

### 错误 2：缺少命名空间

❌ **错误：**
```xml
<svg>
  <!-- 内容 -->
</svg>
```
**问题**：某些浏览器无法正确渲染

✅ **正确：**
```xml
<svg xmlns="http://www.w3.org/2000/svg">
  <!-- 内容 -->
</svg>
```

### 错误 3：UI 界面图使用 SVG

❌ **错误：**
```xml
<svg>
  <rect>按钮</rect>
</svg>
```
**问题**：UI 界面图应该用 HTML 实现交互性

✅ **正确：**
```html
<div style="background: var(--primary); border: 2px solid var(--secondary);">
  <button>按钮</button>
</div>
```

### 错误 4：忘记使用主题颜色

❌ **错误：**
```xml
<rect fill="#667eea" />  <!-- 只适用于紫色主题 -->
```
**问题**：用户选择其他主题时会出错

✅ **正确：**
```xml
<rect fill="var(--primary)" stroke="var(--border)" />
```
**说明**：使用 CSS 变量，自动适配任何主题

### 错误 5：文本缺少字体设置

❌ **错误：**
```xml
<text>文本内容</text>
```
**问题**：使用默认衬线字体，不专业

✅ **正确：**
```xml
<text font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif">
  文本内容
</text>
```

### 错误 6：机械转换（只包在 SVG 里）

❌ **错误：**
```xml
<!-- 错误：只是把 ASCII 包在 SVG 里 -->
<svg>
  <text>┌────────┐</text>
  <text>│  标题  │</text>
  <text>└────────┘</text>
</svg>
```
**问题**：没有理解结构，只是机械包装

✅ **正确：**
```xml
<!-- 正确：理解结构，用矢量元素重绘 -->
<svg>
  <rect x="20" y="20" width="120" height="60" fill="white" stroke="var(--primary)" rx="8"/>
  <text x="80" y="55" text-anchor="middle" font-family="sans-serif">标题</text>
</svg>
```

### 错误 7：缺少美化效果

❌ **错误：**
```xml
<rect x="20" y="20" width="120" height="60" fill="white" stroke="#333"/>
```
**问题**：缺少圆角、阴影、渐变，不美观

✅ **正确：**
```xml
<defs>
  <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" style="stop-color:var(--primary);stop-opacity:1" />
    <stop offset="100%" style="stop-color:var(--secondary);stop-opacity:1" />
  </linearGradient>
  <filter id="shadow">
    <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.1"/>
  </filter>
</defs>

<rect x="20" y="20" width="120" height="60"
      fill="url(#grad1)" stroke="var(--primary)" stroke-width="2" rx="8"
      filter="url(#shadow)"/>
```

### 错误 8：UI 图做成可交互组件 ⚠️ 常见错误

❌ **错误：生成可交互弹窗**
```html
<!-- 错误：需要点击才能看到内容 -->
<button onclick="toggleModal()">查看详情</button>

<div id="modal" style="display: none; position: fixed; top: 50%; left: 50%;">
  <div>弹窗内容</div>
</div>

<script>
function toggleModal() {
  document.getElementById('modal').style.display = 'block';
}
</script>
```
**问题**：
- ❌ 使用 JavaScript 控制显示/隐藏
- ❌ 需要用户交互才能看到内容
- ❌ 不适合文档展示和打印
- ❌ 兼容性差

❌ **错误：使用 CSS 实现悬停弹窗**
```html
<!-- 错误：悬停才显示内容 -->
<div class="popup-container">
  <button>悬停查看</button>
  <div class="popup-content" style="display: none;">
    弹窗内容
  </div>
</div>

<style>
.popup-container:hover .popup-content {
  display: block;
  position: absolute;
  top: 100%;
}
</style>
```
**问题**：
- ❌ 使用 CSS 控制显示/隐藏
- ❌ 需要悬停才能看到内容
- ❌ 打印时可能只显示触发元素

✅ **正确：生成静态展示代码**
```html
<!-- 正确：直接显示所有内容 -->
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            position: relative;">
  <!-- 直接显示弹窗内容，无需交互 -->
  <div style="color: white; font-size: 18px; font-weight: 600;">
    详情标题
  </div>
  <div style="color: white; margin-top: 12px;">
    弹窗内容直接显示在这里...
  </div>
  <button style="margin-top: 16px; padding: 8px 16px;">关闭</button>
</div>
```
**优点**：
- ✅ 内容直接可见，无需交互
- ✅ 适合文档展示和打印
- ✅ 纯 HTML/CSS，无 JavaScript
- ✅ 兼容性好

**关键区别：**
| 特征 | 可交互弹窗（❌） | 静态展示（✅） |
|------|----------------|--------------|
| **显示方式** | 需要点击/悬停 | 直接显示 |
| **JavaScript** | 使用 onclick 等事件 | 不使用 |
| **适用场景** | Web 应用 | 文档展示 |
| **打印支持** | 差 | 好 |
| **目的** | 实现功能 | 展示设计 |

**原则：**
> **UI 类型的 ASCII 图应该生成"看起来像"真实界面的静态展示代码，而不是真正可交互的组件。**
>
> 目标是让读者**看到设计效果**，而不是提供实际功能。

### 错误 9：顺序处理而非多 Task 并行 ⚠️ 常见错误

❌ **错误：AI Agent 自己顺序生成所有图**
- AI 逐个处理占位符
- 一个接一个生成，总耗时 = 每个图耗时 × 图数量
- 8个图 × 10秒 = 80秒

**问题：**
- ❌ 没有利用 Task 工具的并行能力
- ❌ 速度慢，效率低

✅ **正确：使用 Task 工具，每个 Task 处理一个占位符**
- 为每个占位符创建一个独立的 Task
- 所有 Task 并行执行
- 8个 Task 同时工作 ≈ 10-15秒（5-8倍加速）

**关键区别：**
| 特征 | 顺序处理 | 多 Task 并行 |
|------|----------|-------------|
| **执行方式** | AI 逐个生成 | 每个 Task 处理一个占位符 |
| **总耗时（8图）** | ~80秒 | ~10-15秒 |
| **加速比** | 1x | 5-8x |
| **类型精准度** | 混合处理 | 每种类型独立处理 |

**⚠️ 重要：**
> **如果 AI 平台支持 Task 工具，必须为每个占位符创建一个 Task，不能顺序处理，也不能一个 Task 处理多个。**
>
> **每个 Task 生成的图形质量必须完整，不能为了 Task 数量多而降低标准。**

### 错误 10：为了速度降低质量 ⚠️ 常见错误

❌ **错误：生成简略版本**
```xml
<!-- 错误：简略版本，缺少美化 -->
<svg width="400" height="100">
  <rect x="20" y="20" width="120" height="60" fill="#fff" stroke="#333"/>
  <text x="80" y="55">系统A</text>
</svg>
```
**问题**：
- ❌ 没有 `viewBox`（使用硬编码尺寸）
- ❌ 没有 `font-family` 属性
- ❌ 没有 `xmlns` 命名空间
- ❌ 没有圆角（`rx` 属性）
- ❌ 代码长度短（< 300 字符）

✅ **正确：生成完整版本**
```xml
<!-- 正确：完整版本，包含所有必需元素 -->
<svg width="100%" style="max-width: 400px" viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="20" width="120" height="60"
        fill="#1890ff" stroke="#096dd9" stroke-width="2" rx="8"/>
  <text x="80" y="55" text-anchor="middle"
        font-family="-apple-system, BlinkMacSystemFont, sans-serif"
        font-size="14" fill="#fff">系统A</text>
</svg>
```
**优点**：
- ✅ 使用 `viewBox`（响应式）
- ✅ 有 `font-family` 属性
- ✅ 有 `xmlns` 命名空间
- ✅ 有圆角（`rx="8"`）
- ✅ 代码长度合理（> 500 字符）
- ✅ 专业美观

**质量检查清单（必须全部满足）：**
- ✅ 代码长度 > 500 字符（包含完整结构）
- ✅ 使用 `viewBox` 而非硬编码尺寸
- ✅ 使用主题色系
- ✅ 所有文本有 `font-family` 属性
- ✅ 方框有 `rx` 圆角属性
- ✅ 包含 `xmlns` 命名空间

**原则：**
> **无论使用多少个 Task，每个生成的图形质量必须一致，不能为了速度或 Task 数量多而降低标准。**
>
> 每个图形都必须包含完整的元素（viewBox、font-family、圆角、主题色等）。

### 错误 11：HTML 的 class 无前缀导致冲突 ⚠️ 常见错误

❌ **错误：class 无前缀，与主 HTML 文档冲突**

```html
<!-- ❌ 错误：class 无前缀 -->
<div class="container">
  <button class="btn">按钮</button>
</div>

<style>
.container { background: #f5f5f5; }  /* 会影响主文档的 .container */
.btn { background: #1890ff; }        /* 会影响主文档的 .btn */
</style>
```

**问题：**
- ❌ 生成的 HTML 中的 class 会与主文档的同名 class 冲突
- ❌ 主文档的样式会覆盖生成的样式，导致显示错乱
- ❌ 多个占位符之间也会互相影响

✅ **正确：所有 class 加前缀，完全隔离**

```html
<!-- ✅ 正确：class 有前缀 -->
<!-- 假设这是 ui 类型的第 3 个占位符，前缀为 ui-3- -->
<div class="ui-3-container">
  <button class="ui-3-btn">按钮</button>
</div>

<style>
.ui-3-container { background: #f5f5f5; }  /* 只影响这个占位符 */
.ui-3-btn { background: #1890ff; }        /* 只影响这个占位符 */
</style>
```

**前缀规则：**
- 格式：`[示意图类型]-[占位符ID]-`
- 示例：
  - `ui-1-`, `ui-2-`, `ui-3-`（ui 类型）
  - `architecture-1-`, `architecture-2-`（architecture 类型，如果用 HTML）

**验证清单：**
- [ ] 所有 class 都有前缀
- [ ] CSS 选择器都使用带前缀的 class
- [ ] 没有使用元素选择器（如 `button { ... }`）
- [ ] 没有使用通配符选择器（如 `* { ... }`）

**原则：**
> **所有生成的 HTML 中的 class 必须加前缀，确保与主 HTML 文档完全隔离，避免样式冲突。**
>
> 前缀格式：`[示意图类型]-[占位符ID]-`，例如：`ui-1-container`、`ui-2-btn`。


**完整的技术细节和故障排查**：见 `guides/technical-details.md`

