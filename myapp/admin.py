from django.contrib import admin
from myapp.models import Inbox,UserEmail
# Register your models here.

admin.site.register(Inbox)
admin.site.register(UserEmail)