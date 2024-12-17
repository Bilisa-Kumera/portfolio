from django.db import models

class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_type = models.CharField(max_length=100)
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.skill_name} ({self.skill_type})"

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200, null=True)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to='projects/', null=True)
    project_start_date = models.DateField(null=True)
    project_end_date = models.DateField(null=True)

    def __str__(self):
        return self.project_name
