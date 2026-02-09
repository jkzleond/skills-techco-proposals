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
import shutil
from pathlib import Path


def load_placeholders_json(json_file):
    """从JSON文件加载占位符信息

    Returns:
        tuple: (placeholders, session_id, document_name, json_dir, html_file)
    """
    json_path = Path(json_file)
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    session_id = data.get('session_id')
    document_name = data.get('document')
    placeholders = data.get('placeholders', [])

    # 缓存目录就是JSON文件所在目录
    json_dir = json_path.parent

    # 从JSON中读取原始HTML文件路径
    html_file = data.get('html_file')
    if html_file:
        html_file = Path(html_file)

    return placeholders, session_id, document_name, json_dir, html_file


def replace_placeholders(html_file, placeholders, caches_dir, session_id):
    """从缓存目录读取SVG/HTML并替换HTML中的占位符

    Args:
        html_file: HTML文件路径
        placeholders: 占位符列表
        caches_dir: 缓存目录路径
        session_id: 会话ID

    Returns:
        str: 替换后的HTML内容
    """
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    skipped = []
    replaced = []
    ui_count = 0

    for placeholder in placeholders:
        placeholder_id = placeholder['id']
        diagram_type = placeholder['type'].upper()

        # 确定文件扩展名
        is_ui = diagram_type == 'UI'
        ext = 'html' if is_ui else 'svg'

        # 从缓存目录读取生成的文件
        cache_file = caches_dir / f"{placeholder_id}.{ext}"

        if not cache_file.exists():
            print(f"⚠️  跳过占位符 #{placeholder_id}：缓存文件不存在 ({cache_file.name})")
            skipped.append(placeholder_id)
            continue

        # 读取生成的代码
        with open(cache_file, 'r', encoding='utf-8') as f:
            generated_code = f.read()

        # 使用带id和session的标记进行精确匹配
        pattern = rf'(<!-- AI-SVG-{diagram_type}-START:id={placeholder_id},session={session_id} -->).*?(<!-- AI-SVG-{diagram_type}-END:id={placeholder_id},session={session_id} -->)'
        replacement = generated_code

        html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL, count=1)
        replaced.append(placeholder_id)

        if is_ui:
            ui_count += 1
            print(f"✅ 替换占位符 #{placeholder_id} ({diagram_type}) → HTML界面")
        else:
            print(f"✅ 替换占位符 #{placeholder_id} ({diagram_type}) → SVG图形")

    if skipped:
        print(f"\n⚠️  跳过了 {len(skipped)} 个占位符（缓存文件不存在）")

    if replaced:
        print(f"✅ 成功替换了 {len(replaced)} 个占位符")
        if ui_count > 0:
            print(f"   其中 {ui_count} 个为HTML界面，{len(replaced) - ui_count} 个为SVG图形")

    return html_content


def verify_replacement(html_content, expected_count):
    """验证替换是否成功（简单检查）"""
    # 检查是否还有未替换的占位符
    remaining = len(re.findall(r'<!-- AI-SVG-.*?-START:id=', html_content))
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


def cleanup_caches(session_dir):
    """清理缓存目录

    Args:
        session_dir: 会话目录路径（.cvt-caches/{文档名}/{session_id}）
    """
    if not session_dir.exists():
        return

    try:
        # 删除整个会话目录
        shutil.rmtree(session_dir)
        print(f"🧹 已清理缓存目录: {session_dir}")

        # 检查文档目录是否为空，如果为空也删除
        doc_dir = session_dir.parent
        if doc_dir.exists() and not list(doc_dir.iterdir()):
            doc_dir.rmdir()
            print(f"🧹 已清理空的文档目录: {doc_dir}")

    except Exception as e:
        print(f"⚠️  清理缓存目录时出错: {e}")


def main():
    if len(sys.argv) < 2:
        print("用法: python3 replace_svg.py <extracted.json>")
        print("   JSON文件路径：.cvt-caches/{文档名}/{session_id}/extracted.json")
        sys.exit(1)

    json_file = sys.argv[1]
    json_path = Path(json_file)

    # 加载JSON
    placeholders, session_id, document_name, caches_dir, html_file = load_placeholders_json(json_file)
    total = len(placeholders)

    if not session_id:
        print("❌ 错误：JSON文件缺少session_id")
        sys.exit(1)

    if not html_file:
        print("❌ 错误：JSON文件缺少html_file路径")
        sys.exit(1)

    print(f"🆔 会话ID: {session_id}")
    print(f"📄 文档: {document_name}")
    print(f"📄 HTML文件: {html_file}")

    # 检查HTML文件是否存在
    if not html_file.exists():
        print(f"❌ 错误：HTML文件不存在: {html_file}")
        sys.exit(1)

    # 检查缓存文件是否都存在
    missing = []
    for placeholder in placeholders:
        placeholder_id = placeholder['id']
        diagram_type = placeholder['type'].upper()
        ext = 'html' if diagram_type == 'UI' else 'svg'
        cache_file = caches_dir / f"{placeholder_id}.{ext}"
        if not cache_file.exists():
            missing.append((placeholder_id, cache_file.name))

    if missing:
        print(f"❌ 错误：{len(missing)} 个缓存文件不存在")
        for pid, fname in missing:
            print(f"   - 占位符 #{pid}: {fname}")
        print(f"\n💡 提示：AI Agent应先生成SVG/HTML文件到缓存目录：{caches_dir}")
        sys.exit(1)

    print(f"📊 开始替换 {total} 个占位符...\n")

    # 替换占位符
    html_content = replace_placeholders(html_file, placeholders, caches_dir, session_id)

    # 保存HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # 简单验证
    verify_replacement(html_content, total)

    print(f"\n📄 HTML文件已保存: {html_file}")

    # 清理缓存目录
    session_dir = caches_dir
    cleanup_caches(session_dir)


if __name__ == '__main__':
    main()
