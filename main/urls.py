from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('admins/', views.admin, name='admin'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('add-project/', views.add_project, name='add_project'),
    path('view_skills/', views.view_skills, name='view-skills'),
    path('view_skills_home/', views.view_skills_home, name='view-skills-home'),  
    path('view_projects/', views.view_projects, name='view-projects'),
    path('edit_skill/<int:skill_id>/', views.edit_skill, name='edit_skill'),
    path('delete_skill/<int:skill_id>/', views.delete_skill, name='delete_skill'),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
]

# Add media URL handling in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
