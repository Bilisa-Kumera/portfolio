from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import SkillForm
from .models import Skill
from django.shortcuts import redirect, render
from main.forms import ProjectForm, SkillForm
from .models import Project, Skill
def home(request):
    # Fetch all projects and skills
    projects = Project.objects.all()
    skills = Skill.objects.all()

    # Group skills by their skill_type
    skills_by_type = {}
    for skill in skills:
        if skill.skill_type not in skills_by_type:
            skills_by_type[skill.skill_type] = []
        skills_by_type[skill.skill_type].append(skill)

    print("Grouped Skills:", skills_by_type)  # Make sure it prints the expected structure

    return render(request, 'main/home.html', {'projects': projects, 'skills_by_type': skills_by_type})


def admin(request):
    projects = Project.objects.all()
    return render(request, 'main/admin.html', {'projects': projects})

def admin_dashboard(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'main/admin.html', {'skills': skills, 'projects': projects})

def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill added successfully!')
            return redirect('main:add_skill')  # You can redirect to the same page to show the updated list
    else:
        form = SkillForm()
    
    # Fetch all skills from the database to display in the skills section
    skills = Skill.objects.all()

    return render(request, 'main/add_skill.html', {'form': form, 'skills': skills})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully!')
            return redirect('main:admin')  
        else:
            messages.error(request, 'There was an error adding the project.')
            print(form.errors)  
    else:
        form = ProjectForm()
    
    return render(request, 'main/add_project.html', {'form': form})

def view_skills_home(request):
    # Fetch all skills from the database
    skills = Skill.objects.all()

    # Group skills by their skill_type
    skills_by_type = {}
    for skill in skills:
        # Check if the skill type is already in the dictionary
        if skill.skill_type not in skills_by_type:
            skills_by_type[skill.skill_type] = []
        # Append the skill to its corresponding skill type
        skills_by_type[skill.skill_type].append(skill)

    # Print the grouped skills to debug (optional)
    print("Grouped Skills:", skills_by_type)

    # Pass the grouped skills to the template
    return render(request, 'main/view_skills_home.html', {'skills_by_type': skills_by_type})

def view_skills(request):
    skills = Skill.objects.all()
    return render(request, 'main/view_skills.html', {'skills': skills})

def view_projects(request):
    projects = Project.objects.all()
    return render(request, 'main/view_projects.html', {'projects': projects})

def edit_skill(request, skill_id):
    skill = Skill.objects.get(skill_id=skill_id)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully!')
            return redirect('main:view-skills')
    else:
        form = SkillForm(instance=skill)
    
    return render(request, 'main/edit_skill.html', {'form': form})

def delete_skill(request, skill_id):
    skill = Skill.objects.get(skill_id=skill_id)
    skill.delete()
    messages.success(request, 'Skill deleted successfully!')
    return redirect('main:view-skills')


# Edit Project
def edit_project(request, project_id):
    project = get_object_or_404(Project, project_id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('main:view-projects')
        else:
            messages.error(request, 'Error updating the project.')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'main/edit_project.html', {'form': form, 'project': project})

# Delete Project
def delete_project(request, project_id):
    project = get_object_or_404(Project, project_id=project_id)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('main:view-projects')
    
    return render(request, 'main/delete_project.html', {'project': project})