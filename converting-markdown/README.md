# Converting Markdown to HTML - Skill

支持多主题的 Markdown 转 HTML 工具。

## 🎨 可用主题

| 主题 | 颜色 | 适用场景 |
|------|------|---------|
| **purple** | #667eea → #764ba2 | 售前方案、商务文档 |
| **blue** | #1890ff → #096dd9 | 技术文档、API 文档 |
| **green** | #52c41a → #389e0d | 内部报告、运营数据 |
| **minimal** | 灰度系 | 学术论文、正式报告 |

## 🚀 使用方法

本脚本由 AI Agent 调用，不接受交互式输入。

```bash
# 列出所有主题
python3 scripts/convert.py --list-themes

# 指定文件和主题
python3 scripts/convert.py document.md --theme blue
python3 scripts/convert.py document.md --theme green
python3 scripts/convert.py document.md --theme minimal
```

### 安装依赖

```bash
# 必需依赖
pip3 install pyyaml markdown
```

## ➕ 添加新主题

只需在 `templates/` 目录创建新的 `.yaml` 文件：

```bash
# 1. 复制现有主题
cp templates/purple.yaml templates/mytheme.yaml

# 2. 编辑配置文件
vim templates/mytheme.yaml

# 3. 立即使用
python3 scripts/convert.py document.md --theme mytheme
```

## 📁 目录结构

```
converting-markdown/
├── SKILL.md              # 技能说明
├── README.md             # 本文件
├── LICENSE.txt           # MIT 许可证
├── templates/            # 主题配置
│   ├── purple.yaml
│   ├── blue.yaml
│   ├── green.yaml
│   └── minimal.yaml
└── scripts/
    ├── convert.py        # 主转换脚本
    └── themes.py         # 主题加载工具
```

## ✨ 特性

- ✅ 多主题支持（YAML 配置）
- ✅ 响应式设计
- ✅ 打印优化
- ✅ **智能段落合并**（使用专业markdown库）
- ✅ **ASCII图清晰显示**（等宽字体，保留原始结构）
- ✅ 零外部依赖（仅 markdown + PyYAML）
- ✅ 由 AI Agent 调用，使用 `AskUserQuestion` 与用户交互

## 📝 主题配置示例

```yaml
name: "紫色渐变主题"
description: "专业售前方案"

colors:
  primary: "#667eea"
  secondary: "#764ba2"
  background: "#ffffff"
  gradient_start: "#667eea"
  gradient_end: "#764ba2"

styles:
  border_radius: 16
  box_shadow: "0 20px 60px rgba(0, 0, 0, 0.3)"
```

完整配置参考 `templates/` 目录下的现有主题文件。
