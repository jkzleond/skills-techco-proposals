#!/usr/bin/env python3
"""
检查 Markdown 文件中的 ASCII 图是否都标注了类型

用法：
    python3 check_ascii_blocks.py document.md

功能：
    扫描所有代码块，检查包含框线字符的代码块是否标注了 ascii: 类型
    输出未标注的代码块位置
"""

import re
import sys
from pathlib import Path


def has_box_chars(text):
    """检查文本是否包含 ASCII 框线字符"""
    box_chars = set('┌─│└┘┐┬┼┴├┤┤┘┌┐└─│╭╮╰╯═║╗╚╝╔═')
    return any(char in box_chars for char in text)


def check_markdown_file(file_path):
    """检查 Markdown 文件中的 ASCII 图块"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配所有代码块
    # 格式：```language\ncode\n```
    # 使用贪婪匹配避免提前终止，假设代码块内容中不包含反引号
    # [^`\n]* 匹配语言标识符（可以包含冒号等非单词字符）
    code_block_pattern = re.compile(r'```([^`\n]*)\n([^`]+)```', re.DOTALL)
    blocks = code_block_pattern.finditer(content)

    issues = []
    checked_count = 0
    ascii_count = 0

    for block in blocks:
        lang = block.group(1)
        code = block.group(2)

        # 只检查包含框线字符的代码块
        if has_box_chars(code):
            checked_count += 1

            # 获取代码块位置（行号）
            start_pos = block.start()
            line_num = content[:start_pos].count('\n') + 1

            # 检查是否标注了 ascii: 类型
            if lang.startswith('ascii:'):
                ascii_count += 1
                ascii_type = lang.split(':', 1)[1]
                print(f"✓ Line {line_num}: 标注正确 ({ascii_type})")
            elif lang == 'ascii':
                issues.append((line_num, "标注了 'ascii' 但缺少类型 (应为 ascii:architecture/flowchart/ui/timeline/diagram)"))
                print(f"✗ Line {line_num}: 标注了 'ascii' 但缺少类型")
            else:
                issues.append((line_num, f"未标注类型 (当前语言: '{lang}' 或为空)"))
                print(f"✗ Line {line_num}: 未标注类型 (当前: '{lang}')")

    # 输出摘要
    print("\n" + "=" * 60)
    print(f"检查完成！")
    print(f"共发现 {checked_count} 个包含框线字符的代码块")
    print(f"已正确标注: {ascii_count} 个")
    print(f"存在问题: {len(issues)} 个")

    if issues:
        print("\n" + "=" * 60)
        print("问题详情：")
        for line_num, issue in issues:
            print(f"  Line {line_num}: {issue}")
        print("\n请修复以上问题。支持的类型：")
        print("  - ascii:architecture  (系统架构图)")
        print("  - ascii:flowchart     (流程图)")
        print("  - ascii:ui            (UI界面图)")
        print("  - ascii:timeline      (时间线图)")
        print("  - ascii:diagram       (通用图)")
        return False
    else:
        print("\n✓ 所有 ASCII 图都正确标注了类型！")
        return True


def main():
    if len(sys.argv) != 2:
        print("用法: python3 check_ascii_blocks.py <markdown-file>")
        print("\n示例:")
        print("  python3 check_ascii_blocks.py document.md")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"错误: 文件不存在: {file_path}")
        sys.exit(1)

    if not file_path.suffix.lower() in ['.md', '.markdown']:
        print(f"警告: 文件扩展名不是 .md: {file_path}")

    success = check_markdown_file(file_path)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
