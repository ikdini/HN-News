# Generated by Django 4.1.2 on 2022-10-15 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_delete_comment_delete_poll_delete_polloption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='url',
            field=models.URLField(blank=True, default='http://stoplight.io/prism/', null=True),
        ),
    ]
