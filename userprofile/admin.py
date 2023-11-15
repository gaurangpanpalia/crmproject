from django.contrib import admin

# Register your models here.
from .models import Userprofile
from .models import Username
admin.site.register(Userprofile)
admin.site.register(Username)
