from django import template
from ..models import Category

register = template.Library()
"""
Note: file name|=> load categs
func name |=> temp tag to inject in large temp (base.html)
cats |=> variable for side_menu.html
"""

@register.inclusion_tag('_extra/side_menu.html')  # ,takes_context=True)
def categories_list():
    """list all available caterories """
    # print(vars(context))
    #  if with context
    #  autoescape
    #  use_l10n
    #  use_tz
    #  template_name
    #  render_context
    #  template
    #  dicts
    #  request
    #  _processors
    #  _processors_index
    cats = Category.objects.all()
    return {'cats': cats}
