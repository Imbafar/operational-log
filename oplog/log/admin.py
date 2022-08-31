from django.contrib import admin

from .models import Duty, Profile, Record, Text, Watch

admin.site.register(Record)
admin.site.register(Duty)
admin.site.register(Watch)
admin.site.register(Text)
admin.site.register(Profile)
