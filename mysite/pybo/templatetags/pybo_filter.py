import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

# sub 함수에 @register.filter 애너테이션을 적용하면 
# 템플릿에서 해당 함수를 필터로 사용할 수 있게 된다


@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))