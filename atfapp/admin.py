from __future__ import unicode_literals

from .models import User
from django.contrib import admin

# Register models here.

admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
    readonly_fields=('status',)

