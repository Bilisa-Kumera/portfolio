# Generated by Django 5.1.3 on 2024-11-30 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill_id', models.AutoField(primary_key=True, serialize=False)),
                ('skill_type', models.CharField(max_length=100)),
                ('skill_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='project_description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='title',
        ),
        migrations.AddField(
            model_name='project',
            name='project_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(null=True, upload_to='projects/'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_start_date',
            field=models.DateField(null=True),
        ),
    ]
