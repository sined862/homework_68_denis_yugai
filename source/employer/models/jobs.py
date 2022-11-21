from django.db import models

from django.utils import timezone
from django.db.models import TextChoices


class StatusChoices(TextChoices):
    CHOICE = 'ВЫБРАТЬ', 'Выбрать'
    IT = 'IT', 'IT'
    FINANCE = 'ФИНАНСЫ', 'Финансы'
    MARKETING = 'МАРКЕТИНГ', 'Маркетинг'
    LAWYER = 'ЮРИСТ', 'Юрист'
    ENGINEER = 'ИНЖЕНЕР', 'Инженер'


class Job(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Description', max_length=3000, null=False, blank=False)
    salary = models.IntegerField(verbose_name='Salary', null=False, blank=False)
    is_deleted = models.BooleanField(verbose_name='Deleted', null=False, default=False)
    created_at = models.DateTimeField(verbose_name='Date created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date updated', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Date deleted', null=True, default=None)
    categories = models.CharField(verbose_name='Categories', choices=StatusChoices.choices, max_length=200,
                                  default=StatusChoices.CHOICE)
    experiences = models.CharField(verbose_name='Experiences', max_length=200, null=False, blank=False, default='Нет опыта')

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
