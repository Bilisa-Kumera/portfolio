from django import forms
from .models import Skill, Project

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_type', 'skill_name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_description', 'project_image', 'project_start_date', 'project_end_date']
        widgets = {
            'project_start_date': forms.DateInput(attrs={'type': 'date'}),
            'project_end_date': forms.DateInput(attrs={'type': 'date'}),
        }
