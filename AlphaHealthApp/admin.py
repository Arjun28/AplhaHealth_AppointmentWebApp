from django.contrib import admin
from .models import Users
from .models import UsersInfo
from .models import UsersAppointments

admin.site.register(Users)
admin.site.register(UsersInfo)
admin.site.register(UsersAppointments)

