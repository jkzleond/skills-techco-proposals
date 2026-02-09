# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个 **AI Agent SKILL 制作研究项目**，探索和总结 SKILL 的编写方法、设计模式和最佳实践。

项目包含 3 个完整的研究案例，展示如何将复杂的业务流程和专业知识转化为可被 AI Agent 理解和执行的 SKILL 文档。这些案例既是可用的技能，也是学习 SKILL 制作的参考实现。

### 研究案例

1. **converting-markdown** - 展示脚本与 AI 协作模式、多步骤交互流程设计
2. **presales-proposal** - 展示纯文档 SKILL、占位符系统、专业知识转化
3. **internal-project-plan** - 展示复杂计算 SKILL、决策支持、业务逻辑编排
4. **svg-beautifier** - 展示视觉提升 SKILL、按需加载指南、品牌风格注入

---

## 核心架构设计

### 技能职责分离原则

本项目采用"脚本负责机械工作，AI 负责智能工作"的架构设计：

- **Python 脚本（机械工作）**：文件操作、占位符提取、内容替换、格式转换
- **AI Agent（智能工作）**：理解 ASCII 图结构、生成 SVG/HTML 代码、决策主题选择

### 目录结构

```
skills-techco-proposals/
├── converting-markdown/           # Markdown 转 HTML 技能
│   ├── SKILL.md                   # 技能定义和交互流程
│   ├── guides/                    # 技术指南（AI 按需读取）
│   │   ├── output-specs.md        # SVG/HTML 输出格式规范
│   │   └── ascii-to-svg.md        # ASCII 图识别和转换技巧
│   ├── templates/                 # 主题配置（YAML）
│   │   ├── purple.yaml            # 紫色渐变主题（售前方案）
│   │   ├── blue.yaml              # 蓝色科技主题（技术文档）
│   │   ├── green.yaml             # 绿色清新主题（内部报告）
│   │   ├── minimal.yaml           # 极简灰度主题（正式报告）
│   │   └── base.yaml              # 基础样式模板
│   └── scripts/
│       ├── convert.py             # 主转换脚本（支持 --theme 参数）
│       ├── themes.py              # 主题加载工具
│       ├── extract_placeholders.py # 提取占位符到 JSON
│       ├── replace_svg.py         # 替换占位符为 SVG/HTML
│       └── ascii_to_svg_converter.py # ASCII 图转换逻辑
│
├── presales-proposal/             # 售前方案编制技能
│   ├── SKILL.md                   # 技能定义和编制规范
│   └── CONFIG.yaml                # 公司配置（公司名称、角色等）
│
├── internal-project-plan/         # 内部项目规划技能
│   ├── SKILL.md                   # 技能定义和规划规范
│   └── CONFIG.yaml                # 公司配置
│
└── svg-beautifier/                # SVG 美化技能
    ├── SKILL.md                   # 技能定义与核心原则
    ├── CONFIG.yaml                # 全局视觉配置
    └── guides/                    # 风格指南（按需读取）
        ├── chart-styles.md        # 图表美化指南
        └── flowchart-patterns.md  # 流程架构美化指南
```

---

## 项目维护和扩展

### 添加新的研究案例

当添加新的 SKILL 案例时，遵循以下结构：

```
new-skill-case/
├── SKILL.md                   # 主交互流程和规范
├── CONFIG.yaml                # 用户配置（如需要）
├── guides/                    # 按需加载的技术细节（可选）
│   ├── guide-1.md
│   └── guide-2.md
└── scripts/                   # Python 脚本（可选）
    ├── script1.py
    └── script2.py
```

**决策树**：
- 需要调用外部工具？→ 添加 `scripts/` 目录
- 有复杂技术细节？→ 添加 `guides/` 目录
- 需要用户配置？→ 添加 `CONFIG.yaml`
- 纯文档逻辑？→ 只需 `SKILL.md`

### SKILL 编写检查清单

在提交新的 SKILL 案例前，确保：

**结构检查**：
- [ ] 包含 YAML Front Matter（name、description）
- [ ] 有明确的"AI 交互流程"章节
- [ ] 技术细节放在 `guides/` 目录（可选）
- [ ] 有检查清单章节

**质量检查**：
- [ ] 使用"正确/错误"示例对比
- [ ] 职责分离清晰（脚本 vs AI）
- [ ] 交互步骤明确（使用 AskUserQuestion）
- [ ] 占位符系统完整（如需要）

**兼容性检查**：
- [ ] 兼容 Claude、ChatGPT、Gemini 等平台
- [ ] 避免使用特定平台的专有功能
- [ ] 使用标准的 Markdown 格式

### 文档更新同步

当修改 SKILL 案例时，同步更新以下文档：

1. **README.md**：
   - 更新"研究案例"章节
   - 更新"SKILL 设计模式"章节（如有新模式）
   - 更新"学习路径"章节

2. **CLAUDE.md**：
   - 更新"研究案例"列表
   - 更新"核心架构设计"（如有架构变化）
   - 更新"关键开发命令"（如有新命令）

3. **CHANGELOG.md**（建议创建）：
   - 记录版本变更
   - 记录新增的设计模式
   - 记录重大改进

### 代码审查要点

当审查 PR 时，关注：

**SKILL.md 质量**：
- 交互流程是否清晰？
- 是否有足够的示例？
- 检查清单是否完整？

**设计模式一致性**：
- 是否遵循现有的设计模式？
- 是否引入了新的模式（需要文档化）？
- 职责分离是否清晰？

**用户体验**：
- 首次使用是否需要配置？
- 错误提示是否友好？
- 是否有足够的反馈？

---

## 关键开发命令

### Python 依赖安装

```bash
# 必需依赖（用于 converting-markdown）
pip3 install pyyaml markdown
```

### converting-markdown 使用

```bash
# 列出所有可用主题
python3 converting-markdown/scripts/convert.py --list-themes

# 转换文档（使用默认 purple 主题）
python3 converting-markdown/scripts/convert.py document.md

# 转换文档（指定主题）
python3 converting-markdown/scripts/convert.py document.md --theme blue

# 智能 ASCII 图转换模式（3 步流程）
# 步骤1：生成带占位符的 HTML
AI_SVG_CONVERSION=true python3 converting-markdown/scripts/convert.py document.md --theme purple

# 步骤2：提取占位符到 JSON
python3 converting-markdown/scripts/extract_placeholders.py document.html

# 步骤3：AI Agent 生成 SVG 并替换（AI 执行，无需命令）
python3 converting-markdown/scripts/replace_svg.py document.json
```

**⚠️ 重要执行规范：**

- **使用完整路径调用脚本**：避免文件找不到
- **不要使用 cd 切换目录**：保持当前工作目录不变
- **明确输出位置**：HTML 文件生成在 Markdown 文件所在目录

### 调用 Skill 示例

```bash
# 编制售前方案
skill presales-proposal "为 XX 协会编制会员系统建设方案"

# 编制项目规划书
skill internal-project-plan "XX 协会 2026 年度项目规划"
```

---

## ASCII 图标注规范（核心要求）

本项目的一个关键特性是所有 ASCII 图必须标注类型，以支持智能转换为 SVG。

### 必须使用的标注格式

````markdown
```ascii:architecture  # 架构图
```ascii:flowchart     # 流程图
```ascii:ui            # UI 界面图
```ascii:timeline      # 时间线图
```ascii:diagram       # 通用图
```
````

### 为什么必须标注类型？

1. ✅ **保持等宽字体**：确保字符对齐，避免 Markdown 渲染时格式错乱
2. ✅ **智能转换 SVG**：converting-markdown 根据类型选择最优转换策略
3. ✅ **精准识别**：不会把普通文本中的框线字符误认为 ASCII 图
4. ✅ **版本控制友好**：git diff 更清晰，代码块格式更易于比较

### 错误示例（不要这样写）

````markdown
```
┌────────┐
│ 标题   │
└────────┘
```
````

**问题**：没有标注类型，converting-markdown 无法识别，转换时无法生成精美图形

### 正确示例（必须这样写）

````markdown
```ascii:ui
┌────────┐
│ 标题   │
└────────┘
```
````

---

## 核心工作流程

### converting-markdown 智能 ASCII 图转换流程

当用户选择"智能转换 SVG"时，遵循以下 3 步流程：

#### 步骤 1：生成带占位符的 HTML

```bash
AI_SVG_CONVERSION=true python3 converting-markdown/scripts/convert.py document.md --theme purple
```

输出：包含 `AI-SVG-PLACEHOLDER` 标记的 HTML 文件

#### 步骤 2：提取占位符到 JSON

```bash
python3 converting-markdown/scripts/extract_placeholders.py document.html
```

输出：`document.json`，包含所有占位符的原始内容

#### 步骤 3：AI Agent 生成 SVG 并替换

AI Agent 需要：
1. 读取 JSON 文件，获取所有占位符的 `raw_content`
2. 智能理解结构，为每个占位符生成 `svg_code`
3. 保存 JSON 文件
4. 调用替换脚本：`python3 converting-markdown/scripts/replace_svg.py document.json`

**技术参考**：
- SVG/HTML 输出格式规范：`converting-markdown/guides/output-specs.md`
- ASCII 识别和转换技巧：`converting-markdown/guides/ascii-to-svg.md`

### 输出格式规则

| 图形类型 | 输出格式 | 说明 |
|---------|---------|------|
| `architecture` | SVG | 系统架构图，使用方框、箭头、层级 |
| `flowchart` | SVG | 流程图，使用步骤框、连接线 |
| `ui` | **HTML/CSS** | UI 界面图，生成真实可交互界面（⚠️ 不是 SVG） |
| `timeline` | SVG | 时间线图，使用时间轴、节点 |
| `diagram` | SVG | 通用图，根据内容灵活处理 |

### 主题色系

| 主题 | 主色 | 辅助色 | 适用场景 |
|------|------|--------|---------|
| **purple** | #667eea | #764ba2 | 售前方案、商务文档 |
| **blue** | #1890ff | #096dd9 | 技术文档、API 文档 |
| **green** | #52c41a | #389e0d | 内部报告、运营数据 |
| **minimal** | #333333 | #666666 | 学术论文、正式报告 |

---

## 文档编制规范

### presales-proposal（售前方案）

**核心原则**：只回答 4 个核心问题
1. 为什么要做（Why）- 项目背景与建设目标
2. 做什么（What）- 功能方案设计
3. 要花多少钱（How much）- 投资预算
4. 要多久（How long）- 实施周期

**不要包含**：
- ❌ 技术架构、数据库设计、接口设计
- ❌ 投入产出分析、投资回收期
- ❌ 售后服务、质保期、维护计划
- ❌ 具体商品清单/数据清单

**文档风格**：
- ✅ 图文并茂，使用 ASCII 图、表格、流程图
- ✅ 流畅叙述，逻辑连贯
- ✅ 使用引用增强说服力
- ❌ 避免 PPT 式要点清单

### internal-project-plan（内部项目规划）

**核心原则**：表格化为主，简洁明了

**必须包含 8 个章节**：
1. 今年要做的项目表
2. 未来 1-2 年内可以做的项目表
3. 2 年以上长期项目
4. 项目汇总统计
5. 项目优先级建议
6. 实施路径图（ASCII 图）
7. 备注说明
8. **运维服务报价方案**（重点章节）

**运维服务报价方案**：
- 分项阶梯费率（30 万以内、30-80 万、80-150 万、150 万以上）
- 套餐组合（基础版、标准版、高级版、旗舰版）
- AI 系统特殊维护（AI 知识库更新）
- 必须计算今年项目的年度维护费

### 用户配置管理

两个技能都使用 `.claude/user-config.yaml` 管理用户信息：

```yaml
user:
  name: "张三"
  company_name: "某某科技有限公司"
  company_role: "售前产品经理"

last_updated: "2026-02-04"
```

**占位符处理**：
- SKILL.md 中使用 `{{COMPANY_NAME}}` 占位符
- AI Agent 读取配置并全局替换为实际公司名称
- 如果配置不存在，首次使用时询问用户

---

## 重要技术细节

### Python 脚本依赖

- **Python 3.6+**：使用 f-string 语法
- **PyYAML**：主题配置文件解析
- **markdown**：Markdown 转 HTML

### 脚本职责边界

**脚本负责（机械工作）**：
- ✅ 提取占位符到 JSON
- ✅ 替换占位符为 SVG/HTML
- ✅ 文件读写操作
- ❌ 不验证 SVG/HTML 格式（由 AI Agent 负责）

**AI Agent 负责（智能工作）**：
- ✅ 理解 ASCII 图结构
- ✅ 生成 SVG/HTML 代码
- ✅ 验证代码格式正确性

### 验证清单

AI Agent 生成代码后应检查：

**SVG 检查项**：
- [ ] 以 `<svg` 开头，`</svg>` 结尾
- [ ] 包含 `xmlns` 属性
- [ ] 包含 `viewBox` 属性
- [ ] 使用主题色系
- [ ] 包含圆角、阴影等美化效果

**HTML 检查项（UI 类型）**：
- [ ] 使用语义化标签（`div`, `button`, `input` 等）
- [ ] 包含内联样式或 `<style>` 标签
- [ ] 使用主题色系
- [ ] 使用 flexbox 或 grid 布局
- [ ] 包含 hover、focus 等交互效果

---

## 常见错误避免

### 错误 1：未标注 ASCII 图类型

````markdown
❌ 错误：
```
┌────────┐
│ 系统   │
└────────┘
```

✅ 正确：
```ascii:architecture
┌────────┐
│ 系统   │
└────────┘
```
````

### 错误 2：UI 类型使用 SVG

```xml
❌ 错误：UI 应该用 HTML，不用 SVG
<svg>
  <rect>按钮</rect>
</svg>

✅ 正确：生成真实的 HTML 界面
<div style="background: {primary};">
  <button>按钮</button>
</div>
```

### 错误 3：使用 cd 切换目录

```bash
❌ 错误：切换目录（会改变工作目录）
cd /path/to/skill && python3 scripts/convert.py document.md

✅ 正确：使用完整路径
python3 /path/to/skill/scripts/convert.py /path/to/document.md --theme blue
```

---

## 优秀案例参考

### 售前方案案例

- `./售前/会员积分商城建设方案.md`
- `./售前/官网及业务系统升级方案.md`

**特点**：
- ✅ 结构清晰，四大板块完整
- ✅ 图文并茂，使用 ASCII 图、表格、流程图
- ✅ 内容流畅，段落式叙述
- ✅ 所有 ASCII 图都标注了类型
- ✅ 无技术细节、无投入产出分析、无售后服务

### 项目规划案例

- `./协会要开发的项目.md`

**特点**：
- ✅ 8 个章节完整
- ✅ 表格化呈现，简洁明了
- ✅ 统一维护费用说明完整（阶梯费率 + 套餐组合）
- ✅ 实施路径图清晰

---

## 设计模式参考

本项目提炼了 4 种核心设计模式，可供编写新的 SKILL 时参考：

### 模式 1：职责分离（脚本 + AI 协作）

**适用场景**：需要调用外部工具或脚本

**实现要点**：
- 脚本负责：文件操作、格式转换、占位符处理
- AI 负责：决策、理解结构、生成代码
- 通信方式：命令行参数、环境变量、JSON 文件

**案例**：converting-markdown
```bash
# AI 决策后调用脚本
AI_SVG_CONVERSION=true python3 scripts/convert.py document.md --theme purple

# 脚本输出中间结果
python3 scripts/extract_placeholders.py document.html

# AI 生成代码后调用脚本替换
python3 scripts/replace_svg.py document.json
```

### 模式 2：按需加载（SKILL.md + guides）

**适用场景**：复杂业务逻辑，需要分层组织

**实现要点**：
- SKILL.md：核心流程、快速开始、交互步骤
- guides/：技术细节、代码示例、验证清单
- 明确提示："AI 只在需要时读取 guides"

**案例**：converting-markdown
```
SKILL.md:
  ## 技术指南（按需读取）
  - 📄 输出格式和代码要求：见 `guides/output-specs.md`
  - 🎨 ASCII识别和转换技巧：见 `guides/ascii-to-svg.md`

  **AI Agent 只在需要生成代码时才读取 guides。**
```

### 模式 3：占位符系统（动态内容替换）

**适用场景**：需要用户个性化配置

**实现要点**：
- SKILL.md 使用 `{{VARIABLE}}` 占位符
- CONFIG.yaml 存储用户配置
- AI Agent 读取配置并全局替换

**案例**：presales-proposal
```yaml
# .claude/user-config.yaml
user:
  company_name: "某某科技有限公司"

# SKILL.md
**编制单位：** {{COMPANY_NAME}}

# AI Agent 执行时替换
**编制单位：** 某某科技有限公司
```

### 模式 4：纯文档 SKILL（无外部依赖）

**适用场景**：可以完全由 AI Agent 执行

**实现要点**：
- 完整的规范和检查清单
- 无需调用外部脚本
- 使用"正确/错误"示例对比

**案例**：presales-proposal、internal-project-plan
```
SKILL.md:
  ## 核心原则
  ## 文档结构要求
  ## 写作规范
  ## 检查清单

  （所有逻辑由 AI Agent 理解和执行）
```

### 选择设计模式的决策树

```
需要调用外部工具？
├── 是 → 使用模式 1（职责分离）
└── 否
    ├── 需要用户配置？
    │   ├── 是 → 使用模式 3（占位符系统）
    │   └── 否
    │       ├── 有复杂技术细节？
    │       │   ├── 是 → 使用模式 2（按需加载）
    │       │   └── 否 → 使用模式 4（纯文档）
    │       └── 可组合使用多种模式
```

---

## SKILL 质量标准

高质量的 SKILL 应满足以下标准：

### 可用性
- ✅ 首次使用能成功运行
- ✅ 错误提示清晰友好
- ✅ 有明确的输出反馈

### 可维护性
- ✅ 结构清晰，易于理解
- ✅ 职责分离明确
- ✅ 检查清单完整

### 可扩展性
- ✅ 易于添加新功能
- ✅ 配置与代码分离
- ✅ 支持平台兼容

### 可学习性
- ✅ 有充分的示例
- ✅ 使用对比示例（正确/错误）
- ✅ 技术细节按需加载
