---
name: svg-beautifier
description: 自动将 HTML/Markdown 中的基础 SVG 或 ASCII 图转换为具有现代 UI 风格（渐变、阴影、圆角）的专业图表。
---

# SVG 美化技能 (SVG Beautifier)

本技能旨在将功能性但简陋的 SVG/ASCII 图表转化为符合现代企业 SaaS 审美的高权重视觉资源。

## 🎯 核心原则 (Core Principles)

- **层次感 (Hierarchy)**: 必须定义 `<defs>` 并在其中配置标准阴影 (`feDropShadow`) 和渐变。
- **UI 质感 (Texture)**:
    - **容器**: 矩形圆角固定为 `12px`-`16px`。
    - **装饰**: 节点侧边应有进度条或图标提示（如 `rect` 高亮条）。
- **动态性 (Dynamics)**: 连接线优先使用 `marker-end` 的自定义箭头，并对次要逻辑使用 `stroke-dasharray`。
- **字体规范**: 强制使用 `PingFang SC, Microsoft YaHei, Arial` 字体堆栈，主标题 `font-weight: 600`。

## 🔧 技术标准 (Technical Standards)

### 必备滤镜与标记
AI 在生成代码时应始终包含以下定义（颜色值请读取 `CONFIG.yaml`）：
```xml
<defs>
  <!-- 标准阴影 -->
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
    <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000" flood-opacity="0.1" />
  </filter>
  <!-- 标准箭头 -->
  <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
    <polygon points="0 0, 10 3.5, 0 7" fill="{{brand.primary}}" />
  </marker>
</defs>
```

## 📖 技术指南 (按需读取)

具体图形类型的实现细节请参阅：
- 📊 **图表风格规范**: `references/chart-styles.md` (柱状图、折线图、饼图)
- 🕸️ **流程与架构模式**: `references/flowchart-patterns.md` (逻辑流、系统层级)

## 🛠️ AI 交互流程

### 步骤 1：定位目标图表
AI 扫描文档，寻找 `<svg>` 标签或带有 ` ```ascii ` 标记的代码块。

### 步骤 2：读取品牌配置
读取 `CONFIG.yaml` 中的全局变量，替换 Skill 中的 `{{PRIMARY_COLOR}}` 等占位符。

### 步骤 3：生成美化方案
根据图形类型生成对应的美化 SVG 代码。
- **如果是 ASCII**: 先识别结构，再生成 SVG。
- **如果是 SVG**: 提取核心元素，重新套用现代样式模板。

### 步骤 4：验证并应用
检查生成的 SVG 是否包含 `xmlns`, `viewBox`，以及是否满足 `references/` 中的质量清单。

## 📋 检查清单 (Checklist)

- [ ] 是否正确引入了 `<defs>` 中的阴影与渐变定义？
- [ ] 所有矩形节点是否应用了 `rx` 圆角？
- [ ] 线条终点是否正确关联了 `marker-end`？
- [ ] 颜色方案是否完全同步于 `CONFIG.yaml` 中的变量？
- [ ] 文本层级（字体大小、粗细）是否符合视觉重心原则？

> [!TIP]
> 优秀的 SVG 美化不仅仅是添加颜色，更是通过 `defs` 建立一套可复用的视觉组件库。
