from django import template
import markdown

from django.contrib import admin

register = template.Library()


@register.filter(is_safe=True)
def markdown_to_html(text):
    """Markdown を HTML に変換して出力
    さらに拡張機能を使用して目次を自動生成する"""
    md = markdown.Markdown(
        extensions=['extra', 'admonition', 'sane_lists', 'toc'])
    html = md.convert(text)
    return html


@register.filter
def admin_url():
    return admin.site.urls
