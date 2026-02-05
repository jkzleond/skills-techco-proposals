#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASCII 图转 SVG 替换脚本
"""
import re
import sys
from pathlib import Path


def read_html(file_path):
    """读取 HTML 文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_html(file_path, content):
    """写入 HTML 文件"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def contains_ascii_diagram(code_block):
    """检查代码块是否包含 ASCII 图"""
    ascii_chars = ['┌', '┐', '└', '┘', '│', '─', '├', '┤', '┬', '┴', '┼', '━', '┃', '┳', '┻', '╋']
    return any(char in code_block for char in ascii_chars)


def replace_ascii_diagrams_with_svg_placeholder(html_content):
    """
    将 ASCII 图替换为 SVG 占位符
    返回：替换后的 HTML 内容，找到的 ASCII 图数量
    """
    # 匹配 <pre><code>...</code></pre> 块
    pattern = r'<pre><code>(.*?)</code></pre>'
    matches = list(re.finditer(pattern, html_content, re.DOTALL))

    ascii_count = 0
    modified_content = html_content

    # 从后向前替换，避免位置偏移
    for match in reversed(matches):
        code_block = match.group(1)

        if contains_ascii_diagram(code_block):
            ascii_count += 1
            # 创建 SVG 占位符
            placeholder = f'''<div class="ascii-diagram" style="margin: 25px 0; text-align: center;">
<div style="background: #f5f5f5; border: 2px dashed #1890ff; padding: 20px; border-radius: 8px;">
<p style="color: #1890ff; font-weight: 600; margin: 0 0 10px 0;">📊 ASCII 图 {ascii_count}</p>
<pre style="background: white; padding: 15px; border-radius: 4px; overflow-x: auto;"><code>{code_block}</code></pre>
</div>
</div>'''

            # 替换
            start, end = match.span()
            modified_content = modified_content[:start] + placeholder + modified_content[end:]

    return modified_content, ascii_count


def main():
    if len(sys.argv) < 2:
        print("❌ 用法：python3 replace_ascii_with_svg.py <html_file>")
        sys.exit(1)

    html_file = Path(sys.argv[1])

    if not html_file.exists():
        print(f"❌ 文件不存在：{html_file}")
        sys.exit(1)

    print(f"📖 读取文件：{html_file}")
    html_content = read_html(html_file)

    print(f"🔍 识别并替换 ASCII 图...")
    modified_content, ascii_count = replace_ascii_diagrams_with_svg_placeholder(html_content)

    print(f"✅ 找到 {ascii_count} 个 ASCII 图")

    if ascii_count > 0:
        print(f"💾 保存替换后的文件...")
        write_html(html_file, modified_content)
        print(f"✅ 完成！已将 ASCII 图标记为待转换状态")
    else:
        print(f"ℹ️  未找到 ASCII 图，无需替换")


if __name__ == "__main__":
    main()
