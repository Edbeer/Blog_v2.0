from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/categories_menu.html')
def show_categories(class_menu='sub_menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'class_menu': class_menu}
