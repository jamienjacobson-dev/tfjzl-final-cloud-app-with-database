# Generated by Django 4.2.3 on 2025-04-01 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_rename_choice_text_choice_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='grade_point',
            new_name='grade',
        ),
    ]
