# Generated by Django 4.1.3 on 2022-11-25 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_is_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
    ]
