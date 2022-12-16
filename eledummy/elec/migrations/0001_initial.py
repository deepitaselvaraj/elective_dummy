# Generated by Django 4.1.4 on 2022-12-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('course_code', models.CharField(blank=True, max_length=8, null=True)),
                ('course_name', models.CharField(blank=True, max_length=30, null=True)),
                ('course_dept', models.CharField(blank=True, max_length=30, null=True)),
                ('syllabus', models.FileField(null=True, upload_to='syllabus')),
                ('total_seats', models.IntegerField(default=60)),
                ('filled_seats', models.IntegerField(default=0)),
                ('vacancy', models.IntegerField(default=60)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(blank=True, max_length=30, null=True)),
                ('dept_short', models.CharField(blank=True, max_length=5, null=True)),
                ('strength', models.IntegerField()),
                ('course_offered', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=8, unique=True)),
                ('name', models.CharField(blank=True, max_length=13, null=True)),
                ('mail', models.EmailField(max_length=254)),
                ('mobile', models.CharField(blank=True, max_length=13, null=True)),
                ('department', models.CharField(blank=True, max_length=30, null=True)),
                ('course_chosen', models.CharField(blank=True, max_length=30, null=True)),
                ('course_alloted', models.CharField(blank=True, max_length=30, null=True)),
                ('updated_at', models.TimeField(auto_now=True)),
            ],
        ),
    ]
