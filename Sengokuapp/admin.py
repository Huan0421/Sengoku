from django.contrib import admin
from Sengokuapp.models import People,Domain,Family,Road,Comment,UserProfile,Message
# Register your models here.
admin.site.register(People)
admin.site.register(Domain)
admin.site.register(Family)
admin.site.register(Road)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Message)
