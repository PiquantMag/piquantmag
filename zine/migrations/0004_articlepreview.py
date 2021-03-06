# Generated by Django 2.0 on 2018-02-11 21:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('zine', '0003_allow_issue_fields_to_be_blank'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePreview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='zine.Article')),
            ],
        ),
    ]
