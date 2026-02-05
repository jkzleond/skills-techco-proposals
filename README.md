# Skills for Tech Company Proposals

科技公司方案编制专用 Skills 集合，提升 AI 辅助方案编制效率。

## 🎯 包含的 Skills

### 1. converting-markdown
将 Markdown 文档转换为美观的 HTML，支持多主题、响应式设计、智能 SVG 图形转换。

- **用途**：方案文档转 HTML（供领导查阅）
- **特点**：
  - 多主题支持（purple/blue/green/minimal）
  - ASCII 图智能转换 SVG
  - 响应式设计（PC/平板/手机）
  - 打印优化
- **文档**：[converting-markdown/SKILL.md](converting-markdown/SKILL.md)
- **技术指南**：
  - [输出规范](converting-markdown/guides/output-specs.md)
  - [ASCII图转换技巧](converting-markdown/guides/ascii-to-svg.md)

### 2. presales-proposal
编制售前方案、汇报方案、功能建议方案。

- **用途**：售前产品经理编制客户方案
- **特点**：
  - 图文并茂（ASCII图、表格、流程图）
  - 四大核心板块（背景/功能/预算/周期）
  - 严格遵循"回答4个核心问题"
  - ASCII图类型标注规范（100%标注率）
- **文档**：[presales-proposal/SKILL.md](presales-proposal/SKILL.md)
- **适用场景**：客户询问功能、给领导汇报、编制方案文档

### 3. internal-project-plan
编制内部项目规划书，规划多年度项目路线图和报价。

- **用途**：规划客户多年度项目、报价参考
- **特点**：
  - 项目清单（分年度表格）
  - 优先级建议
  - 实施路径图（ASCII图）
  - 运维服务报价方案（分项阶梯费率 + 套餐组合）
- **文档**：[internal-project-plan/SKILL.md](internal-project-plan/SKILL.md)
- **适用场景**：多年度项目规划、统一维护费用方案

## 🚀 快速开始

### 方法1：符号链接（推荐）

将本仓库的 skills 链接到你的项目：

```bash
# 1. 克隆本仓库
git clone https://github.com/yourname/skills-techco-proposals.git ~/common/www/ai_coding/skills-techco-proposals

# 2. 在你的项目中创建符号链接
cd your-project/.claude/skills
ln -s ~/common/www/ai_coding/skills-techco-proposals/converting-markdown
ln -s ~/common/www/ai_coding/skills-techco-proposals/presales-proposal
ln -s ~/common/www/ai_coding/skills-techco-proposals/internal-project-plan
```

### 方法2：Git Submodule

```bash
cd your-project
git submodule add https://github.com/yourname/skills-techco-proposals.git .claude/skills/techco-proposals
```

## 📖 使用示例

```bash
# 转换 Markdown 为 HTML（purple主题）
python3 ~/common/www/ai_coding/skills-techco-proposals/converting-markdown/scripts/convert.py \
  售前/会员积分商城建设方案.md --theme purple

# 编制售前方案
skill presales-proposal "为XX协会编制会员系统建设方案"

# 编制项目规划书
skill internal-project-plan "XX协会2026年度项目规划"
```

## 🛠️ 技术依赖

### converting-markdown
- Python 3.6+
- PyYAML
- markdown

```bash
pip3 install pyyaml markdown
```

### presales-proposal / internal-project-plan
- 无依赖（纯 SKILL 文档）

## 📂 目录结构

```
skills-techco-proposals/
├── README.md                          # 本文档
├── LICENSE                            # MIT 许可证
│
├── converting-markdown/               # Markdown转HTML技能
│   ├── SKILL.md
│   ├── guides/
│   │   ├── output-specs.md            # 输出规范
│   │   └── ascii-to-svg.md            # ASCII图转换技巧
│   ├── templates/                     # 主题配置
│   │   ├── purple.yaml
│   │   ├── blue.yaml
│   │   ├── green.yaml
│   │   └── minimal.yaml
│   └── scripts/
│       ├── convert.py                 # 主转换脚本
│       ├── themes.py                  # 主题加载工具
│       ├── extract_placeholders.py    # 提取占位符
│       └── replace_svg.py             # 替换SVG
│
├── presales-proposal/                 # 售前方案编制技能
│   └── SKILL.md
│
└── internal-project-plan/             # 内部项目规划技能
    └── SKILL.md
```

## 🎨 设计理念

### 核心原则

1. **职责分离**：脚本做机械工作，AI做智能工作
2. **单一定义源**：SKILL.md 定义流程，guides 提供技术细节
3. **按需加载**：AI 只在需要时读取 guides
4. **平台无关**：兼容 Claude、ChatGPT、Gemini 等所有支持 SKILL 格式的 AI Agent

### ASCII 图规范

所有 ASCII 图**必须标注类型**：

````markdown
```ascii:architecture  # 架构图
```ascii:flowchart     # 流程图
```ascii:ui            # UI界面图
```ascii:timeline      # 时间线图
```ascii:diagram       # 通用图
```
````

**为什么要标注类型？**
1. ✅ 保持等宽字体，确保字符对齐
2. ✅ 智能转换 SVG（converting-markdown 根据类型选择最优策略）
3. ✅ 精准识别，不会误判普通文本
4. ✅ 版本控制友好，git diff 更清晰

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 贡献流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

### 代码规范

- SKILL.md 文档遵循[项目规范](CONTRIBUTING.md)
- Python 代码遵循 PEP 8
- 提交信息使用清晰、描述性的语言

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🔗 相关资源

- [Claude Code 官方文档](https://docs.anthropic.com/claude-code)
- [SKILL 格式规范](https://docs.anthropic.com/claude-code/skills)
- [Markdown 转 HTML 最佳实践](converting-markdown/SKILL.md)

## 📮 联系方式

- 问题反馈：[GitHub Issues](https://github.com/yourname/skills-techco-proposals/issues)
- 邮箱：your-email@example.com

---

**Made with ❤️ for Tech Companies**
