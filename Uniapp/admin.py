from django.contrib import admin
from.models import Yonalish, Fan, Ustoz
from django.contrib.auth.models import Group,User
admin.site.register(Yonalish)
admin.site.register(Fan)
admin.site.register(Ustoz)

admin.site.unregister(User)
admin.site.unregister(Group)