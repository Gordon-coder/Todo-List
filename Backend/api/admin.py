from django.contrib import admin
from api.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)

admin.site.register(User, UserAdmin)