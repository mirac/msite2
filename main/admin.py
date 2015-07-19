from django.contrib import admin
from models import User


class UserModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserModelAdmin)
