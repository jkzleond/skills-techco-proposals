#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
主题模板加载工具
支持 YAML 配置文件
"""

import yaml
from pathlib import Path


class Theme:
    """主题类"""

    def __init__(self, theme_file):
        """加载主题配置 - 合并 base.yaml + 主题颜色"""
        # 1. 先加载 base.yaml
        script_dir = Path(__file__).parent
        templates_dir = script_dir.parent / 'templates'
        base_file = templates_dir / 'base.yaml'

        with open(base_file, 'r', encoding='utf-8') as f:
            base_config = yaml.safe_load(f)

        # 2. 再加载主题颜色文件
        with open(theme_file, 'r', encoding='utf-8') as f:
            theme_config = yaml.safe_load(f)

        # 3. 合并配置（主题颜色覆盖 base 中的颜色）
        self.config = self._deep_merge(base_config, theme_config)

        self.name = self.config.get('name', 'Unknown')
        self.description = self.config.get('description', '')

        # 颜色
        colors = self.config.get('colors', {})
        self.primary = colors.get('primary', '#667eea')
        self.secondary = colors.get('secondary', '#764ba2')
        self.background = colors.get('background', '#ffffff')
        self.text = colors.get('text', '#333333')
        self.gradient_start = colors.get('gradient_start', self.primary)
        self.gradient_end = colors.get('gradient_end', self.secondary)
        self.link = colors.get('link', '#1890ff')
        self.code_bg = colors.get('code_bg', '#2d2d2d')
        self.code_text = colors.get('code_text', '#f8f8f2')
        self.border_color = colors.get('border_color', '#667eea')
        self.header_text = colors.get('header_text', '#ffffff')
        self.blockquote_bg = colors.get('blockquote_bg', f'rgba({self.primary}, 0.08)')
        self.blockquote_border = colors.get('blockquote_border', f'rgba({self.primary}, 0.15)')
        self.table_hover = colors.get('table_hover', f'rgba({self.primary}, 0.05)')
        self.code_inline_bg = colors.get('code_inline_bg', '#e6f7ff')
        self.code_inline_color = colors.get('code_inline_color', '#096dd9')

        # 样式
        styles = self.config.get('styles', {})
        self.border_radius = styles.get('border_radius', 16)
        self.box_shadow = styles.get('box_shadow', '0 20px 60px rgba(0, 0, 0, 0.3)')
        self.header_padding = styles.get('header_padding', '60px 40px')
        self.content_padding = styles.get('content_padding', '50px 60px')
        self.header_h1_weight = styles.get('header_h1_weight', '700')
        self.header_meta_opacity = styles.get('header_meta_opacity', '0.95')
        self.header_text_shadow = styles.get('header_text_shadow', 'none')

        # 字体大小
        font_sizes = self.config.get('font_sizes', {})
        self.header_h1_size = font_sizes.get('header_h1', '2.5em')
        self.header_meta_size = font_sizes.get('header_meta', '1.1em')
        self.h1_size = font_sizes.get('h1', '2.5em')
        self.h2_size = font_sizes.get('h2', '2em')
        self.h3_size = font_sizes.get('h3', '1.5em')
        self.h4_size = font_sizes.get('h4', '1.2em')
        self.h5_size = font_sizes.get('h5', '1.1em')
        self.body_size = font_sizes.get('body', '15px')
        self.code_size = font_sizes.get('code', '0.9em')

        # 间距
        spacing = self.config.get('spacing', {})
        self.h2_margin = spacing.get('h2_margin', '50px 0 25px 0')
        self.h3_margin = spacing.get('h3_margin', '35px 0 20px 0')
        self.h4_margin = spacing.get('h4_margin', '25px 0 15px 0')
        self.p_margin = spacing.get('p_margin', '15px 0')

        # 渐变
        gradients = self.config.get('gradients', {})
        self.gradient_bg = self._substitute_vars(
            gradients.get('background',
                         'linear-gradient(135deg, {primary} 0%, {secondary} 100%)'))
        self.gradient_header = self._substitute_vars(
            gradients.get('header',
                         'linear-gradient(135deg, {primary} 0%, {secondary} 100%)'))
        self.gradient_table = self._substitute_vars(
            gradients.get('table_header',
                         'linear-gradient(135deg, {primary} 0%, {secondary} 100%)'))
        self.gradient_blockquote = self._substitute_vars(
            gradients.get('blockquote',
                         'linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%)'))
        self.gradient_table_hover = self._substitute_vars(
            gradients.get('table_hover', 'rgba(102, 126, 234, 0.05)'))

        # 特殊样式 - 替换模板变量
        special_raw = self.config.get('special_styles', {})
        self.blockquote_style = self._substitute_in_dict(special_raw.get('blockquote', {}))
        self.table_style = self._substitute_in_dict(special_raw.get('table', {}))
        self.code_inline_style = self._substitute_in_dict(special_raw.get('code_inline', {}))
        self.pre_style = self._substitute_in_dict(special_raw.get('pre', {}))

    def _deep_merge(self, base, override):
        """深度合并字典"""
        result = base.copy()
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = value
        return result

    def _substitute_vars(self, text):
        """替换模板变量"""
        if not isinstance(text, str):
            return text
        replacements = {
            '{{primary}}': self.primary,
            '{{secondary}}': self.secondary,
            '{{border_color}}': self.border_color,
            '{{table_hover}}': self.table_hover,
        }
        for key, value in replacements.items():
            text = text.replace(key, value)
        return text

    def _substitute_in_dict(self, data):
        """递归替换字典中的所有模板变量"""
        if isinstance(data, dict):
            return {k: self._substitute_in_dict(v) for k, v in data.items()}
        elif isinstance(data, str):
            return self._substitute_vars(data)
        else:
            return data


def load_theme(theme_name='purple'):
    """加载主题"""
    # 获取模板目录
    script_dir = Path(__file__).parent
    templates_dir = script_dir.parent / 'templates'
    theme_file = templates_dir / f'{theme_name}.yaml'

    if not theme_file.exists():
        raise ValueError(f"主题 '{theme_name}' 不存在: {theme_file}")

    return Theme(theme_file)


def list_themes():
    """列出所有可用主题"""
    script_dir = Path(__file__).parent
    templates_dir = script_dir.parent / 'templates'

    themes = []
    for yaml_file in sorted(templates_dir.glob('*.yaml')):
        theme = Theme(yaml_file)
        themes.append({
            'name': yaml_file.stem,
            'display_name': theme.name,
            'description': theme.description
        })

    return themes


if __name__ == '__main__':
    # 测试：列出所有主题
    print("可用主题：")
    for theme in list_themes():
        print(f"  - {theme['name']}: {theme['display_name']}")
        print(f"    {theme['description']}")
