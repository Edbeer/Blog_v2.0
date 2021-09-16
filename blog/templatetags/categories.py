from django import template
from django.db.models import Count
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/categories_menu.html')
def show_categories(class_menu='sub_menu'):
    categories = Category.objects.annotate(cnt=Count('posts')).filter(cnt__gt=0)
    return {'categories': categories, 'class_menu': class_menu}
