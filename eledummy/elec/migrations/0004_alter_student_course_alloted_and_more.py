# Generated by Django 4.1.4 on 2022-12-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elec', '0003_alter_course_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_alloted',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='course_chosen',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
