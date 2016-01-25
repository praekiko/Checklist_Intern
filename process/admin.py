from django.contrib import admin

# Register your models here.
from .models import Report, Stage, Process

class ReportAdmin(admin.ModelAdmin):
    model = Report
    filter_horizontal = ('stage',)
    list_display = ('title', 'startDate', 'endDate', 'completed_stages_count')
    list_filter = ['startDate']
    search_fields = ['title']

class StageAdmin(admin.ModelAdmin):
    model = Stage
    list_display = ('title', 'completed_processes_count', 'all_processes_count', 'isStageCompleted')

class ProcessAdmin(admin.ModelAdmin):
    model = Process
    list_display = ('title', 'isCompleted')

admin.site.register(Report, ReportAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Process, ProcessAdmin)