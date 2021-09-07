from django import template
from blog.models import Tag

register = template.Library()


@register.inclusion_tag('blog/tags_cloud.html')
def show_tags_cloud(class_cloud='tagcloud'):
    tags = Tag.objects.all()
    return {'tags': tags, 'class_cloud': class_cloud}