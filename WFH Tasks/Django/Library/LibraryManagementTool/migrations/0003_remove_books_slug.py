# Generated by Django 3.0.3 on 2020-05-06 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagementTool', '0002_books_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='slug',
        ),
    ]
