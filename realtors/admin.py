from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    list_filter = ('name', )
    list_editable = ('is_mvp', )
    search_fields = ('name', 'email', 'descripton', 'phone')
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
