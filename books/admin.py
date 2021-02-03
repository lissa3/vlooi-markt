from django.contrib import admin
from .models import Category,Author,Tag,UserBookRelation,Book
from mptt.admin import MPTTModelAdmin


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(UserBookRelation)


