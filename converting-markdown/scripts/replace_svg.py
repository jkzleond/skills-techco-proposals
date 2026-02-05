#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将JSON文件中的SVG代码替换到HTML文件

使用方法：
    python3 replace_svg.py html_file.json

注意：本脚本只负责替换，不验证SVG/HTML格式。
格式验证由AI Agent在生成代码时自行负责。
"""

import json
import re
import sys


def load_placeholders_json(json_file):
    """从JSON文件加载占位符和SVG代码"""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['placeholders']


def replace_placeholders(html_file, placeholders):
    """替换HTML中的占位符为SVG/HTML代码（无验证）"""
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    skipped = []
    replaced = []
    ui_count = 0

    for placeholder in placeholders:
        svg_code = placeholder.get('svg_code')
        if not svg_code:
            print(f"⚠️  跳过占位符 #{placeholder['id']}：没有svg_code")
            skipped.append(placeholder['id'])
            continue

        diagram_type = placeholder['type'].upper()
        is_ui = diagram_type == 'UI'

        # 直接替换，不做验证（AI Agent已自行验证）
        pattern = rf'(<!-- AI-SVG-{diagram_type}-START -->).*?(<!-- AI-SVG-{diagram_type}-END -->)'
        replacement = svg_code

        html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL, count=1)
        replaced.append(placeholder['id'])

        if is_ui:
            ui_count += 1
            print(f"✅ 替换占位符 #{placeholder['id']} ({diagram_type}) → HTML界面")
        else:
            print(f"✅ 替换占位符 #{placeholder['id']} ({diagram_type}) → SVG图形")

    if skipped:
        print(f"\n⚠️  跳过了 {len(skipped)} 个占位符（缺少代码）")

    if replaced:
        print(f"✅ 成功替换了 {len(replaced)} 个占位符")
        if ui_count > 0:
            print(f"   其中 {ui_count} 个为HTML界面，{len(replaced) - ui_count} 个为SVG图形")

    return html_content


def verify_replacement(html_content, expected_count):
    """验证替换是否成功（简单检查）"""
    remaining = len(re.findall(r'<!-- AI-SVG-.*-START -->', html_content))
    svg_count = len(re.findall(r'<svg[^>]*>', html_content))
    ui_div_count = len(re.findall(r'<div style="[^"]*font-family', html_content))

    # 简单验证：没有未替换的占位符即可
    success = remaining == 0

    if success:
        print(f"\n✅ 替换完成：所有占位符已替换")
        print(f"   - SVG图形: {svg_count}个")
        print(f"   - HTML界面: {ui_div_count}个")
        print(f"   - 总计: {svg_count + ui_div_count}个")
    else:
        print(f"\n⚠️  警告：仍有 {remaining} 个占位符未替换")

    return success


def main():
    if len(sys.argv) < 2:
        print("用法: python3 replace_svg.py html_file.json")
        sys.exit(1)

    json_file = sys.argv[1]
    html_file = json_file.replace('.json', '.html')

    # 加载JSON
    placeholders = load_placeholders_json(json_file)
    total = len(placeholders)

    # 检查是否有代码（svg_code字段）
    missing_code = sum(1 for p in placeholders if not p.get('svg_code'))
    if missing_code == total:
        print(f"❌ 错误：所有占位符都没有代码")
        sys.exit(1)

    print(f"📊 开始替换 {total - missing_code}/{total} 个占位符...\n")

    # 替换占位符
    html_content = replace_placeholders(html_file, placeholders)

    # 保存HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # 简单验证
    verify_replacement(html_content, total - missing_code)

    print(f"\n📄 HTML文件已保存: {html_file}")


if __name__ == '__main__':
    main()
