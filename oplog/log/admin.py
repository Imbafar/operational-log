from django.contrib import admin

from .models import Depart, Duty, Position, Record, Text, User, Watch

admin.site.register(Record)
admin.site.register(Duty)
admin.site.register(Watch)
admin.site.register(Text)
admin.site.register(User)
admin.site.register(Position)
admin.site.register(Depart)
