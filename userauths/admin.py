from django.contrib import admin

# Register your models here.

from userauths.models import User

class userAdmnin(admin.ModelAdmin):
    # list_display = ['username', 'email', 'bio']
    list_display = ['username', 'email']

admin.site.register(User, userAdmnin)
