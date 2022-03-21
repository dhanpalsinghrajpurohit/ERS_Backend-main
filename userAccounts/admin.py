from django.contrib import admin
from .models import HRProfile,userProfile
# Register your models here.
class AdminHRProfile(admin.ModelAdmin):
    list_display = ("user","company")
admin.site.register(HRProfile,AdminHRProfile)

class AdminUserProfile(admin.ModelAdmin):
    list_display = ("user","fullname","email")
admin.site.register(userProfile,AdminUserProfile)

# admin.site.register(userProfile)