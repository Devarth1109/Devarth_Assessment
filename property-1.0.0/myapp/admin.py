from django.contrib import admin
from .models import User,Member,Chairman,Watchman,Visitors,Event,Notice
# Register your models here.
admin.site.register(User)
admin.site.register(Member)
admin.site.register(Chairman)
admin.site.register(Watchman)
admin.site.register(Visitors)
admin.site.register(Event)
admin.site.register(Notice)