from django.contrib import admin
from .models import Category,Author,Tag,UserProductRelation,Product
from mptt.admin import MPTTModelAdmin


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(UserProductRelation)


