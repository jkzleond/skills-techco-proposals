#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown 转 HTML 脚本
支持多模板主题
使用专业库（markdown）+ ASCII图转SVG
美观、高效、稳定

使用方法：
    python3 convert.py [markdown文件路径] [--theme THEME]
    python3 convert.py --list-themes
"""

import argparse
import re
import sys
import html
import markdown
import os
import random
import string
from pathlib import Path


def convert_architecture_svg(content, placeholder_id, session_id):
    """转换架构图为SVG

    模式1（保留原样）：直接输出ASCII代码块
    模式2（智能转换）：输出特殊标记，等待AI Agent生成SVG

    Args:
        content: ASCII图内容
        placeholder_id: 占位符ID (1, 2, 3...)
        session_id: 会话唯一标识 (6位随机号)
    """
    ai_enabled = os.environ.get('AI_SVG_CONVERSION', 'false').lower() == 'true'

    if ai_enabled:
        # 智能转换模式：输出AI可识别的标记
        escaped_content = html.escape(content)
        return f'''<!-- AI-SVG-ARCHITECTURE-START:id={placeholder_id},session={session_id} -->
<div class="ai-svg-placeholder" data-id="{placeholder_id}" data-session="{session_id}" data-type="architecture" data-raw="{escaped_content}">
  <div style="background: #fff7e6; border: 2px dashed #fa8c16; border-radius: 8px; padding: 20px; margin: 25px 0; text-align: center;">
    <p style="color: #fa8c16; font-size: 14px; margin: 0;">🤖 AI Agent正在生成架构图SVG...</p>
    <p style="color: #999; font-size: 12px; margin: 5px 0 0 0;">原始内容已嵌入，等待智能处理</p>
  </div>
</div>
<!-- AI-SVG-ARCHITECTURE-END:id={placeholder_id},session={session_id} -->'''
    else:
        # 保留原样模式：输出ASCII代码块
        return f'''<div style="background: #f8f9fa; border: 2px solid #e8e8e8; border-radius: 8px; padding: 20px; margin: 25px 0;">
<pre><code style="font-family: 'Courier New', monospace; white-space: pre; line-height: 1.5;">{content}</code></pre>
</div>'''


def convert_flowchart_svg(content, placeholder_id, session_id):
    """转换流程图为SVG

    Args:
        content: ASCII图内容
        placeholder_id: 占位符ID (1, 2, 3...)
        session_id: 会话唯一标识 (6位随机号)
    """
    ai_enabled = os.environ.get('AI_SVG_CONVERSION', 'false').lower() == 'true'

    if ai_enabled:
        escaped_content = html.escape(content)
        return f'''<!-- AI-SVG-FLOWCHART-START:id={placeholder_id},session={session_id} -->
<div class="ai-svg-placeholder" data-id="{placeholder_id}" data-session="{session_id}" data-type="flowchart" data-raw="{escaped_content}">
  <div style="background: #fff7e6; border: 2px dashed #fa8c16; border-radius: 8px; padding: 20px; margin: 25px 0; text-align: center;">
    <p style="color: #fa8c16; font-size: 14px; margin: 0;">🤖 AI Agent正在生成流程图SVG...</p>
    <p style="color: #999; font-size: 12px; margin: 5px 0 0 0;">原始内容已嵌入，等待智能处理</p>
  </div>
</div>
<!-- AI-SVG-FLOWCHART-END:id={placeholder_id},session={session_id} -->'''
    else:
        return f'''<div style="background: #f8f9fa; border: 2px solid #e8e8e8; border-radius: 8px; padding: 20px; margin: 25px 0;">
<pre><code style="font-family: 'Courier New', monospace; white-space: pre; line-height: 1.5;">{content}</code></pre>
</div>'''


def convert_ui_svg(content, placeholder_id, session_id):
    """转换UI图为HTML

    Args:
        content: ASCII图内容
        placeholder_id: 占位符ID (1, 2, 3...)
        session_id: 会话唯一标识 (6位随机号)
    """
    ai_enabled = os.environ.get('AI_SVG_CONVERSION', 'false').lower() == 'true'

    if ai_enabled:
        escaped_content = html.escape(content)
        return f'''<!-- AI-SVG-UI-START:id={placeholder_id},session={session_id} -->
<div class="ai-svg-placeholder" data-id="{placeholder_id}" data-session="{session_id}" data-type="ui" data-raw="{escaped_content}">
  <div style="background: #fff7e6; border: 2px dashed #fa8c16; border-radius: 8px; padding: 20px; margin: 25px 0; text-align: center;">
    <p style="color: #fa8c16; font-size: 14px; margin: 0;">🤖 AI Agent正在生成UI图HTML...</p>
    <p style="color: #999; font-size: 12px; margin: 5px 0 0 0;">原始内容已嵌入，等待智能处理</p>
  </div>
</div>
<!-- AI-SVG-UI-END:id={placeholder_id},session={session_id} -->'''
    else:
        return f'''<div style="background: #f8f9fa; border: 2px solid #e8e8e8; border-radius: 8px; padding: 20px; margin: 25px 0;">
<pre><code style="font-family: 'Courier New', monospace; white-space: pre; line-height: 1.5;">{content}</code></pre>
</div>'''


def convert_timeline_svg(content, placeholder_id, session_id):
    """转换时间线图为SVG

    Args:
        content: ASCII图内容
        placeholder_id: 占位符ID (1, 2, 3...)
        session_id: 会话唯一标识 (6位随机号)
    """
    ai_enabled = os.environ.get('AI_SVG_CONVERSION', 'false').lower() == 'true'

    if ai_enabled:
        escaped_content = html.escape(content)
        return f'''<!-- AI-SVG-TIMELINE-START:id={placeholder_id},session={session_id} -->
<div class="ai-svg-placeholder" data-id="{placeholder_id}" data-session="{session_id}" data-type="timeline" data-raw="{escaped_content}">
  <div style="background: #fff7e6; border: 2px dashed #fa8c16; border-radius: 8px; padding: 20px; margin: 25px 0; text-align: center;">
    <p style="color: #fa8c16; font-size: 14px; margin: 0;">🤖 AI Agent正在生成时间线图SVG...</p>
    <p style="color: #999; font-size: 12px; margin: 5px 0 0 0;">原始内容已嵌入，等待智能处理</p>
  </div>
</div>
<!-- AI-SVG-TIMELINE-END:id={placeholder_id},session={session_id} -->'''
    else:
        return f'''<div style="background: #f8f9fa; border: 2px solid #e8e8e8; border-radius: 8px; padding: 20px; margin: 25px 0;">
<pre><code style="font-family: 'Courier New', monospace; white-space: pre; line-height: 1.5;">{content}</code></pre>
</div>'''


def convert_diagram_svg(content, placeholder_id, session_id):
    """转换通用图为SVG

    Args:
        content: ASCII图内容
        placeholder_id: 占位符ID (1, 2, 3...)
        session_id: 会话唯一标识 (6位随机号)
    """
    ai_enabled = os.environ.get('AI_SVG_CONVERSION', 'false').lower() == 'true'

    if ai_enabled:
        escaped_content = html.escape(content)
        return f'''<!-- AI-SVG-DIAGRAM-START:id={placeholder_id},session={session_id} -->
<div class="ai-svg-placeholder" data-id="{placeholder_id}" data-session="{session_id}" data-type="diagram" data-raw="{escaped_content}">
  <div style="background: #fff7e6; border: 2px dashed #fa8c16; border-radius: 8px; padding: 20px; margin: 25px 0; text-align: center;">
    <p style="color: #fa8c16; font-size: 14px; margin: 0;">🤖 AI Agent正在生成通用图SVG...</p>
    <p style="color: #999; font-size: 12px; margin: 5px 0 0 0;">原始内容已嵌入，等待智能处理</p>
  </div>
</div>
<!-- AI-SVG-DIAGRAM-END:id={placeholder_id},session={session_id} -->'''
    else:
        return f'''<div style="background: #f8f9fa; border: 2px solid #e8e8e8; border-radius: 8px; padding: 20px; margin: 25px 0;">
<pre><code style="font-family: 'Courier New', monospace; white-space: pre; line-height: 1.5;">{content}</code></pre>
</div>'''

# 导入主题模块
from themes import load_theme, list_themes


def extract_toc(html_content):
    """从HTML内容中提取目录"""
    toc = []

    # 匹配h1、h2和h3标签
    pattern = r'<(h[123])[^>]*>(.*?)</\1>'
    matches = re.findall(pattern, html_content, re.DOTALL)

    for tag, content in matches:
        level = int(tag[1])
        text = re.sub(r'<[^>]+>', '', content)  # 移除HTML标签，只保留文本
        text = text.strip()

        # 跳过空文本
        if not text:
            continue

        # 使用文本内容作为ID（URL编码）
        import urllib.parse
        elem_id = urllib.parse.quote(text)

        # 添加ID到原始HTML
        html_content = html_content.replace(
            f'<{tag}>{content}</{tag}>',
            f'<{tag} id="{elem_id}">{content}</{tag}>',
            1
        )

        item = {
            'text': text,
            'id': elem_id,
            'level': level,
            'children': []
        }

        # 调整层级关系
        if level == 1:
            toc.append(item)
        elif level == 2:
            # h2直接添加到根级别
            toc.append(item)
        elif level == 3:
            # h3添加到最后一个h2的children
            if toc and toc[-1]['level'] == 2:
                toc[-1]['children'].append(item)
            else:
                # 如果没有h2，就添加到根级别
                toc.append(item)

    return toc, html_content


def add_unit(value, unit='px'):
    """智能添加单位，如果值已经包含单位则不添加"""
    value_str = str(value)
    if any(value_str.endswith(u) for u in ['px', 'em', '%', 'rem', 'vh', 'vw']):
        return value_str
    return f"{value_str}{unit}"


def generate_toc_html(toc):
    """生成目录HTML"""
    if not toc:
        return ''

    html = '<ul class="toc-list">'

    # 直接输出所有h2及其子项
    for item in toc:
        level = item['level']

        if level == 2:
            # 如果有子项，添加toggle图标
            if item['children']:
                html += f'''
            <li class="toc-item toc-level-2">
                <div class="toc-h2-wrapper">
                    <a href="#{item['id']}" class="toc-link">{item['text']}</a>
                    <span class="toc-toggle-icon" onclick="toggleH2Children(this)">▶</span>
                </div>
                <ul class="toc-sublist collapsed">
                '''
                for child in item['children']:
                    html += f'''
                    <li class="toc-item toc-level-3">
                        <a href="#{child['id']}" class="toc-link">{child['text']}</a>
                    </li>
                    '''
                html += '</ul></li>'
            else:
                # 没有子项，直接输出链接
                html += f'''
            <li class="toc-item toc-level-2">
                <a href="#{item['id']}" class="toc-link">{item['text']}</a>
            </li>
                '''

    html += '</ul>'
    return html


def convert_markdown_to_html(md_file, html_file, theme_name='purple'):
    """将Markdown转换为HTML"""

    # 加载主题
    try:
        theme = load_theme(theme_name)
    except ValueError as e:
        print(f"❌ {e}")
        sys.exit(1)

    # 生成会话ID和缓存目录
    md_path = Path(md_file)
    doc_name = md_path.stem  # 文档名称（不含扩展名）
    session_id = ''.join(random.choices('abcdef0123456789', k=6))  # 6位随机号

    # 创建缓存目录：.cvt-caches/{文档名}/{session_id}/
    caches_dir = md_path.parent / '.cvt-caches' / doc_name / session_id
    caches_dir.mkdir(parents=True, exist_ok=True)

    print(f"🆔 会话ID：{session_id}")
    print(f"📁 缓存目录：{caches_dir}")

    # 读取Markdown文件
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # ========== 阶段1：提取ASCII图并替换为占位符 ==========
    import re

    # 匹配所有 ascii:类型 代码块
    ascii_pattern = r'```ascii:(\w+)\n(.*?)\n```'
    matches = re.findall(ascii_pattern, content, re.DOTALL)

    # 保存到字典：{placeholder: (类型, 内容)}
    ascii_diagrams = {}
    placeholder_index = 1

    for match in matches:
        diagram_type = match[0]  # 类型：architecture, flowchart, ui等
        diagram_content = match[1]  # ASCII图内容

        placeholder = f'<!-- SVG-PLACEHOLDER-{placeholder_index} -->'
        ascii_diagrams[placeholder] = (diagram_type, diagram_content)
        placeholder_index += 1

        # 替换为占位符
        content = content.replace(
            f'```ascii:{diagram_type}\n{diagram_content}\n```',
            placeholder,
            1  # 只替换第一个匹配（避免重复）
        )

    print(f"📊 提取到 {len(ascii_diagrams)} 个ASCII图")
    for placeholder, (dtype, _) in ascii_diagrams.items():
        print(f"   - {dtype}: {placeholder}")

    # ========== 阶段2：用markdown库转换为HTML ==========

    # 提取标题和元数据
    title = "方案文档"
    metadata = {'编制单位': '', '编制日期': '', '版本号': ''}

    lines = content.split('\n')
    content_start = 0

    # 智能判断是否有 frontmatter
    has_frontmatter = False
    first_separator_index = -1

    # 第一遍扫描：检查是否有 frontmatter 格式的元数据
    for i, line in enumerate(lines):
        if line.strip() == '---':
            first_separator_index = i
            break
        # 检查是否有 frontmatter 中的元数据
        if any(key in line for key in ['**编制单位：**', '**编制日期：**', '**版本号：**']):
            has_frontmatter = True

    # 第二遍扫描：提取标题、元数据，并确定正文起始位置
    separator_count = 0
    for i, line in enumerate(lines):
        if line.startswith('# '):
            title = line[2:].strip()
        elif '**编制单位：**' in line:
            metadata['编制单位'] = line.split('：', 1)[1].strip().rstrip('*').strip()
        elif '**编制日期：**' in line:
            metadata['编制日期'] = line.split('：', 1)[1].strip().rstrip('*').strip()
        elif '**版本号：**' in line:
            metadata['版本号'] = line.split('：', 1)[1].strip().rstrip('*').strip()
        elif line.strip() == '---':
            separator_count += 1
            # 智能判断：
            # - 如果有 frontmatter 格式，从第1个分隔符后开始
            # - 如果没有 frontmatter，从文档开头开始（content_start 保持为 0）
            if has_frontmatter and separator_count == 1:
                content_start = i + 1
                break
            # 如果没有 frontmatter 但遇到了分隔符，从分隔符后开始
            elif not has_frontmatter and separator_count == 1:
                content_start = i + 1
                break

    # 提取正文内容
    markdown_content = '\n'.join(lines[content_start:])

    # 步骤1：使用专业库转换Markdown
    md = markdown.Markdown(extensions=['tables', 'fenced_code'])
    html_body = md.convert(markdown_content)

    # 步骤1.5：提取目录
    toc, html_body = extract_toc(html_body)
    toc_html = generate_toc_html(toc)

    # 步骤2：应用主题CSS模板
    html_template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
            line-height: 1.8;
            color: {theme.text};
            background: {theme.gradient_bg};
            padding: 20px;
            display: flex;
            gap: 20px;
            max-width: 1600px;
            margin: 0 auto;
        }}

        .container {{
            flex: 1;
            background: {theme.background};
            border-radius: {add_unit(theme.border_radius)};
            box-shadow: {theme.box_shadow};
            overflow: hidden;
            min-width: 0;
        }}

        .header {{
            background: {theme.gradient_header};
            color: {theme.header_text};
            padding: {theme.header_padding};
            text-align: center;
        }}

        .header h1 {{
            font-size: {theme.header_h1_size};
            margin-bottom: 20px;
            font-weight: {theme.header_h1_weight};
            color: {theme.header_text};
            text-shadow: {theme.header_text_shadow};
        }}

        .header strong {{
            color: {theme.header_text};
            font-weight: 600;
        }}

        .header .meta {{
            font-size: {theme.header_meta_size};
            opacity: {theme.header_meta_opacity};
        }}

        h1 {{
            color: {theme.primary};
            font-size: {theme.h2_size};
            margin: {theme.h2_margin};
            padding-bottom: 12px;
            border-bottom: 3px solid {theme.primary};
            font-weight: 600;
        }}

        h2 {{
            color: {theme.primary};
            font-size: {theme.h2_size};
            margin: {theme.h2_margin};
            padding-bottom: 12px;
            border-bottom: 3px solid {theme.primary};
            font-weight: 600;
        }}

        h3 {{
            color: {theme.secondary};
            font-size: {theme.h3_size};
            margin: {theme.h3_margin};
            font-weight: 600;
        }}

        h4 {{
            color: {theme.primary};
            font-size: {theme.h4_size};
            margin: {theme.h4_margin};
            font-weight: 600;
        }}

        h5 {{
            color: #666;
            font-size: {theme.h5_size};
            margin: 20px 0 12px 0;
            font-weight: 600;
        }}

        p {{
            margin: {theme.p_margin};
            text-align: justify;
            font-size: {theme.body_size};
            line-height: 1.9;
        }}

        strong {{
            color: {theme.secondary};
            font-weight: 600;
        }}

        blockquote {{
            margin: 20px 0;
            padding: {theme.blockquote_style.get('padding', '15px 20px')};
            background: {theme.gradient_blockquote};
            border-left: {theme.blockquote_style.get('border_left', '4px solid ' + theme.primary)};
            font-style: {theme.blockquote_style.get('font_style', 'italic')};
            border-radius: {add_unit(theme.blockquote_style.get('border_radius', '0 8px 8px 0'), '')};
        }}

        blockquote p {{
            margin: 0;
            font-style: italic;
        }}

        ul, ol {{
            margin: 15px 0;
            padding-left: 35px;
        }}

        li {{
            margin: 10px 0;
            line-height: 1.8;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 30px 0;
            box-shadow: {theme.table_style.get('box_shadow', '0 4px 12px rgba(0,0,0,0.08)')};
            border-radius: {add_unit(theme.table_style.get('border_radius', '10px'))};
            overflow: hidden;
        }}

        thead {{
            background: {theme.gradient_table};
            color: #fff;
        }}

        th {{
            padding: 16px 18px;
            text-align: left;
            font-weight: 600;
            font-size: 15px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        td {{
            padding: 14px 18px;
            border-bottom: 1px solid #f0f0f0;
            font-size: 15px;
        }}

        tr:last-child td {{
            border-bottom: none;
        }}

        tr:hover {{
            background: {theme.gradient_table_hover};
            transition: {theme.table_style.get('hover_transition', 'background 0.3s ease')};
        }}

        pre {{
            background: {theme.code_bg};
            color: {theme.code_text};
            padding: {theme.pre_style.get('padding', '25px')};
            border-radius: {add_unit(theme.pre_style.get('border_radius', '10px'))};
            overflow-x: auto;
            margin: 25px 0;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, "Courier New", monospace;
            font-size: 14px;
            line-height: 1.6;
            box-shadow: {theme.pre_style.get('box_shadow', '0 4px 12px rgba(0,0,0,0.1)')};
        }}

        code {{
            background: {theme.code_inline_style.get('background', '#f4f4f4')};
            padding: {theme.code_inline_style.get('padding', '3px 8px')};
            border-radius: {add_unit(theme.code_inline_style.get('border_radius', '4px'))};
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
            font-size: {theme.code_size};
            color: {theme.code_inline_style.get('color', '#e83e8c')};
        }}

        pre code {{
            background: transparent;
            padding: 0;
            border-radius: 0;
            color: inherit;
        }}

        a {{
            color: {theme.link};
            text-decoration: none;
            font-weight: 500;
        }}

        a:hover {{
            color: {theme.primary};
            text-decoration: underline;
        }}

        hr {{
            border: none;
            border-top: 2px solid #e9ecef;
            margin: 35px 0;
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}

            .content {{
                padding: 30px 25px;
            }}

            header {{
                padding: 30px 20px;
            }}

            header h1 {{
                font-size: 24px;
            }}

            .metadata p {{
                font-size: 14px;
            }}

            h1 {{
                font-size: 22px;
            }}

            h2 {{
                font-size: 22px;
            }}

            h3 {{
                font-size: 19px;
            }}

            table {{
                font-size: 13px;
            }}

            th, td {{
                padding: 10px 12px;
            }}
        }}

        @media print {{
            body {{
                background: #fff;
                padding: 0;
            }}

            .container {{
                box-shadow: none;
                border-radius: 0;
            }}

            header {{
                background: #fff;
                color: #333;
                border-bottom: 3px solid #333;
                padding: 20px;
            }}

            header h1 {{
                color: #333;
            }}

            .metadata {{
                background: none;
                color: #666;
            }}

            h1, h2 {{
                color: #333;
                border-bottom: 2px solid #333;
                page-break-after: avoid;
            }}

            h3 {{
                color: #555;
                page-break-after: avoid;
            }}

            table {{
                page-break-inside: avoid;
            }}

            pre {{
                page-break-inside: avoid;
            }}
        }}

        /* 侧边栏样式 - 使用固定中性配色 */
        .sidebar {{
            width: 280px;
            background: #ffffff;
            border-radius: {add_unit(theme.border_radius)};
            box-shadow: {theme.box_shadow};
            height: calc(100vh - 40px);
            position: sticky;
            top: 20px;
            transition: width 0.3s ease;
            flex-shrink: 0;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}

        .sidebar.collapsed {{
            display: none;
        }}

        .sidebar-header {{
            padding: 20px;
            border-bottom: 1px solid #e8e8e8;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: {theme.gradient_header};
            color: #ffffff;
            min-height: 70px;
            flex-shrink: 0;
        }}

        .sidebar.collapsed .sidebar-header {{
            padding: 0;
            justify-content: center;
            border-bottom: none;
        }}

        .sidebar-header h3 {{
            margin: 0;
            font-size: 1.2em;
            font-weight: 600;
            transition: opacity 0.3s;
            color: #eee;
        }}

        .sidebar.collapsed .sidebar-header h3 {{
            display: none;
        }}

        /* PC端收起时的展开按钮 */
        .pc-toc-toggle {{
            display: none;
            position: fixed;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            width: 24px;
            height: 80px;
            background: {theme.primary};
            color: white;
            border: none;
            border-radius: 0 {add_unit(theme.border_radius)} {add_unit(theme.border_radius)} 0;
            cursor: pointer;
            font-size: 20px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.15);
            align-items: center;
            justify-content: center;
            writing-mode: vertical-rl;
            transition: background 0.2s;
            z-index: 1000;
        }}

        .pc-toc-toggle:hover {{
            background: {theme.secondary};
        }}

        @media (min-width: 769px) {{
            .sidebar.collapsed ~ .pc-toc-toggle {{
                display: flex;
            }}
        }}

        .sidebar-toggle {{
            background: rgba(255, 255, 255, 0.1);
            border: none;
            color: #ffffff;
            font-size: 1.2em;
            cursor: pointer;
            padding: 5px 10px;
            border-radius: 4px;
            transition: background 0.2s;
            flex-shrink: 0;
        }}

        .sidebar.collapsed .sidebar-toggle {{
            background: none;
            padding: 15px;
            font-size: 1.5em;
        }}

        .sidebar-toggle:hover {{
            background: rgba(255, 255, 255, 0.2);
        }}

        .sidebar-content {{
            padding: 15px 0;
            overflow-y: auto;
            flex: 1;
            transition: opacity 0.3s;
        }}

        .sidebar.collapsed .sidebar-content {{
            opacity: 0;
            visibility: hidden;
            display: none;
        }}

        .sidebar-header {{
            padding: 20px;
            border-bottom: 1px solid {theme.border_color};
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: {theme.gradient_header};
            color: {theme.header_text};
        }}

        .sidebar-header h3 {{
            margin: 0;
            font-size: 1.2em;
            font-weight: 600;
            transition: opacity 0.3s;
            color: #eee;
        }}

        .sidebar-toggle {{
            background: rgba(255, 255, 255, 0.1);
            border: none;
            color: {theme.header_text};
            font-size: 1.2em;
            cursor: pointer;
            padding: 5px 10px;
            border-radius: 4px;
            transition: background 0.2s;
            flex-shrink: 0;
        }}

        .sidebar-toggle:hover {{
            background: rgba(255, 255, 255, 0.2);
        }}

        .sidebar-content {{
            padding: 15px 0;
        }}

        .toc-list {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}

        .toc-item {{
            margin: 0;
        }}

        .toc-link {{
            display: block;
            padding: 10px 20px;
            color: {theme.text};
            text-decoration: none;
            transition: all 0.2s;
            border-left: 3px solid transparent;
            width: 100%;
        }}

        .toc-link:hover {{
            background: {theme.code_inline_bg};
            border-left-color: {theme.primary};
            color: {theme.primary};
        }}

        .toc-link.active {{
            background: {theme.code_inline_bg};
            border-left-color: {theme.primary};
            color: {theme.primary};
            font-weight: 600;
        }}

        .toc-level-1 {{
            font-weight: 600;
            font-size: 1.05em;
        }}

        .toc-h1-wrapper {{
            display: flex;
            align-items: center;
            gap: 8px;
            justify-content: space-between;
            width: 100%;
        }}

        .toc-h2-wrapper {{
            display: flex;
            align-items: center;
            gap: 8px;
            justify-content: space-between;
            width: 100%;
        }}

        .toc-toggle-icon {{
            cursor: pointer;
            user-select: none;
            transition: transform 0.2s;
            flex-shrink: 0;
            font-size: 10px;
            color: #999;
            margin-left: auto;
            margin-right: 15px;
        }}

        .toc-toggle-icon.expanded {{
            transform: rotate(90deg);
        }}

        .toc-h1-children {{
            list-style: none;
            padding-left: 24px;
            margin: 0;
            overflow: hidden;
            transition: all 0.3s ease;
        }}

        .toc-h1-children.collapsed {{
            max-height: 0;
            opacity: 0;
        }}

        .toc-h1-children:not(.collapsed) {{
            max-height: 2000px;
            opacity: 1;
        }}

        .toc-level-2 {{
            font-weight: 500;
        }}

        .toc-sublist {{
            list-style: none;
            padding-left: 0;
            margin: 0;
            max-height: 2000px;
            opacity: 1;
            transition: all 0.3s ease;
            overflow: hidden;
        }}

        .toc-sublist.collapsed {{
            max-height: 0;
            opacity: 0;
        }}

        .toc-level-3 .toc-link {{
            padding-left: 40px;
            font-size: 0.95em;
            font-weight: 400;
        }}

        /* 手机端目录展开按钮 */
        .mobile-toc-toggle {{
            display: none;
            position: fixed;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            width: 40px;
            height: 60px;
            background: {theme.primary};
            color: white;
            border: none;
            border-radius: 0 8px 8px 0;
            cursor: pointer;
            font-size: 24px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
            z-index: 1001;
            align-items: center;
            justify-content: center;
        }}

        .mobile-toc-toggle:hover {{
            background: {theme.secondary};
        }}

        .content {{
            padding: {theme.content_padding};
        }}

        /* 响应式设计 */
        @media (max-width: 768px) {{
            body {{
                flex-direction: column;
                padding: 10px;
            }}

            .sidebar {{
                position: fixed;
                left: 0;
                top: 0;
                height: 100vh;
                z-index: 1000;
                border-radius: 0;
                width: 280px;
            }}

            .sidebar.collapsed {{
                left: -280px;
                width: 280px;
            }}

            .sidebar.collapsed ~ .mobile-toc-toggle {{
                display: flex;
            }}

            .container {{
                width: 100%;
            }}

            .content {{
                padding: 30px 20px;
            }}
        }}

        /* 打印时隐藏侧边栏 */
        @media print {{
            body {{
                display: block;
                padding: 0;
            }}

            .sidebar {{
                display: none;
            }}

            .container {{
                box-shadow: none;
                border-radius: 0;
            }}

            .content {{
                padding: 40px 50px;
            }}
        }}
    </style>
</head>
<body>
    <aside class="sidebar">
        <div class="sidebar-header">
            <h3>目录</h3>
            <button class="sidebar-toggle" onclick="toggleSidebar()">☰</button>
        </div>
        <div class="sidebar-content">
            {toc_html}
        </div>
    </aside>

    <button class="pc-toc-toggle" onclick="toggleSidebar()">☰</button>
    <button class="mobile-toc-toggle" onclick="toggleSidebar()">☰</button>

    <div class="container">
        <div class="header">
            <h1>{title}</h1>
            <div class="meta">
                <strong>编制单位：</strong>{metadata.get('编制单位', '')} |
                <strong>编制日期：</strong>{metadata.get('编制日期', '')} |
                <strong>版本号：</strong>{metadata.get('版本号', '')}
            </div>
        </div>
        <div class="content">
            {html_body}
        </div>
    </div>

    <script>
        function toggleSidebar() {{
            const sidebar = document.querySelector('.sidebar');
            sidebar.classList.toggle('collapsed');
        }}

        function toggleH1Children(icon) {{
            const childrenList = icon.parentElement.nextElementSibling;
            if (childrenList && childrenList.classList.contains('toc-h1-children')) {{
                icon.classList.toggle('expanded');
                childrenList.classList.toggle('collapsed');
            }}
        }}

        function toggleH2Children(icon) {{
            const childrenList = icon.parentElement.nextElementSibling;
            if (childrenList && childrenList.classList.contains('toc-sublist')) {{
                icon.classList.toggle('expanded');
                childrenList.classList.toggle('collapsed');
            }}
        }}

        // 高亮当前章节
        window.addEventListener('scroll', () => {{
            const headings = document.querySelectorAll('h1[id], h2[id], h3[id]');
            const tocLinks = document.querySelectorAll('.toc-link');

            let current = '';
            headings.forEach(heading => {{
                const rect = heading.getBoundingClientRect();
                if (rect.top <= 100) {{
                    current = heading.getAttribute('id');
                }}
            }});

            tocLinks.forEach(link => {{
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + current) {{
                    link.classList.add('active');
                }}
            }});
        }});
    </script>
</body>
</html>'''

    # 写入HTML文件
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_template)

    # ========== 阶段3：替换占位符为SVG ==========
    if ascii_diagrams:
        ai_enabled = os.environ.get('AI_SVG_CONVERSION', 'false').lower() == 'true'

        if ai_enabled:
            print(f"\n🎨 AI模式：生成占位符")
            print(f"📊 检测到 {len(ascii_diagrams)}个ASCII图")
        else:
            print(f"\n🎨 默认模式：保留ASCII原样")
            print(f"📊 检测到 {len(ascii_diagrams)}个ASCII图")

        # 重新读取HTML
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # 对每个占位符进行转换
        placeholder_index = 1
        for placeholder, (diagram_type, diagram_content) in ascii_diagrams.items():
            # 根据类型选择转换策略
            if diagram_type == 'architecture':
                svg_content = convert_architecture_svg(diagram_content, placeholder_index, session_id)
            elif diagram_type == 'flowchart':
                svg_content = convert_flowchart_svg(diagram_content, placeholder_index, session_id)
            elif diagram_type == 'ui':
                svg_content = convert_ui_svg(diagram_content, placeholder_index, session_id)
            elif diagram_type == 'timeline':
                svg_content = convert_timeline_svg(diagram_content, placeholder_index, session_id)
            else:
                svg_content = convert_diagram_svg(diagram_content, placeholder_index, session_id)

            placeholder_index += 1

            # 替换占位符为SVG
            html_content = html_content.replace(placeholder, svg_content)
            if not ai_enabled:
                print(f"   ✅ {diagram_type}: {placeholder}")

        # 保存转换后的HTML
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        if not ai_enabled:
            print(f"\n✅ ASCII图已用等宽字体显示")
        else:
            print(f"\n✅ AI占位符已生成到HTML")

    print(f"\n✅ 转换完成！")
    print(f"📄 主题：{theme.name}")
    print(f"📄 输入文件：{md_file}")
    print(f"📄 输出文件：{html_file}")
    print(f"📊 输出文件大小：{html_file.stat().st_size / 1024:.1f} KB")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='将 Markdown 文档转换为美观的 HTML',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例：
  %(prog)s document.md                 # 使用默认主题（purple）
  %(prog)s document.md --theme blue    # 使用蓝色主题
  %(prog)s --list-themes               # 列出所有可用主题
        '''
    )

    parser.add_argument('markdown_file', nargs='?', help='Markdown 文件路径')
    parser.add_argument('--theme', '-t', default='purple',
                       help='主题名称 (默认: purple)')
    parser.add_argument('--list-themes', '-l', action='store_true',
                       help='列出所有可用主题')

    args = parser.parse_args()

    # 列出主题
    if args.list_themes:
        print("🎨 可用主题：\n")
        themes = list_themes()
        for theme_info in themes:
            print(f"  {theme_info['name']}")
            print(f"    {theme_info['display_name']}")
            print(f"    {theme_info['description']}\n")
        return

    # 检查是否指定了文件
    if not args.markdown_file:
        print("❌ 错误：未指定 Markdown 文件")
        print("\n使用方法：")
        print("  python3 scripts/convert.py <markdown_file> [--theme THEME]")
        print("\n示例：")
        print("  python3 scripts/convert.py document.md")
        print("  python3 scripts/convert.py document.md --theme blue")
        print("  python3 scripts/convert.py --list-themes")
        sys.exit(1)

    # 确定要转换的文件（支持绝对路径或相对路径）
    md_path = Path(args.markdown_file)

    # 检查文件是否存在
    if not md_path.exists():
        print(f"❌ 文件不存在：{md_path}")
        print(f"💡 提示：请使用绝对路径或确保文件相对于当前工作目录存在")
        print(f"💡 当前工作目录：{Path.cwd()}")
        sys.exit(1)

    # 生成输出文件路径
    html_path = md_path.with_suffix('.html')

    # 执行转换
    convert_markdown_to_html(md_path, html_path, args.theme)


if __name__ == "__main__":
    main()
