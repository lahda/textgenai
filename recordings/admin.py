from django.contrib import admin

from recordings.models import Summary,Recording_extend,Recording_rewrite

# Register your models here.
admin.site.register(Summary)
admin.site.register(Recording_extend)
admin.site.register(Recording_rewrite)