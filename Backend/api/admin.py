from django.contrib import admin

# Register your models here.
def register_models():
    from api.models import User
    admin.site.register(User)