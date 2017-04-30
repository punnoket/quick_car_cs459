from django.contrib import admin
from quick_app.models import Notification, Mechanic, User, Job

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Notification._meta.fields]

admin.site.register(Notification)

class MechanicAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Mechanic._meta.fields]

admin.site.register(Mechanic)

class UserAdmin(admin.ModelAdmin):
	list_display=[f.name for f in User._meta.fields]

admin.site.register(User)

class JobAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Job._meta.fields]

admin.site.register(Job)
