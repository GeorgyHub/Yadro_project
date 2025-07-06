from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'middlename', 'birthday', 'phone', 'email', 'logo')
    list_display_links = ('id', 'surname')
    list_filter = ('id', 'surname', 'name', 'middlename', 'birthday',)
    search_fields = ('surname', 'name', 'middlename')

admin.site.register(Profile, ProfileAdmin)