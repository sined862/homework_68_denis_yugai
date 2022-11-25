# Generated by Django 4.1.3 on 2022-11-25 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employer', '0005_alter_job_is_deleted'),
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to=settings.AUTH_USER_MODEL, verbose_name='Соискатель')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='employer.job', verbose_name='Вакансия')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='applicant.resume', verbose_name='Резюме соискателя')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000, verbose_name='Текст сообщения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='applicant.response', verbose_name='Отклик')),
            ],
        ),
    ]