# Generated by Django 4.1.2 on 2022-10-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_story_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='descendants',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='url',
            field=models.URLField(blank=True, default='http://stoplight.io/prism/', null=True),
        ),
    ]