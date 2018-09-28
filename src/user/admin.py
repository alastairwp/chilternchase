from django.contrib import admin
from user.models import User

class UserAdmin(admin.ModelAdmin):
    class Meta:
        Model = User

admin.site.register(User, UserAdmin)