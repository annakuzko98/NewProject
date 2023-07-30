# admin.py
from django.contrib import admin
from .models import Blog_Post, DailyPlan

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_name', 'post_description', 'post_date', 'Feeling')
    list_display_links = ('id',)
    list_editable = ('post_description',)
    list_filter = ('post_date', 'Feeling')
    list_per_page = 20

class DailyPlanModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'plan_name', 'plan_description', 'plan_date', 'plan_time', 'completed')
    list_display_links = ('id',)
    list_editable = ('completed',)
    list_filter = ('plan_date', 'completed')
    list_per_page = 20

admin.site.register(Blog_Post, PostModelAdmin)
admin.site.register(DailyPlan, DailyPlanModelAdmin)
