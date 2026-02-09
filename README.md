# AI Agent SKILL 制作研究项目

> 研究 AI Agent 的 SKILL 格式、设计模式和最佳实践，通过实际案例探索如何编写高质量的 SKILL 文档。

## 🎯 项目目的

本项目是一个**关于 SKILL 制作的研究项目**，旨在探索和总结 AI Agent SKILL 的编写方法、设计模式和最佳实践。通过五个完整的实际案例，展示如何将复杂的业务流程和专业知识转化为可被 AI Agent 理解和执行的 SKILL 文档。

### 可以学到什么

- ✅ **SKILL 格式规范**：如何编写符合规范的 SKILL.md 文档
- ✅ **职责分离设计**：如何划分"脚本机械工作"和"AI 智能工作"
- ✅ **交互流程设计**：如何设计 AI Agent 与用户的交互流程
- ✅ **占位符管理**：如何处理用户配置和动态内容
- ✅ **按需加载技术**：如何组织 SKILL.md 和 guides，提高 AI 效率
- ✅ **跨平台兼容**：如何编写兼容 Claude、ChatGPT、Gemini 等平台的 SKILL

---

## 📚 研究案例

### 案例 1：converting-markdown（复杂交互流程）

**研究点**：如何设计多步骤交互流程和脚本协作

- **SKILL.md**：定义完整的 AI 交互流程（选择文件 → 选择主题 → ASCII 图处理方式 → 验证）
- **guides/**：按需加载的技术细节（输出规范、转换技巧）
- **scripts/**：Python 脚本负责机械工作（转换、提取、替换）
- **职责分离**：
  - 脚本：文件操作、占位符提取、内容替换
  - AI Agent：理解 ASCII 图结构、生成 SVG/HTML 代码

**关键设计模式**：
```
用户 → AI Agent（决策） → 脚本（执行） → AI Agent（生成代码） → 脚本（替换）
```

### 案例 2：presales-proposal（纯文档 SKILL）

**研究点**：如何将专业知识转化为 SKILL 文档

- **SKILL.md**：完整的售前方案编制规范（核心原则、文档结构、写作规范、检查清单）
- **CONFIG.yaml**：用户配置管理（公司名称、角色定位）
- **占位符系统**：使用 `{{COMPANY_NAME}}` 占位符，AI Agent 运行时替换

**关键设计模式**：
```
用户配置 + SKILL 规范 → AI Agent 生成文档 → 输出符合规范的方案
```

### 案例 3：internal-project-plan（复杂计算 SKILL）

**研究点**：如何让 AI Agent 执行复杂的计算和逻辑判断

- **SKILL.md**：详细的项目规划规范（8 个章节、阶梯费率、套餐组合）
- **计算逻辑**：AI Agent 根据项目金额自动计算各档套餐维护费
- **决策支持**：优先级建议、实施路径规划

**关键设计模式**：
```
项目数据 → AI Agent（计算 + 决策） → 生成规划书 + 报价方案
```

### 案例 4：svg-beautifier（视觉提升 SKILL）

**研究点**：如何让 AI Agent 像设计师一样处理视觉资源

- **SKILL.md**：定义现代 UI 风格规范和美化流程
- **guides/**：分图形类型的详细视觉准则（图表 vs 流程图）
- **设计决策**：通过 `CONFIG.yaml` 动态注入品牌色

**关键设计模式**：
```
基础/ASCII 图表 → AI Agent（视觉理解 + 风格注入） → 高保真 SVG 图表
```

### 案例 5：fast-prototype（符合 skill-creator 标准）

**研究点**：如何让 AI Agent 从需求描述生成完整的可运行原型和文档

- **SKILL.md**：精简的核心工作流（134 行，符合 skill-creator 标准）
- **references/**：按需加载的技术参考文档（5 个文档，共 1641 行）
- **技术栈**：Vue3 + Tailwind + Element Plus
- **渐进式披露**：三级加载系统（Metadata → SKILL.md → references/）

**符合 skill-creator 标准**：
- ✅ SKILL.md < 500 行
- ✅ 使用 references/ 目录
- ✅ 无 README.md
- ✅ 无 CONFIG.yaml
- ✅ 无多余文档

**关键设计模式**：
```
需求描述 → AI Agent（结构化PRD生成） → 用户确认 → AI Agent（原型+文档生成）
```

**核心特点**：
- 结构化 PRD：Mermaid（流程）+ ASCII（布局）+ 表格（功能）
- 可运行原型：Vue3 + Tailwind + Element Plus，完整交互逻辑
- 专业文档：标准 PRD、界面设计、前后端技术文档

---

## 🏗️ SKILL 设计模式

### 模式 1：职责分离（脚本 + AI 协作）

适用于需要调用外部工具或脚本的场景。

**架构**：
```
┌─────────────┐    决策     ┌─────────────┐    执行     ┌──────────────┐
│  AI Agent   │ ────────→ │   Python    │ ────────→ │  文件操作    │
│             │ ←────────  │   脚本      │ ←────────  │   结果输出   │
└─────────────┘    返回     └─────────────┘    状态     └──────────────┘
```

**实现示例**：converting-markdown
- AI Agent：询问用户选择主题、处理 ASCII 图、生成 SVG 代码
- 脚本：转换 Markdown、提取占位符、替换 SVG

### 模式 2：按需加载（SKILL.md + guides）

适用于复杂业务逻辑，需要分层组织的场景。

**架构**：
```
SKILL.md（主流程）
├── 快速开始
├── 交互流程
└── 📖 详细技术指南（guides/）
    ├── guide-1.md（AI 按需读取）
    ├── guide-2.md（AI 按需读取）
    └── guide-3.md（AI 按需读取）
```

**实现示例**：converting-markdown
- SKILL.md：定义完整交互流程
- guides/output-specs.md：SVG/HTML 输出格式规范
- guides/ascii-to-svg.md：ASCII 识别和转换技巧

**优点**：
- ✅ 减少 AI 的上下文负担
- ✅ 提高 SKILL.md 的可读性
- ✅ 技术细节可以独立更新

### 模式 3：占位符系统（动态内容替换）

适用于需要用户个性化配置的场景。

**架构**：
```
SKILL.md（定义占位符）
        ↓
.claude/user-config.yaml（用户配置）
        ↓
AI Agent（读取配置 → 替换占位符 → 生成文档）
```

**实现示例**：presales-proposal、internal-project-plan
- SKILL.md：使用 `{{COMPANY_NAME}}` 占位符
- CONFIG.yaml：存储用户的公司名称、角色等
- AI Agent：首次使用时询问，后续自动读取

### 模式 4：纯文档 SKILL（无外部依赖）

适用于可以完全由 AI Agent 执行的场景。

**架构**：
```
SKILL.md（完整规范）
├── 角色定位
├── 核心原则
├── 文档结构要求
├── 写作规范
└── 检查清单
        ↓
AI Agent（理解规范 → 生成文档）
```

**实现示例**：presales-proposal、internal-project-plan
- 无需调用外部脚本
- 所有逻辑由 AI Agent 执行
- 适用于文档生成、方案编制等场景

---

## 📖 SKILL 编写最佳实践

### 1. 明确的交互流程

**❌ 不好的写法**：
```markdown
## 使用方法

调用脚本转换文件。
```

**✅ 好的写法**：
```markdown
## AI 交互流程

### 步骤1：选择 Markdown 文件
使用 `AskUserQuestion` 工具让用户选择文件。

### 步骤2：选择主题模板
使用 `AskUserQuestion` 工具展示主题选项：
- purple - 紫色渐变（售前方案）
- blue - 蓝色科技（技术文档）

### 步骤3：执行转换
调用脚本：`python3 scripts/convert.py [file] --theme [theme]`

### 步骤4：告知用户
```
✅ 转换完成！
📄 输出文件：/path/to/document.html
```
```

### 2. 职责分离清晰

**❌ 不好的写法**：
```markdown
让 AI 生成 SVG 图形，然后替换到 HTML 中。
```

**✅ 好的写法**：
```markdown
**职责分工：**
- **脚本负责**（机械工作）：提取、占位符替换、文件读写
- **AI Agent负责**（智能工作）：理解结构、生成SVG代码

**脚本不验证**SVG/HTML格式，格式验证由 AI Agent 在生成代码时自行负责。
```

### 3. 按需加载技术细节

**❌ 不好的写法**（所有内容都在 SKILL.md）：
```markdown
## SKILL

[20 页的详细技术规范...]
```

**✅ 好的写法**（分层组织）：
```markdown
## SKILL

## AI 交互流程
[核心流程...]

## 技术指南（按需读取）
- 📄 输出格式和代码要求：见 `guides/output-specs.md`
- 🎨 ASCII识别和转换技巧：见 `guides/ascii-to-svg.md`

**AI Agent 只在需要生成代码时才读取 guides。**
```

### 4. 检查清单验证

在 SKILL 末尾添加检查清单，帮助 AI Agent 自我验证：

```markdown
## 检查清单

### 内容检查
- [ ] 四大核心板块完整
- [ ] ASCII 图都标注了类型
- [ ] 使用了主题色系

### 格式检查
- [ ] SVG 以 `<svg` 开头
- [ ] HTML 使用语义化标签

### 语言检查
- [ ] 流畅叙述，避免清单式
- [ ] 使用具体示例
```

### 5. 错误示例对比

使用"正确/错误"对比，帮助 AI Agent 理解要求：

```markdown
### 错误示例

❌ **错误**：没有标注类型
```
┌────────┐
│ 系统   │
└────────┘
```

✅ **正确**：标注类型
````markdown
```ascii:architecture
┌────────┐
│ 系统   │
└────────┘
```
````
```

---

## 🛠️ 技术栈

### SKILL 编写
- **格式**：Markdown + YAML Front Matter
- **配置管理**：YAML
- **占位符**：`{{VARIABLE}}` 格式

### Python 脚本（可选）
- **版本**：Python 3.6+
- **依赖**：PyYAML、markdown（按需）
- **职责**：文件操作、格式转换、占位符处理

---

## 📂 目录结构

```
skills-techco-proposals/
├── CLAUDE.md                          # Claude Code 工作指南
├── README.md                          # 本文档
├── LICENSE                            # MIT 许可证
│
├── converting-markdown/               # 案例1：脚本+AI协作
│   ├── SKILL.md                       # 主交互流程
│   ├── guides/                        # 按需加载的技术指南
│   │   ├── output-specs.md            # 输出格式规范
│   │   └── ascii-to-svg.md            # ASCII转换技巧
│   ├── templates/                     # 配置文件（YAML）
│   └── scripts/                       # Python脚本
│
├── presales-proposal/                 # 案例2：纯文档SKILL
│   ├── SKILL.md                       # 完整编制规范
│   └── CONFIG.yaml                    # 用户配置
│
├── internal-project-plan/             # 案例3：复杂计算SKILL
│   ├── SKILL.md                       # 规划规范+计算逻辑
│   └── CONFIG.yaml                    # 用户配置
│
├── svg-beautifier/                    # 案例4：视觉提升SKILL
│   ├── SKILL.md                       # 美化规范与流程
│   ├── CONFIG.yaml                    # 视觉配置（品牌色等）
│   └── guides/                        # 详细视觉指南
│       ├── chart-styles.md            # 数据图表风格
│       └── flowchart-patterns.md      # 流程架构风格
│
└── fast-prototype/                   # 案例5：需求到原型SKILL（符合skill-creator标准）
    ├── SKILL.md                       # 核心工作流（134行）
    ├── assets/                        # 资源目录
    └── references/                    # 按需加载的参考文档
        ├── component-styles.md        # 组件样式指南
        ├── design-specs.md            # 界面设计规范
        ├── prd-template.md            # PRD文档模板
        ├── frontend-tech.md           # 前端技术文档模板
        └── backend-tech.md            # 后端技术文档模板
```

---

## 🚀 快速开始

### 安装依赖

```bash
# 仅 converting-markdown 需要 Python 依赖
pip3 install pyyaml markdown
```

### 使用案例

```bash
# 案例1：converting-markdown（脚本+AI协作）
python3 converting-markdown/scripts/convert.py document.md --theme purple

# 案例2：presales-proposal（纯文档SKILL）
skill presales-proposal "为XX协会编制会员系统建设方案"

# 案例3：internal-project-plan（复杂计算）
skill internal-project-plan "XX协会2026年度项目规划"

# 案例5：fast-prototype（需求到原型）
skill fast-prototype "为一个客户管理系统设计原型"
```

---

## 🎓 学习路径

### 初学者：理解 SKILL 基本结构

1. 阅读 `presales-proposal/SKILL.md`
   - 学习基本的 SKILL 格式
   - 理解角色定位和核心原则
   - 掌握占位符系统

2. 阅读 `internal-project-plan/SKILL.md`
   - 学习如何编写复杂的业务逻辑
   - 理解如何让 AI Agent 执行计算

### 进阶：设计交互流程

3. 阅读 `converting-markdown/SKILL.md`
   - 学习多步骤交互流程设计
   - 理解脚本与 AI 协作模式

4. 阅读 `converting-markdown/guides/`
   - 学习按需加载技术
   - 理解如何分层组织内容

### 高级：自定义 SKILL

5. 参考 5 个案例的结构和模式
6. 根据自己的需求编写 SKILL
7. 使用检查清单验证质量

### 专家：全流程工作流设计

6. 阅读 `fast-prototype/SKILL.md`
   - 学习 5 阶段工作流设计
   - 理解如何从需求到原型到文档
   - 掌握符合 skill-creator 标准的渐进式披露设计

---

## 🔍 设计决策记录

### 为什么使用 ASCII 图标注类型？

**问题**：如何让 AI Agent 识别 ASCII 图并智能转换？

**解决方案**：要求用户标注类型（` ```ascii:architecture ` `）

**优点**：
- ✅ 保持等宽字体，确保字符对齐
- ✅ AI Agent 可以根据类型选择最优转换策略
- ✅ 不会误判普通文本中的框线字符
- ✅ 版本控制友好，git diff 更清晰

**参考**：[ASCII 图规范](#ascii-图规范)

### 为什么使用 guides/ 按需加载？

**问题**：如何减少 AI 的上下文负担？

**解决方案**：将技术细节放在 guides/ 目录，AI 只在需要时读取

**优点**：
- ✅ SKILL.md 保持简洁，聚焦核心流程
- ✅ 技术细节可以独立更新
- ✅ 减少 AI 的 token 消耗

**参考**：[按需加载模式](#模式-2按需加载skillmd--guides)

### 为什么职责要分离？

**问题**：如何避免 AI Agent 做不擅长的机械工作？

**解决方案**：脚本负责文件操作，AI 负责智能决策

**优点**：
- ✅ 稳定可靠：脚本处理文件操作，不会出错
- ✅ 可追溯：中间结果保存为 JSON
- ✅ 职责清晰：AI 专注于理解和生成

**参考**：[职责分离模式](#模式-1职责分离脚本--ai-协作)

---

## 🤝 贡献指南

欢迎贡献你的 SKILL 设计经验和案例！

### 贡献类型

- 📝 新的 SKILL 设计模式
- 🔍 最佳实践案例
- 🐛 Bug 修复和改进
- 📖 文档完善

### 贡献流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-pattern`)
3. 提交更改 (`git commit -m 'Add: 新的设计模式'`)
4. 推送到分支 (`git push origin feature/amazing-pattern`)
5. 开启 Pull Request

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 🔗 相关资源

- [Claude Code 官方文档](https://docs.anthropic.com/claude-code)
- [SKILL 格式规范](https://docs.anthropic.com/claude-code/skills)
- [CLAUDE.md - 工作指南](CLAUDE.md)

---

**Made with ❤️ for AI Agent SKILL Makers**
