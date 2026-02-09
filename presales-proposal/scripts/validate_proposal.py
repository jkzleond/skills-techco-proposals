#!/usr/bin/env python3
"""
售前方案验证脚本

用法：
    python3 validate_proposal.py document.md

功能：
    验证售前方案是否符合规范要求
    - 检查四大核心板块是否完整
    - 检查是否包含禁止内容
    - 检查 ASCII 图标注
    - 生成验证报告
"""

import re
import sys
from pathlib import Path


class ProposalValidator:
    """售前方案验证器"""

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.content = ""
        self.issues = []
        self.warnings = []

    def load_file(self):
        """加载文件内容"""
        if not self.file_path.exists():
            self.issues.append(f"文件不存在: {self.file_path}")
            return False

        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.content = f.read()

        return True

    def check_four_sections(self):
        """检查四大核心板块"""
        required_sections = {
            "项目背景与建设目标": "一、项目背景与建设目标",
            "功能方案设计": "二、功能方案设计",
            "投资预算": "三、投资预算",
            "实施周期": "四、实施周期",
        }

        for name, pattern in required_sections.items():
            if pattern not in self.content:
                self.issues.append(f"缺少核心板块: {name}")
            else:
                print(f"✓ 核心板块存在: {name}")

    def check_forbidden_content(self):
        """检查是否包含禁止内容"""
        forbidden_items = [
            "技术架构设计",
            "数据库设计",
            "接口设计",
            "技术选型",
            "投入产出分析",
            "投资回收期",
            "售后服务",
            "质保期",
            "维护计划",
            "附录",
        ]

        found_forbidden = []
        for item in forbidden_items:
            # 简单的关键词检查
            if item in self.content:
                found_forbidden.append(item)

        if found_forbidden:
            self.warnings.append(
                f"可能包含禁止内容: {', '.join(found_forbidden)}\n"
                "  请确认这些内容是否真的需要（某些情况可能合理）"
            )

    def check_issuer_info(self):
        """检查编制单位信息"""
        if "{{COMPANY_NAME}}" in self.content:
            self.warnings.append("文档中包含占位符 {{COMPANY_NAME}}，请替换为实际公司名称")
        elif "**编制单位：**" not in self.content:
            self.warnings.append("缺少编制单位信息")

    def check_price_format(self):
        """检查价格格式"""
        # 检查是否有明确的价格数字
        price_pattern = r'人民币[零一二三四五六七八九十百千万亿壹贰叁肆伍陆柒捌玖拾佰仟万亿元整]+\(¥[\d,]+\.?\d*\)'
        if not re.search(price_pattern, self.content):
            self.issues.append("缺少明确的价格信息（中文大写 + 阿拉伯数字）")

    def check_timeline(self):
        """检查实施周期"""
        # 检查是否有周期信息
        if "周" not in self.content and "月" not in self.content:
            self.issues.append("缺少实施周期信息（周/月）")

    def check_ascii_blocks(self):
        """检查 ASCII 图标注"""
        # 检查未标注的代码块
        code_block_pattern = re.compile(r'```([^`\n]*)\n([^`]+)```', re.DOTALL)
        blocks = code_block_pattern.finditer(self.content)

        box_chars = set('┌─│└┘┐┬┼┴├┤┤┘┌┐└─│╭╮╰╯═║╗╚╝╔═')
        unlabeled_blocks = []

        for block in blocks:
            lang = block.group(1)
            code = block.group(2)

            # 只检查包含框线字符的代码块
            if any(char in box_chars for char in code):
                start_pos = block.start()
                line_num = self.content[:start_pos].count('\n') + 1

                if not lang.startswith('ascii:'):
                    unlabeled_blocks.append((line_num, lang))

        if unlabeled_blocks:
            for line_num, lang in unlabeled_blocks:
                self.warnings.append(
                    f"Line {line_num}: ASCII 图未标注类型 (当前: '{lang}')"
                )

    def validate(self):
        """执行所有验证"""
        print("=" * 60)
        print("售前方案验证")
        print("=" * 60)
        print()

        # 加载文件
        if not self.load_file():
            return False

        # 执行各项检查
        print("检查核心板块...")
        self.check_four_sections()
        print()

        print("检查禁止内容...")
        self.check_forbidden_content()
        print()

        print("检查编制单位信息...")
        self.check_issuer_info()
        print()

        print("检查价格格式...")
        self.check_price_format()
        print()

        print("检查实施周期...")
        self.check_timeline()
        print()

        print("检查 ASCII 图标注...")
        self.check_ascii_blocks()
        print()

        # 输出结果
        self.print_results()

        return len(self.issues) == 0

    def print_results(self):
        """打印验证结果"""
        print("=" * 60)
        print("验证结果")
        print("=" * 60)
        print()

        if not self.issues and not self.warnings:
            print("✓ 所有检查通过！方案符合规范要求。")
        else:
            if self.issues:
                print(f"发现 {len(self.issues)} 个问题：")
                for issue in self.issues:
                    print(f"  ✗ {issue}")
                print()

            if self.warnings:
                print(f"发现 {len(self.warnings)} 个警告：")
                for warning in self.warnings:
                    print(f"  ⚠ {warning}")
                print()

        print()
        print("=" * 60)


def main():
    if len(sys.argv) != 2:
        print("用法: python3 validate_proposal.py <markdown-file>")
        print()
        print("示例:")
        print("  python3 validate_proposal.py proposal.md")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"错误: 文件不存在: {file_path}")
        sys.exit(1)

    if file_path.suffix.lower() not in ['.md', '.markdown']:
        print(f"警告: 文件扩展名不是 .md: {file_path}")

    validator = ProposalValidator(file_path)
    success = validator.validate()

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
