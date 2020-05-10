from django.contrib import admin
from facelook.models import EmployeeModels,live_attendance

# Register your models here.
# class EmployeeModelsAdmin(admin.ModelAdmin):
#     list_display = ['Id','Name','Post','Attendance','Start_date','Mail','salary','password','age']
admin.site.register(EmployeeModels)
# class live_attendanceAdmin(admin.ModelAdmin):
#     list_display = ['id','name','post','location','Date','email','salary','age']
admin.site.register(live_attendance)
