# Generated by Django 4.2.7 on 2023-11-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_remove_review_rewiew_product_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.ManyToManyField(null=True, related_name='review_related', to='post.review'),
        ),
    ]