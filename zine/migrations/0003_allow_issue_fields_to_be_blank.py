# Generated by Django 2.0 on 2018-02-11 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zine', '0002_add_image_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='synopsis',
            field=models.TextField(blank=True, null=True),
        ),
    ]