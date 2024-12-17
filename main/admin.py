from django.contrib import admin
from .models import Skill, Project

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_id', 'skill_name', 'skill_type')
    search_fields = ('skill_name', 'skill_type')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name', 'project_start_date', 'project_end_date')
    search_fields = ('project_name',)
    list_filter = ('project_start_date', 'project_end_date')
