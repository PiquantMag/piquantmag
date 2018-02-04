# Generated by Django 2.0 on 2018-01-29 00:56

from django.db import migrations, models
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('zine', '0001_all'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='_image_caption_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='component',
            name='image_caption',
            field=markupfield.fields.MarkupField(blank=True, null=True, rendered_field=True),
        ),
        migrations.AddField(
            model_name='component',
            name='image_caption_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown')], default='markdown', editable=False, max_length=30),
        ),
    ]