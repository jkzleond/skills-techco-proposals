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

## 验证清单

AI Agent 在生成代码后应检查：

### SVG 检查项
- [ ] 以 `<svg` 开头，`</svg>` 结尾
- [ ] 包含 `xmlns` 属性
- [ ] 包含 `viewBox` 属性
- [ ] 使用主题色系（根据选择的主题）
- [ ] 包含圆角、阴影等美化效果
- [ ] 文本可读（字体大小合适）
- [ ] 没有明显的语法错误

### HTML 检查项
- [ ] 使用语义化标签（`div`, `button`, `input` 等）
- [ ] 包含内联样式或 `<style>` 标签
- [ ] 使用主题色系
- [ ] 包含圆角、阴影、渐变等美化效果
- [ ] 使用 flexbox 或 grid 布局
- [ ] 包含 hover、focus 等交互效果
- [ ] 按钮有 cursor: pointer
- [ ] 文本可读、对比度足够

## 常见错误

### ❌ 不要这样做

**错误1：机械转换（只包在SVG里）**
```xml
<!-- 错误：只是把ASCII包在SVG里 -->
<svg>
  <text>┌────────┐</text>
  <text>│  标题  │</text>
  <text>└────────┘</text>
</svg>
```

**错误2：UI类型使用SVG**
```xml
<!-- 错误：UI应该用HTML，不用SVG -->
<svg>
  <rect>按钮</rect>
</svg>
```

**错误3：忽略主题色**
```xml
<!-- 错误：硬编码颜色，应该使用主题色 -->
<rect stroke="#ff0000">
<!-- 应该使用 {primary} 变量 -->
```

### ✅ 应该这样做

**正确1：智能理解，重新绘制**
```xml
<!-- 正确：理解结构，用矢量元素重绘 -->
<svg>
  <rect x="20" y="20" width="120" height="60" fill="white" stroke="{primary}" rx="8"/>
  <text x="80" y="55" text-anchor="middle">标题</text>
</svg>
```

**正确2：UI类型使用HTML**
```html
<!-- 正确：生成真实的HTML界面 -->
<div style="background: {primary};">
  <button>按钮</button>
</div>
```

**正确3：使用主题色**
```xml
<!-- 正确：根据主题使用色系 -->
<rect stroke="{primary}" fill="url(#grad1)">
```

## 获取主题色系

在生成代码时，从以下来源获取主题色：

1. **询问用户**（如果需要）
2. **从 SKILL.md 读取**主题配置
3. **使用占位符变量** `{primary}` 和 `{secondary}`

生成时替换为实际颜色值。
