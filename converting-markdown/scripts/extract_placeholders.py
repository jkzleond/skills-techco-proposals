#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提取HTML中的AI占位符，导出为JSON文件

使用方法：
    python3 extract_placeholders.py html_file.json
"""

import json
import re
import html
import sys


def extract_placeholders(html_file):
    """提取HTML中的所有AI占位符"""
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 分两步提取：先找到START和END标记之间的内容
    placeholders = []

    # 找到所有START标记
    start_pattern = r'<!-- AI-SVG-(ARCHITECTURE|FLOWCHART|UI|TIMELINE|DIAGRAM)-START -->'
    start_matches = list(re.finditer(start_pattern, html_content))

    for idx, match in enumerate(start_matches, 1):
        diagram_type = match.group(1)
        start_pos = match.start()

        # 找到对应的END标记
        end_pattern = f'<!-- AI-SVG-{diagram_type}-END -->'
        end_match = re.search(end_pattern, html_content[start_pos:])

        if not end_match:
            continue

        end_pos = start_pos + end_match.end()
        block_content = html_content[start_pos:end_pos]

        # 提取data-raw属性（使用非贪婪模式匹配到引号）
        raw_match = re.search(r'data-raw="([^"]*(?:\\"[^"]*)*)"', block_content, re.DOTALL)
        if raw_match:
            raw_escaped = raw_match.group(1)
            # HTML解码原始内容
            raw_content = html.unescape(raw_escaped)

            placeholder = {
                'id': idx,
                'type': diagram_type.lower(),
                'raw_content': raw_content,
                'svg_code': None  # AI Agent将填充这个字段
            }
            placeholders.append(placeholder)

    return placeholders, html_content


def save_placeholders_json(placeholders, json_file):
    """保存占位符到JSON文件"""
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            'total': len(placeholders),
            'placeholders': placeholders
        }, f, ensure_ascii=False, indent=2)


def main():
    if len(sys.argv) < 2:
        print("用法: python3 extract_placeholders.py html_file.json")
        sys.exit(1)

    html_file = sys.argv[1]
    json_file = html_file.replace('.html', '.json')

    # 提取占位符
    placeholders, html_content = extract_placeholders(html_file)

    # 保存到JSON
    save_placeholders_json(placeholders, json_file)

    # 输出统计信息
    from collections import Counter
    types = [p['type'] for p in placeholders]
    stats = Counter(types)

    print(f"✅ 提取完成！")
    print(f"📊 总计: {len(placeholders)}个占位符")
    for dtype, count in stats.most_common():
        print(f"   - {dtype}: {count}个")
    print(f"📄 JSON文件: {json_file}")


if __name__ == '__main__':
    main()
