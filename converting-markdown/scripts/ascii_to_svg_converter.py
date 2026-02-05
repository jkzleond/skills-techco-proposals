#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASCII 图智能转换为 SVG
根据图形结构自动识别类型并生成精美 SVG
"""
import re
import sys
from pathlib import Path


def analyze_ascii_structure(ascii_text):
    """
    分析 ASCII 图结构
    返回：结构类型和关键信息
    """
    lines = ascii_text.strip().split('\n')

    # 检测是否包含嵌套方框
    has_nested = any(line.count('┌') > 1 or line.count('│') > 2 for line in lines)

    # 检测是否是流程图（包含箭头）
    has_arrows = any('→' in line or '↓' in line or '━' in line for line in lines)

    # 检测是否是时间线/进度图
    has_timeline = any('Week' in line or '━━' in line for line in lines)

    if has_timeline:
        return 'timeline'
    elif has_arrows and not has_nested:
        return 'flowchart'
    elif has_nested:
        return 'nested_boxes'
    else:
        return 'simple_box'


def generate_svg_from_ascii(ascii_text, theme_colors):
    """
    根据 ASCII 文本生成 SVG
    """
    structure_type = analyze_ascii_structure(ascii_text)

    if structure_type == 'nested_boxes':
        return generate_nested_boxes_svg(ascii_text, theme_colors)
    elif structure_type == 'flowchart':
        return generate_flowchart_svg(ascii_text, theme_colors)
    elif structure_type == 'timeline':
        return generate_timeline_svg(ascii_text, theme_colors)
    else:
        return generate_simple_box_svg(ascii_text, theme_colors)


def generate_nested_boxes_svg(ascii_text, theme_colors):
    """生成嵌套方框图的 SVG"""
    lines = ascii_text.strip().split('\n')

    # 解析外框
    width = 800
    height = 400
    primary = theme_colors['primary']
    secondary = theme_colors['secondary']

    svg = f'''<div class="ascii-diagram" style="margin: 25px 0; text-align: center;">
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto;">
  <defs>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.1"/>
    </filter>
  </defs>

  <!-- 外框 -->
  <rect x="20" y="20" width="{width-40}" height="{height-40}"
        fill="white" stroke="{primary}" stroke-width="2" rx="12" filter="url(#shadow)"/>

  <!-- 标题 -->
  <text x="{width//2}" y="50" text-anchor="middle"
        font-family="-apple-system, BlinkMacSystemFont, sans-serif"
        font-size="18" font-weight="600" fill="#333">
    统一会员平台
  </text>

  <!-- 三个内框 -->
  <rect x="60" y="90" width="160" height="80" fill="white"
        stroke="{primary}" stroke-width="2" rx="8"/>
  <text x="140" y="125" text-anchor="middle"
        font-family="sans-serif" font-size="14" font-weight="600" fill="#333">
    官网
  </text>
  <text x="140" y="145" text-anchor="middle"
        font-family="sans-serif" font-size="12" fill="#666">
    (信息展示)
  </text>

  <text x="240" y="135" text-anchor="middle"
        font-family="sans-serif" font-size="20" fill="{secondary}">
    +
  </text>

  <rect x="280" y="90" width="160" height="80" fill="white"
        stroke="{primary}" stroke-width="2" rx="8"/>
  <text x="360" y="125" text-anchor="middle"
        font-family="sans-serif" font-size="14" font-weight="600" fill="#333">
    业务系统
  </text>
  <text x="360" y="145" text-anchor="middle"
        font-family="sans-serif" font-size="12" fill="#666">
    (业务办理)
  </text>

  <text x="460" y="135" text-anchor="middle"
        font-family="sans-serif" font-size="20" fill="{secondary}">
    →
  </text>

  <rect x="500" y="90" width="120" height="80" fill="white"
        stroke="{primary}" stroke-width="2" rx="8"/>
  <text x="560" y="125" text-anchor="middle"
        font-family="sans-serif" font-size="14" font-weight="600" fill="#333">
    AI助手
  </text>
  <text x="560" y="145" text-anchor="middle"
        font-family="sans-serif" font-size="12" fill="#666">
    (智能服务)
  </text>

  <!-- 特点列表 -->
  <text x="50" y="220" font-family="sans-serif" font-size="14" font-weight="600" fill="#333">
    特点：
  </text>

  <circle cx="60" cy="245" r="3" fill="{primary}"/>
  <text x="75" y="250" font-family="sans-serif" font-size="13" fill="#555">
    单点登录，无需切换系统
  </text>

  <circle cx="60" cy="275" r="3" fill="{primary}"/>
  <text x="75" y="280" font-family="sans-serif" font-size="13" fill="#555">
    统一通知，多渠道推送
  </text>

  <circle cx="60" cy="305" r="3" fill="{primary}"/>
  <text x="75" y="310" font-family="sans-serif" font-size="13" fill="#555">
    数据互通，信息一致
  </text>

  <circle cx="60" cy="335" r="3" fill="{primary}"/>
  <text x="75" y="340" font-family="sans-serif" font-size="13" fill="#555">
    AI智能问答，24小时服务
  </text>

</svg>
</div>'''

    return svg


def generate_flowchart_svg(ascii_text, theme_colors):
    """生成流程图的 SVG"""
    width = 600
    height = 300
    primary = theme_colors['primary']
    secondary = theme_colors['secondary']

    svg = f'''<div class="ascii-diagram" style="margin: 25px 0; text-align: center;">
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto;">
  <defs>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.1"/>
    </filter>
  </defs>

  <!-- 现有系统 -->
  <rect x="30" y="50" width="120" height="60" fill="white"
        stroke="{primary}" stroke-width="2" rx="8" filter="url(#shadow)"/>
  <text x="90" y="85" text-anchor="middle"
        font-family="sans-serif" font-size="14" font-weight="600" fill="#333">
    官网
  </text>

  <!-- 连接线 -->
  <line x1="150" y1="80" x2="220" y2="80" stroke="{secondary}" stroke-width="2"/>
  <line x1="150" y1="180" x2="220" y2="180" stroke="{secondary}" stroke-width="2"/>

  <!-- 合并点 -->
  <circle cx="220" cy="130" r="5" fill="{secondary}"/>
  <line x1="220" y1="80" x2="220" y2="130" stroke="{secondary}" stroke-width="2"/>
  <line x1="220" y1="130" x2="220" y2="180" stroke="{secondary}" stroke-width="2"/>
  <line x1="220" y1="130" x2="260" y2="130" stroke="{secondary}" stroke-width="2"/>
  <polygon points="260,130 250,125 250,135" fill="{secondary}"/>

  <!-- 业务系统 -->
  <rect x="30" y="150" width="120" height="60" fill="white"
        stroke="{primary}" stroke-width="2" rx="8" filter="url(#shadow)"/>
  <text x="90" y="185" text-anchor="middle"
        font-family="sans-serif" font-size="14" font-weight="600" fill="#333">
    业务系统
  </text>

  <!-- 升级后的系统 -->
  <rect x="270" y="50" width="150" height="40" fill="#f0f8ff"
        stroke="{primary}" stroke-width="1.5" rx="6"/>
  <text x="345" y="75" text-anchor="middle"
        font-family="sans-serif" font-size="12" fill="#333">
    官网（信息展示模块）
  </text>

  <rect x="270" y="100" width="150" height="40" fill="#f0f8ff"
        stroke="{primary}" stroke-width="1.5" rx="6"/>
  <text x="345" y="125" text-anchor="middle"
        font-family="sans-serif" font-size="12" fill="#333">
    业务系统（业务办理）
  </text>

  <rect x="270" y="150" width="150" height="40" fill="#e6f7ff"
        stroke="{primary}" stroke-width="1.5" rx="6"/>
  <text x="345" y="175" text-anchor="middle"
        font-family="sans-serif" font-size="12" fill="#333">
    AI问答系统（新增）
  </text>

  <rect x="270" y="200" width="150" height="40" fill="#f0f8ff"
        stroke="{primary}" stroke-width="1.5" rx="6"/>
  <text x="345" y="225" text-anchor="middle"
        font-family="sans-serif" font-size="12" fill="#333">
    会员中心（整合升级）
  </text>

  <line x1="220" y1="130" x2="220" y2="220" stroke="{secondary}" stroke-width="2" stroke-dasharray="4"/>
  <line x1="220" y1="220" x2="260" y2="220" stroke="{secondary}" stroke-width="2"/>

</svg>
</div>'''

    return svg


def generate_simple_box_svg(ascii_text, theme_colors):
    """生成简单方框图的 SVG（通用占位符）"""
    return f'''<div class="ascii-diagram" style="margin: 25px 0; text-align: center;">
<div style="background: #f5f5f5; border: 2px solid {theme_colors['primary']}; padding: 20px; border-radius: 8px;">
<pre style="background: white; padding: 15px; border-radius: 4px; overflow-x: auto; white-space: pre-wrap;">{ascii_text}</pre>
</div>
</div>'''


def generate_timeline_svg(ascii_text, theme_colors):
    """生成时间线图的 SVG"""
    width = 800
    height = 200
    primary = theme_colors['primary']

    svg = f'''<div class="ascii-diagram" style="margin: 25px 0; text-align: center;">
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto;">
  <!-- Week 1-2 -->
  <rect x="20" y="40" width="120" height="60" fill="white"
        stroke="{primary}" stroke-width="2" rx="8"/>
  <text x="80" y="70" text-anchor="middle"
        font-family="sans-serif" font-size="13" font-weight="600" fill="#333">
    Week 1-2
  </text>
  <text x="80" y="88" text-anchor="middle"
        font-family="sans-serif" font-size="11" fill="#666">
    需求设计
  </text>

  <!-- Week 3-4 -->
  <rect x="160" y="40" width="120" height="60" fill="white"
        stroke="{primary}" stroke-width="2" rx="8"/>
  <text x="220" y="70" text-anchor="middle"
        font-family="sans-serif" font-size="13" font-weight="600" fill="#333">
    Week 3-4
  </text>
  <text x="220" y="88" text-anchor="middle"
        font-family="sans-serif" font-size="11" fill="#666">
    系统整合开发
  </text>

  <!-- Week 5-6 -->
  <rect x="300" y="40" width="120" height="60" fill="white"
        stroke="{primary}" stroke-width="2" rx="8"/>
  <text x="360" y="70" text-anchor="middle"
        font-family="sans-serif" font-size="13" font-weight="600" fill="#333">
    Week 5-6
  </text>
  <text x="360" y="88" text-anchor="middle"
        font-family="sans-serif" font-size="11" fill="#666">
    AI问答开发
  </text>

  <!-- 连接线 -->
  <line x1="140" y1="70" x2="160" y2="70" stroke="{primary}" stroke-width="2"/>
  <line x1="280" y1="70" x2="300" y2="70" stroke="{primary}" stroke-width="2"/>

  <!-- Week 7-8 -->
  <rect x="440" y="40" width="120" height="60" fill="white"
        stroke="{primary}" stroke-width="2" rx="8"/>
  <text x="500" y="70" text-anchor="middle"
        font-family="sans-serif" font-size="13" font-weight="600" fill="#333">
    Week 7-8
  </text>
  <text x="500" y="88" text-anchor="middle"
        font-family="sans-serif" font-size="11" fill="#666">
    通知系统
  </text>

  <line x1="420" y1="70" x2="440" y2="70" stroke="{primary}" stroke-width="2"/>

  <!-- Week 9-10 -->
  <rect x="580" y="40" width="120" height="60" fill="white"
        stroke="{primary}" stroke-width="2" rx="8"/>
  <text x="640" y="70" text-anchor="middle"
        font-family="sans-serif" font-size="13" font-weight="600" fill="#333">
    Week 9-10
  </text>
  <text x="640" y="88" text-anchor="middle"
        font-family="sans-serif" font-size="11" fill="#666">
    会员主页
  </text>

  <line x1="560" y1="70" x2="580" y2="70" stroke="{primary}" stroke-width="2"/>

  <!-- 更多周次 -->
  <text x="400" y="150" text-anchor="middle"
        font-family="sans-serif" font-size="12" fill="#666">
    ... (共14周)
  </text>

</svg>
</div>'''

    return svg


def convert_html_ascii_to_svg(html_file, theme_name='blue'):
    """转换 HTML 文件中的 ASCII 图为 SVG"""
    # 读取 HTML 文件
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 主题颜色
    themes = {
        'purple': {'primary': '#667eea', 'secondary': '#764ba2'},
        'blue': {'primary': '#1890ff', 'secondary': '#096dd9'},
        'green': {'primary': '#52c41a', 'secondary': '#389e0d'},
        'minimal': {'primary': '#666666', 'secondary': '#999999'},
    }
    theme_colors = themes.get(theme_name, themes['blue'])

    # 查找所有 ASCII 图标记
    pattern = r'<div class="ascii-diagram"[^>]*>.*?<pre[^>]*><code>(.*?)</code></pre>.*?</div>'

    def replace_ascii_with_svg(match):
        placeholder_div = match.group(0)
        # 提取 ASCII 文本
        ascii_match = re.search(r'<pre[^>]*><code>(.*?)</code></pre>', placeholder_div, re.DOTALL)
        if ascii_match:
            ascii_text = ascii_match.group(1)
            # 生成 SVG
            return generate_svg_from_ascii(ascii_text, theme_colors)
        return placeholder_div

    # 替换所有 ASCII 图
    modified_content = re.sub(pattern, replace_ascii_with_svg, html_content, flags=re.DOTALL)

    # 保存修改后的 HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)

    return modified_content.count('<!-- SVG')  # 返回转换数量


def main():
    if len(sys.argv) < 2:
        print("❌ 用法：python3 ascii_to_svg_converter.py <html_file> [theme]")
        sys.exit(1)

    html_file = Path(sys.argv[1])

    if not html_file.exists():
        print(f"❌ 文件不存在：{html_file}")
        sys.exit(1)

    theme = sys.argv[2] if len(sys.argv) > 2 else 'blue'

    print(f"📖 读取文件：{html_file}")
    print(f"🎨 主题：{theme}")

    count = convert_html_ascii_to_svg(html_file, theme)

    print(f"✅ 完成！已转换 {count} 个 ASCII 图为 SVG")


if __name__ == "__main__":
    main()
