# Generated by Django 4.2.7 on 2023-11-29 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_remove_category_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
    ]
