from django.contrib import admin

# Register your models here.
from .models import Report, Stage, Process

class ReportAdmin(admin.ModelAdmin):
    model = Report
    filter_horizontal = ('stage',)
    list_display = ('title', 'startDate', 'endDate', 'completed_stages_count')
    list_filter = ['startDate']
    search_fields = ['title']

admin.site.register(Report, ReportAdmin)
admin.site.register(Stage)
admin.site.register(Process)