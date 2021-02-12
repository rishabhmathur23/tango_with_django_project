from django.contrib import admin
<<<<<<< HEAD
from rango.models import Category, Page, UserProfile
=======
from rango.models import Category, Page
>>>>>>> dfff8dc76e2ea3abd62f521a43a1667a8eb58bcd

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)

<<<<<<< HEAD
class PageAdmin(admin.ModelAdmin):
    list_display = ("title",'category","url")
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
=======

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
admin.site.register(Page, PageAdmin)


>>>>>>> dfff8dc76e2ea3abd62f521a43a1667a8eb58bcd
