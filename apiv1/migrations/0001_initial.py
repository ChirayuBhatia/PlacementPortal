# Generated by Django 5.1.5 on 2025-02-07 12:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('enrollment_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, to_field='username')),
                ('branch', models.CharField(choices=[('IT', 'Information Technology'), ('CSE', 'Computer Software Engineering'), ('CSE-AIML', 'Computer Software Engineering'), ('CSE-DS', 'Computer Software Engineering'), ('CSE-BS', 'Computer Software Engineering'), ('ECE', 'Electronics & Communication Engineering'), ('EX', 'Electrical & Electronics Engineering'), ('AU', 'Automobile Engineering'), ('ME', 'Mechanical Engineering')], max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('dob', models.DateField()),
                ('current_location', models.CharField(max_length=255)),
                ('permanent_address', models.JSONField()),
                ('mobile_number', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.JSONField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiv1.student')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('skills_used', models.JSONField()),
                ('links', models.URLField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiv1.student')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.JSONField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiv1.student')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_city', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('skills_used', models.JSONField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiv1.student')),
            ],
            options={
                'verbose_name': 'Internship',
                'verbose_name_plural': 'Internships',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=255)),
                ('board_university', models.CharField(max_length=255)),
                ('medium', models.CharField(max_length=50)),
                ('percentage_cgpa', models.CharField(max_length=10)),
                ('school_college_name', models.CharField(max_length=255)),
                ('start_year', models.IntegerField()),
                ('passing_year', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiv1.student')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Education Records',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(max_length=255)),
                ('organization_name', models.CharField(max_length=255)),
                ('skills_learned', models.JSONField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiv1.student')),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificates',
            },
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiv1.student')),
            ],
            options={
                'verbose_name': 'Summary',
                'verbose_name_plural': 'Summary',
            },
        ),
    ]
