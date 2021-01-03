from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCustomChange, UserCustomCreation
from .models import UserCustom

class UserCustomAdmin(UserAdmin):
    add_form=UserCustomChange
    form=UserCustomCreation
    model=UserCustom
    list_display=['username','email','password']

admin.site.register(UserCustom,UserCustomAdmin)