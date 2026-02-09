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
from pathlib import Path


def extract_placeholders(html_file):
    """提取HTML中的所有AI占位符

    Returns:
        tuple: (placeholders_dict, session_id, document_name)
            - placeholders_dict: {id: {type, raw_content}}
            - session_id: 6位随机号
            - document_name: 文档名称
    """
    html_path = Path(html_file)
    document_name = html_path.stem  # 文档名称（不含扩展名）

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 分两步提取：先找到START和END标记之间的内容
    placeholders = []
    session_id = None

    # 找到所有START标记（带id和session）
    start_pattern = r'<!-- AI-SVG-(ARCHITECTURE|FLOWCHART|UI|TIMELINE|DIAGRAM)-START:id=(\d+),session=([a-f0-9]+) -->'
    start_matches = list(re.finditer(start_pattern, html_content))

    for match in start_matches:
        diagram_type = match.group(1)
        placeholder_id = match.group(2)
        current_session = match.group(3)

        # 使用第一个session_id（所有占位符应该相同）
        if session_id is None:
            session_id = current_session

        start_pos = match.start()

        # 找到对应的END标记（带id和session）
        end_pattern = f'<!-- AI-SVG-{diagram_type}-END:id={placeholder_id},session={current_session} -->'
        end_match = re.search(end_pattern, html_content[start_pos:])

        if not end_match:
            print(f"⚠️  警告：占位符 #{placeholder_id} 缺少END标记")
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
                'id': placeholder_id,  # 字符串类型
                'type': diagram_type.lower(),
                'raw_content': raw_content
            }
            placeholders.append(placeholder)

    return placeholders, session_id, document_name


def save_placeholders_json(placeholders, session_id, document_name, json_file, html_file):
    """保存占位符到JSON文件

    Args:
        placeholders: 占位符列表
        session_id: 会话ID
        document_name: 文档名称
        json_file: 输出JSON文件路径
        html_file: 原始HTML文件路径
    """
    # 确保输出目录存在
    json_file = Path(json_file)
    json_file.parent.mkdir(parents=True, exist_ok=True)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            'session_id': session_id,
            'document': document_name,
            'html_file': str(html_file),  # 保存原始 HTML 文件路径
            'total': len(placeholders),
            'placeholders': placeholders
        }, f, ensure_ascii=False, indent=2)


def main():
    if len(sys.argv) < 2:
        print("用法: python3 extract_placeholders.py <html_file>")
        sys.exit(1)

    html_file = sys.argv[1]
    html_path = Path(html_file)

    # 提取占位符
    placeholders, session_id, document_name = extract_placeholders(html_file)

    if not placeholders:
        print("⚠️  未找到任何AI占位符")
        sys.exit(0)

    # 输出JSON到缓存目录：.cvt-caches/{文档名}/{session_id}/extracted.json
    json_file = html_path.parent / '.cvt-caches' / document_name / session_id / 'extracted.json'

    # 保存到JSON
    save_placeholders_json(placeholders, session_id, document_name, json_file, html_file)

    # 输出统计信息
    from collections import Counter
    types = [p['type'] for p in placeholders]
    stats = Counter(types)

    print(f"✅ 提取完成！")
    print(f"🆔 会话ID: {session_id}")
    print(f"📊 总计: {len(placeholders)}个占位符")
    for dtype, count in stats.most_common():
        print(f"   - {dtype}: {count}个")
    print(f"📄 JSON文件: {json_file}")

    # 输出缓存目录，提示AI Agent
    caches_dir = json_file.parent
    print(f"📁 缓存目录: {caches_dir}")
    print(f"💡 提示：AI Agent应将生成的SVG/HTML保存到此目录，文件名格式：{{id}}.svg 或 {{id}}.html")


if __name__ == '__main__':
    main()
