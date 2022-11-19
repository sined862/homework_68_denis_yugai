from django.db import models

from django.utils import timezone


class Job(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Description', max_length=3000, null=False, blank=False)
    salary = models.IntegerField(verbose_name='Salary', null=False, blank=False)
    is_deleted = models.BooleanField(verbose_name='Deleted', null=False, default=False)
    created_at = models.DateTimeField(verbose_name='Date created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date updated', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Date deleted', null=True, default=None)
    categories = models.ManyToManyField(
        to='employer.Category',
        related_name='jobs',
        blank=True
    )
    experiences = models.ManyToManyField(
        to='employer.Experience',
        related_name='jobs',
        blank=True
    )

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
