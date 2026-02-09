# AI Agent 代码生成规范

本文档为 AI Agent 提供 ASCII 图转换为 SVG/HTML 代码的标准化规范。

## 核心原则

### 1. 理解优先于转换
不要机械地转换 ASCII 字符，要理解图形的结构和含义，用矢量元素重新绘制。

### 2. 美观与可读性并重
代码不仅要功能正确，还要视觉精美，符合现代设计审美。

### 3. 主题一致性
严格使用指定主题的色系，保持整个文档的视觉一致性。

---

## 色彩系统

### 四大主题色系

```python
# 紫色主题 (purple)
PRIMARY = "#667eea"
SECONDARY = "#764ba2"
BG_GRADIENT = "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"

# 蓝色主题 (blue)
PRIMARY = "#1890ff"
SECONDARY = "#096dd9"
BG_GRADIENT = "linear-gradient(135deg, #1890ff 0%, #096dd9 100%)"

# 绿色主题 (green)
PRIMARY = "#52c41a"
SECONDARY = "#389e0d"
BG_GRADIENT = "linear-gradient(135deg, #52c41a 0%, #389e0d 100%)"

# 极简主题 (minimal)
PRIMARY = "#333333"
SECONDARY = "#666666"
BG_GRADIENT = "linear-gradient(135deg, #333333 0%, #666666 100%)"
```

### 辅助色彩

```python
WHITE = "#ffffff"
BLACK = "#000000"
GRAY_LIGHT = "#f5f5f5"
GRAY_MEDIUM = "#999999"
GRAY_DARK = "#333333"
SHADOW = "rgba(0, 0, 0, 0.1)"
```

---

## SVG 通用规范

### 1. 基础结构模板

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {width} {height}"
     width="100%"
     style="max-width:{max_width}px"
>
  <!-- SVG 内容 -->
</svg>
```

**必须包含的属性：**
- `xmlns="http://www.w3.org/2000/svg"` - SVG 命名空间
- `viewBox="0 0 {width} {height}"` - 视口坐标
- `width="100%"` - 响应式宽度
- `style="max-width:{max_width}px"` - 最大宽度限制

### 2. 标准 Definitions 模板

```xml
<defs>
  <!-- 主渐变 -->
  <linearGradient id="grad{id}" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" style="stop-color:{PRIMARY};stop-opacity:1" />
    <stop offset="100%" style="stop-color:{SECONDARY};stop-opacity:1" />
  </linearGradient>

  <!-- 阴影滤镜 -->
  <filter id="shadow{id}" x="-20%" y="-20%" width="140%" height="140%">
    <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.1"/>
  </filter>

  <!-- 箭头标记 -->
  <marker id="arrow{id}" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
    <polygon points="0 0, 10 3, 0 6" fill="{SECONDARY}" />
  </marker>
</defs>
```

**注意：** 每个 SVG 的 id 应该唯一，避免冲突（如 `grad1`, `grad2`, `shadow1`, `shadow2`）

### 3. 基础图形元素

#### 矩形框（卡片/模块）

```xml
<rect x="{x}" y="{y}"
      width="{width}" height="{height}"
      fill="white"
      stroke="{PRIMARY}"
      stroke-width="2"
      rx="8"
      filter="url(#shadow{id})"/>
```

**参数说明：**
- `rx="8"` - 圆角半径（推荐 8-12px）
- `stroke-width="2"` - 边框粗细（推荐 2px）
- `filter="url(#shadow{id})"` - 阴影效果

#### 文本标签

```xml
<text x="{x}" y="{y}"
      text-anchor="middle"
      font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
      font-size="{size}"
      font-weight="{weight}"
      fill="{color}">
  文本内容
</text>
```

**参数说明：**
- `text-anchor="middle"` - 水平居中（左对齐用 `start`，右对齐用 `end`）
- `font-size` - 推荐 14-16px（正文），18-20px（标题）
- `font-weight` - `400`（常规），`600`（中等），`700`（粗体）
- `fill` - `#333`（正文），`{PRIMARY}`（标题）

#### 连接线（箭头）

```xml
<line x1="{x1}" y1="{y1}"
      x2="{x2}" y2="{y2}"
      stroke="{SECONDARY}"
      stroke-width="2"
      marker-end="url(#arrow{id})"/>
```

**参数说明：**
- `stroke-width="2"` - 线条粗细（推荐 2px）
- `marker-end` - 箭头标记

---

## 分类型生成规范

### 类型 1: 流程图 (flowchart)

#### 结构模式

```
起始节点 → 处理节点 → 处理节点 → 结束节点
```

#### 垂直流程模板

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 400 700"
     width="100%"
     style="max-width:400px">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#1890ff"/>
      <stop offset="100%" style="stop-color:#096dd9"/>
    </linearGradient>
    <filter id="shadow1">
      <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.1"/>
    </filter>
    <marker id="arrow1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#096dd9"/>
    </marker>
  </defs>

  <!-- 步骤 1 -->
  <rect x="50" y="20" width="300" height="50" fill="white" stroke="#1890ff" stroke-width="2" rx="8" filter="url(#shadow1)"/>
  <text x="200" y="50" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#333">步骤 1</text>

  <!-- 箭头 -->
  <line x1="200" y1="70" x2="200" y2="100" stroke="#096dd9" stroke-width="2" marker-end="url(#arrow1)"/>

  <!-- 步骤 2 -->
  <rect x="50" y="100" width="300" height="50" fill="white" stroke="#1890ff" stroke-width="2" rx="8" filter="url(#shadow1)"/>
  <text x="200" y="130" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#333">步骤 2</text>

  <!-- ... 更多步骤 ... -->
</svg>
```

#### 特殊处理

**起始/结束节点：** 使用渐变背景突出显示
```xml
<rect x="50" y="20" width="300" height="50" fill="url(#grad1)" stroke="none" rx="8"/>
<text x="200" y="50" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="600" fill="white">开始</text>
```

**关键节点：** 使用不同边框颜色或加粗边框
```xml
<rect x="50" y="200" width="300" height="50" fill="white" stroke="#096dd9" stroke-width="3" rx="8" filter="url(#shadow1)"/>
```

**条件分支：** 使用菱形或不同颜色路径
```xml
<!-- 条件判断节点 -->
<polygon points="200,150 280,200 200,250 120,200" fill="white" stroke="#1890ff" stroke-width="2" filter="url(#shadow1)"/>
```

#### 漏斗图特殊处理

```xml
<!-- 漏斗层级，从宽到窄 -->
<rect x="50" y="20" width="300" height="60" fill="url(#grad1)" rx="8"/>  <!-- 顶层 100% -->
<rect x="75" y="100" width="250" height="60" fill="url(#grad2)" rx="8"/> <!-- 第二层 60% -->
<rect x="100" y="180" width="200" height="60" fill="url(#grad3)" rx="8"/> <!-- 第三层 40% -->
<rect x="125" y="260" width="150" height="60" fill="url(#grad4)" rx="8"/> <!-- 底层 30% -->
```

---

### 类型 2: 架构图 (architecture)

#### 结构模式

```
┌──────────────┐
│   系统层     │
└──────────────┘
       ↓
┌──────────────┐
│  模块层      │
│ ┌──┐ ┌──┐   │
│ │A │ │B │   │
│ └──┘ └──┘   │
└──────────────┘
```

#### 层级架构模板

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 500 750"
     width="100%"
     style="max-width:500px">
  <defs>
    <!-- 同上 -->
  </defs>

  <!-- 顶层系统 -->
  <rect x="50" y="20" width="400" height="80" fill="white" stroke="#1890ff" stroke-width="2" rx="8" filter="url(#shadow1)"/>
  <text x="250" y="65" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="600" fill="#333">官网/公众号</text>

  <!-- 连接箭头 -->
  <line x1="250" y1="100" x2="250" y2="140" stroke="#096dd9" stroke-width="2" marker-end="url(#arrow1)"/>

  <!-- 中间系统容器 -->
  <rect x="50" y="140" width="400" height="280" fill="none" stroke="#1890ff" stroke-width="2" rx="8" stroke-dasharray="5,5"/>

  <!-- 子模块 A -->
  <rect x="75" y="170" width="160" height="100" fill="white" stroke="#1890ff" stroke-width="2" rx="8" filter="url(#shadow1)"/>
  <text x="155" y="225" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#333">信息展示区</text>

  <!-- 子模块 B -->
  <rect x="265" y="170" width="160" height="100" fill="white" stroke="#1890ff" stroke-width="2" rx="8" filter="url(#shadow1)"/>
  <text x="345" y="225" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#333">互动转化区</text>

  <!-- ... 更多模块 ... -->
</svg>
```

#### 数据流向表示

**实线箭头：** 直接调用
```xml
<line x1="250" y1="100" x2="250" y2="140" stroke="#096dd9" stroke-width="2" marker-end="url(#arrow1)"/>
```

**虚线箭头：** 异步/数据同步
```xml
<line x1="250" y1="440" x2="250" y2="480" stroke="#096dd9" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#arrow1)"/>
```

**双向箭头：** 双向通信
```xml
<defs>
  <marker id="arrow-start" markerWidth="10" markerHeight="10" refX="1" refY="3" orient="auto">
    <polygon points="10 0, 0 3, 10 6" fill="#096dd9"/>
  </marker>
</defs>
<line x1="100" y1="100" x2="200" y2="100" stroke="#096dd9" stroke-width="2" marker-start="url(#arrow-start)" marker-end="url(#arrow1)"/>
```

#### 容器分组

使用虚线边框表示逻辑分组：
```xml
<rect x="50" y="140" width="400" height="280" fill="none" stroke="#1890ff" stroke-width="2" rx="8" stroke-dasharray="5,5"/>
```

---

### 类型 3: 时间线图 (timeline)

#### 水平时间线模板

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 700 300"
     width="100%"
     style="max-width:700px">
  <defs>
    <!-- 同上 -->
  </defs>

  <!-- 主时间轴线 -->
  <line x1="50" y1="150" x2="650" y2="150" stroke="#096dd9" stroke-width="3"/>

  <!-- 时间节点 1 -->
  <circle cx="100" cy="150" r="10" fill="#1890ff" stroke="white" stroke-width="3"/>
  <text x="100" y="190" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#333">Week 1</text>
  <rect x="50" y="80" width="100" height="50" fill="white" stroke="#1890ff" stroke-width="2" rx="8" filter="url(#shadow1)"/>
  <text x="100" y="110" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#333">需求分析</text>

  <!-- 时间节点 2 -->
  <circle cx="250" cy="150" r="10" fill="#1890ff" stroke="white" stroke-width="3"/>
  <text x="250" y="190" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#333">Week 2</text>
  <rect x="200" y="80" width="100" height="50" fill="white" stroke="#1890ff" stroke-width="2" rx="8" filter="url(#shadow1)"/>
  <text x="250" y="110" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#333">UI 设计</text>

  <!-- ... 更多节点 ... -->
</svg>
```

#### 关键节点突出

```xml
<!-- 最终里程碑节点 -->
<circle cx="600" cy="150" r="12" fill="#52c41a" stroke="white" stroke-width="3"/>
<rect x="550" y="80" width="100" height="50" fill="url(#successGrad)" stroke="none" rx="8"/>
<text x="600" y="110" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="600" fill="white">验收</text>
```

---

## HTML 生成规范（UI 类型）

### 1. 整体结构模板

```html
<div style="background: #f5f5f5;
            padding: 40px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <!-- 页面内容 -->
</div>
```

### 2. 响应式布局

#### Flexbox 布局（推荐）

```html
<!-- 水平排列 -->
<div style="display: flex; gap: 16px; align-items: center;">
  <div style="flex: 1;">项目 1</div>
  <div style="flex: 1;">项目 2</div>
</div>

<!-- 垂直排列 -->
<div style="display: flex; flex-direction: column; gap: 12px;">
  <div>项目 1</div>
  <div>项目 2</div>
</div>
```

#### Grid 布局

```html
<!-- 2列网格 -->
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
  <div>项目 1</div>
  <div>项目 2</div>
</div>

<!-- 3列网格 -->
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
  <div>项目 1</div>
  <div>项目 2</div>
  <div>项目 3</div>
</div>
```

### 3. 卡片组件

```html
<div style="background: white;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            border: 1px solid #e8e8e8;">
  <!-- 卡片内容 -->
</div>
```

### 4. 按钮组件

#### 主按钮

```html
<button style="padding: 12px 24px;
               background: linear-gradient(135deg, #1890ff 0%, #096dd9 100%);
               color: white;
               border: none;
               border-radius: 8px;
               font-size: 16px;
               font-weight: 600;
               cursor: pointer;
               transition: all 0.2s;
               box-shadow: 0 2px 4px rgba(24, 144, 255, 0.3);">
  立即报名
</button>
```

#### 次要按钮

```html
<button style="padding: 12px 24px;
               background: white;
               color: #1890ff;
               border: 2px solid #1890ff;
               border-radius: 8px;
               font-size: 16px;
               font-weight: 600;
               cursor: pointer;
               transition: all 0.2s;">
  了解更多
</button>
```

#### 文字按钮

```html
<button style="padding: 8px 16px;
               background: transparent;
               color: #1890ff;
               border: none;
               font-size: 14px;
               font-weight: 600;
               cursor: pointer;
               text-decoration: underline;">
  查看详情
</button>
```

### 5. 表单组件

```html
<!-- 表单容器 -->
<div style="background: white;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);">

  <!-- 输入框 -->
  <div style="margin-bottom: 16px;">
    <label style="display: block;
                margin-bottom: 8px;
                font-size: 14px;
                font-weight: 600;
                color: #333;">
      姓名
    </label>
    <input type="text"
           placeholder="请输入您的姓名"
           style="width: 100%;
                  padding: 12px;
                  border: 2px solid #e8e8e8;
                  border-radius: 8px;
                  font-size: 14px;
                  transition: border-color 0.2s;"/>
  </div>

  <!-- 单选按钮 -->
  <div style="margin-bottom: 16px;">
    <label style="display: block;
                margin-bottom: 8px;
                font-size: 14px;
                font-weight: 600;
                color: #333;">
      票种
    </label>
    <label style="display: flex; align-items: center; margin-bottom: 8px; cursor: pointer;">
      <input type="radio" name="ticket" style="margin-right: 8px;"/>
      <span>会员票（1200元）</span>
    </label>
  </div>

  <!-- 提交按钮 -->
  <button style="width: 100%;
                 padding: 14px;
                 background: linear-gradient(135deg, #1890ff 0%, #096dd9 100%);
                 color: white;
                 border: none;
                 border-radius: 8px;
                 font-size: 16px;
                 font-weight: 600;
                 cursor: pointer;">
    提交报名
  </button>
</div>
```

### 6. 排版规范

#### 标题

```html
<h1 style="font-size: 32px; font-weight: 700; color: #333; margin-bottom: 16px;">主标题</h1>
<h2 style="font-size: 24px; font-weight: 600; color: #333; margin-bottom: 12px;">二级标题</h2>
<h3 style="font-size: 20px; font-weight: 600; color: #333; margin-bottom: 10px;">三级标题</h3>
```

#### 文本

```html
<p style="font-size: 16px; line-height: 1.6; color: #666; margin-bottom: 12px;">
  正文内容
</p>

<span style="font-size: 14px; color: #999;">辅助文本</span>
```

#### 强调文本

```html
<strong style="font-weight: 600; color: #1890ff;">重点内容</strong>

<mark style="background: #e6f7ff; color: #1890ff; padding: 2px 6px; border-radius: 4px;">
  高亮内容
</mark>
```

### 7. 列表组件

```html
<!-- 无序列表 -->
<ul style="list-style: none; padding: 0; margin: 0;">
  <li style="padding: 12px 0; border-bottom: 1px solid #e8e8e8; display: flex; align-items: start;">
    <span style="color: #1890ff; margin-right: 8px;">•</span>
    <span>列表项 1</span>
  </li>
  <li style="padding: 12px 0; border-bottom: 1px solid #e8e8e8; display: flex; align-items: start;">
    <span style="color: #1890ff; margin-right: 8px;">•</span>
    <span>列表项 2</span>
  </li>
</ul>
```

### 8. 图片组件

```html
<!-- 响应式图片 -->
<img src="image.jpg"
     alt="描述文本"
     style="width: 100%;
            height: auto;
            border-radius: 8px;
            object-fit: cover;"/>

<!-- 头像 -->
<img src="avatar.jpg"
     alt="张三"
     style="width: 80px;
            height: 80px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #1890ff;"/>
```

### 9. 徽章/标签

```html
<!-- 主徽章 -->
<span style="display: inline-block;
              padding: 4px 12px;
              background: linear-gradient(135deg, #1890ff 0%, #096dd9 100%);
              color: white;
              font-size: 12px;
              font-weight: 600;
              border-radius: 12px;">
  热门
</span>

<!-- 灰色徽章 -->
<span style="display: inline-block;
              padding: 4px 12px;
              background: #f5f5f5;
              color: #666;
              font-size: 12px;
              font-weight: 600;
              border-radius: 12px;">
  已满
</span>
```

### 10. 交互效果

#### Hover 效果

```html
<button style="transition: all 0.2s;"
        onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 16px rgba(24, 144, 255, 0.3)'"
        onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 4px rgba(24, 144, 255, 0.3)'">
  悬停效果
</button>
```

#### Focus 效果（可访问性）

```html
<input type="text"
       style="outline: none;"
       onfocus="this.style.borderColor='#1890ff'; this.style.boxShadow='0 0 0 3px rgba(24, 144, 255, 0.1)'"
       onblur="this.style.borderColor='#e8e8e8'; this.style.boxShadow='none'"/>
```

---

## 通用最佳实践

### 1. 尺寸规范

```python
# 间距
SPACE_XS = "4px"
SPACE_SM = "8px"
SPACE_MD = "12px"
SPACE_LG = "16px"
SPACE_XL = "24px"
SPACE_XXL = "32px"

# 圆角
RADIUS_SM = "4px"
RADIUS_MD = "8px"
RADIUS_LG = "12px"
RADIUS_XL = "16px"

# 字号
FONT_XS = "12px"
FONT_SM = "14px"
FONT_MD = "16px"
FONT_LG = "18px"
FONT_XL = "20px"
FONT_XXL = "24px"
```

### 2. 阴影规范

```python
# 轻微阴影
SHADOW_SM = "0 2px 4px rgba(0, 0, 0, 0.1)"

# 中等阴影
SHADOW_MD = "0 4px 12px rgba(0, 0, 0, 0.1)"

# 深度阴影
SHADOW_LG = "0 8px 24px rgba(0, 0, 0, 0.15)"

# 彩色阴影（主题色）
SHADOW_PRIMARY = "0 4px 12px rgba(24, 144, 255, 0.3)"
```

### 3. 过渡动画

```css
transition: all 0.2s ease;
transition: transform 0.2s ease;
transition: background-color 0.2s ease;
transition: border-color 0.2s ease;
```

### 4. 响应式断点

```html
<!-- 移动优先策略 -->
<div style="width: 100%; max-width: 1200px; margin: 0 auto; padding: 16px;">
  <!-- 内容 -->
</div>

<!-- 媒体查询（通过 style 标签） -->
<style>
  @media (min-width: 768px) {
    .container {
      padding: 32px;
    }
  }
</style>
```

### 5. 可访问性

```html
<!-- 语义化标签 -->
<button>按钮</button>  <!-- ✅ -->
<div>按钮</div>        <!-- ❌ -->

<!-- alt 属性 -->
<img src="image.jpg" alt="图片描述"/>

<!-- 颜色对比度 -->
- 文本与背景对比度 ≥ 4.5:1
- 大文本与背景对比度 ≥ 3:1

<!-- 焦点状态 -->
<button style="outline: 2px solid #1890ff; outline-offset: 2px;">
```

---

## 质量检查清单

### SVG 检查清单

- [ ] 以 `<svg` 开头，`</svg>` 结尾
- [ ] 包含 `xmlns="http://www.w3.org/2000/svg"`
- [ ] 包含 `viewBox` 属性
- [ ] 使用 `width="100%"` 和 `style="max-width:XXXpx"`
- [ ] 所有渐变、滤镜、标记的 id 唯一
- [ ] 使用主题色系（PRIMARY / SECONDARY）
- [ ] 文本字体大小合适（14-20px）
- [ ] 文本颜色对比度足够
- [ ] 矩形使用圆角（rx="8"）
- [ ] 使用阴影效果（filter="url(#shadow)"）
- [ ] 连接线使用箭头（marker-end="url(#arrow)"）
- [ ] 没有语法错误（XML 标签闭合）

### HTML 检查清单

- [ ] 使用语义化标签（button, input, label 等）
- [ ] 包含内联样式或 `<style>` 标签
- [ ] 使用主题色系（PRIMARY / SECONDARY）
- [ ] 使用 Flexbox 或 Grid 布局
- [ ] 按钮包含 `cursor: pointer`
- [ ] 交互元素包含 `transition` 过渡效果
- [ ] 表单元素包含 `<label>` 标签
- [ ] 输入框包含 `placeholder`
- [ ] 图片包含 `alt` 属性
- [ ] 响应式设计（width: 100%, max-width）
- [ ] 文本可读、对比度足够
- [ ] 间距一致（使用统一的 spacing）

### 通用检查清单

- [ ] 代码格式化、缩进正确
- [ ] 注释清晰（复杂逻辑）
- [ ] 没有硬编码的魔法数字
- [ ] 颜色使用变量或主题色
- [ ] 字体使用系统字体栈
- [ ] 没有废弃的 HTML/SVG 属性
- [ ] 在主流浏览器中测试通过

---

## 常见错误示例

### ❌ 错误 1: 机械转换 ASCII

```xml
<!-- 错误：只把 ASCII 包在 SVG 里 -->
<svg>
  <text>┌────────┐</text>
  <text>│  标题  │</text>
  <text>└────────┘</text>
</svg>
```

**✅ 正确做法：理解结构，重新绘制**
```xml
<svg>
  <rect x="0" y="0" width="100" height="50" fill="white" stroke="#1890ff" rx="8"/>
  <text x="50" y="30" text-anchor="middle">标题</text>
</svg>
```

### ❌ 错误 2: 忽略主题色

```xml
<!-- 错误：硬编码其他颜色 -->
<rect stroke="#ff0000" fill="#00ff00"/>
```

**✅ 正确做法：使用主题色**
```xml
<rect stroke="{PRIMARY}" fill="url(#grad1)"/>
```

### ❌ 错误 3: UI 类型使用 SVG

```xml
<!-- 错误：UI 应该用 HTML -->
<svg>
  <rect x="0" y="0" width="200" height="40">按钮</rect>
</svg>
```

**✅ 正确做法：使用 HTML**
```html
<button style="padding: 12px 24px; background: #1890ff; color: white;">
  按钮
</button>
```

### ❌ 错误 4: 缺少响应式

```xml
<!-- 错误：固定宽度 -->
<svg width="500" height="300">
```

**✅ 正确做法：响应式宽度**
```xml
<svg width="100%" style="max-width:500px" viewBox="0 0 500 300">
```

### ❌ 错误 5: id 冲突

```xml
<!-- 错误：多个 SVG 使用相同 id -->
<svg><defs><linearGradient id="grad1"/></defs></svg>
<svg><defs><linearGradient id="grad1"/></defs></svg>
```

**✅ 正确做法：每个 SVG 使用唯一 id**
```xml
<svg><defs><linearGradient id="grad1"/></defs></svg>
<svg><defs><linearGradient id="grad2"/></defs></svg>
```

---

## 示例参考

完整的代码示例请参考：
- `/references/output-specs.md` - 输出格式规范
- `/references/ascii-to-svg.md` - ASCII 识别和转换技巧

**成功案例：**
- `培训课程活动落地页建设方案.html` - 8 个精美图表（7 SVG + 1 HTML）
- `官网及业务系统升级方案.html` - 完整的售前方案转换

---

## 总结

**核心要点：**
1. **理解优先** - 理解图形含义，不要机械转换
2. **主题一致** - 严格使用指定主题的色系
3. **美观实用** - 渐变、阴影、圆角一个都不能少
4. **响应式** - SVG 用 `width="100%"`，HTML 用 flex/grid
5. **质量保证** - 按照检查清单验证代码

**AI Agent 执行流程：**
1. 读取 JSON 文件，获取所有占位符
2. 根据类型选择对应的模板（flowchart/architecture/ui/timeline）
3. 使用主题色系和标准元素生成代码
4. 填充 JSON 的 `svg_code` 字段
5. 调用替换脚本生成最终 HTML
6. 验证没有残留占位符

遵循本规范，AI Agent 可以生成高质量、一致性强、视觉精美的代码！
