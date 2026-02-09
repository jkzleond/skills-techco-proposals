#!/usr/bin/env python3
"""
售前方案模板生成脚本

用法：
    python3 create_proposal_template.py "项目名称" [output-file]

功能：
    生成标准的售前方案框架
    包含正确的标题层级
    预填充占位符
"""

import sys
from datetime import datetime
from pathlib import Path


def get_template(project_name, issuer_name="{{COMPANY_NAME}}"):
    """生成方案模板"""

    current_date = datetime.now()
    date_str = f"{current_date.year}年{current_date.month}月"

    template = f"""# {project_name}建设方案

**编制单位：** {issuer_name}
**编制日期：** {date_str}
**版本号：** v1.0

---

## 目录

- [一、项目背景与建设目标](#一项目背景与建设目标)
- [二、功能方案设计](#二功能方案设计)
- [三、投资预算](#三投资预算)
- [四、实施周期](#四实施周期)

---

## 一、项目背景与建设目标

### 1.1 现状分析

[描述当前情况和存在的问题，使用段落式叙述]


### 1.2 会员/客户的真实反馈

[使用引用展示真实反馈，增强说服力]

> "会员反馈内容1"

> "会员反馈内容2"


### 1.3 解决方案

[概述解决方案思路，使用流程图展示]

```ascii:flowchart
[在此处绘制流程图]
```


### 1.4 建设目标

[用表格展示建设目标]

| 目标类别 | 具体目标 | 预期效果 |
|---------|---------|---------|
| [类别1] | [目标1] | [效果1] |
| [类别2] | [目标2] | [效果2] |


---

## 二、功能方案设计

### 2.1 系统定位

[说明系统是什么、不是什么]


### 2.2 系统架构

[用架构图展示系统结构]

```ascii:architecture
[在此处绘制系统架构图]
```


### 2.3 功能设计

#### 2.3.1 会员端功能

[图文并茂描述会员端功能]

| 功能模块 | 功能说明 | 用户价值 |
|---------|---------|---------|
| [模块1] | [说明] | [价值] |
| [模块2] | [说明] | [价值] |


#### 2.3.2 管理端功能

[图文并茂描述管理端功能]

| 功能模块 | 功能说明 | 管理价值 |
|---------|---------|---------|
| [模块1] | [说明] | [价值] |
| [模块2] | [说明] | [价值] |


### 2.4 与现有系统的关系

[用架构图说明新系统与现有系统的关系]

```ascii:architecture
[在此处绘制集成架构图]
```


---

## 三、投资预算

### 3.1 开发费用

**开发费用总计：人民币___.___元整（¥___,___.__）**

### 3.2 费用构成

本费用包含以下完整功能模块的开发：

| 功能模块 | 包含内容 | 说明 |
|---------|---------|------|
| [模块1] | [功能1、功能2...] | [简要说明] |
| [模块2] | [功能1、功能2...] | [简要说明] |

### 3.3 费用包含内容

整个项目按以下阶段实施：

#### 需求分析与设计阶段
- [具体工作内容1]
- [具体工作内容2]

#### 功能开发阶段
- **[模块1名称]开发**
  - [功能1]
  - [功能2]
- **[模块2名称]开发**
  - [功能1]
  - [功能2]

#### 测试与上线阶段
- [具体工作内容]

### 3.4 费用不包含内容

| 费用项 | 说明 | 预估费用 |
|--------|------|----------|
| [费用1] | [说明] | 约[金额] |
| [费用2] | [说明] | 约[金额] |

### 3.5 付款方式

[用流程图展示付款方式]

```ascii:flowchart
[在此处绘制付款流程图]
```


---

## 四、实施周期

### 4.1 开发周期

**总开发周期：约_周**

### 4.2 实施阶段

#### 阶段1：需求分析与设计（_周）
- [工作内容1]
- [工作内容2]

**阶段产出**：
- [产出物1]
- [产出物2]


#### 阶段2：功能开发（_周）
- [工作内容1]
- [工作内容2]

**阶段产出**：
- [产出物1]
- [产出物2]


#### 阶段3：测试与上线（_周）
- [工作内容1]
- [工作内容2]

**阶段产出**：
- [产出物1]
- [产出物2]


### 4.3 交付物清单

#### 文档交付物
- [文档1]
- [文档2]

#### 系统交付物
- [系统1]
- [系统2]

#### 培训交付物
- [培训内容1]
- [培训内容2]


---

**提示**：
- 编制完成后，使用 `python3 scripts/validate_proposal.py [file.md]` 验证方案
- 使用 `python3 converting-markdown/scripts/check_ascii_blocks.py [file.md]` 检查 ASCII 图标注
- 详细规范见 `references/` 目录下的参考文档
"""

    return template


def main():
    if len(sys.argv) < 2:
        print("用法: python3 create_proposal_template.py <项目名称> [output-file]")
        print()
        print("示例:")
        print('  python3 create_proposal_template.py "会员积分商城" proposal.md')
        print('  python3 create_proposal_template.py "官网升级"')
        sys.exit(1)

    project_name = sys.argv[1]

    # 确定输出文件名
    if len(sys.argv) >= 3:
        output_file = Path(sys.argv[2])
    else:
        # 默认使用项目名称作为文件名
        output_file = Path(f"{project_name}建设方案.md")

    # 检查文件是否已存在
    if output_file.exists():
        print(f"警告: 文件已存在: {output_file}")
        response = input("是否覆盖？(y/N): ")
        if response.lower() != 'y':
            print("已取消")
            sys.exit(0)

    # 生成模板
    template = get_template(project_name)

    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)

    print(f"✓ 方案模板已生成: {output_file}")
    print()
    print("下一步:")
    print(f"  1. 编辑文件: {output_file}")
    print(f"  2. 验证方案: python3 scripts/validate_proposal.py {output_file}")
    print(f"  3. 检查 ASCII 图: python3 converting-markdown/scripts/check_ascii_blocks.py {output_file}")


if __name__ == '__main__':
    main()
