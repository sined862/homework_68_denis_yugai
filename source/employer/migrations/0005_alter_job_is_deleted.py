# Generated by Django 4.1.3 on 2022-11-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0004_job_author_alter_job_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_deleted',
            field=models.BooleanField(default=True, verbose_name='Опубликовать'),
        ),
    ]
