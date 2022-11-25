from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models import TextChoices


# class StatusChoices(TextChoices):
#     CHOICE = 'ВЫБРАТЬ', 'Выбрать'
#     IT = 'IT', 'IT'
#     FINANCE = 'ФИНАНСЫ', 'Финансы'
#     MARKETING = 'МАРКЕТИНГ', 'Маркетинг'
#     LAWYER = 'ЮРИСТ', 'Юрист'
#     ENGINEER = 'ИНЖЕНЕР', 'Инженер'


class Job(models.Model):
    title = models.CharField(verbose_name='Название вакансии', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Детальное описание вакансии включающее в себя требования по знаниям соискателя', max_length=3000, null=False, blank=False)
    salary = models.IntegerField(verbose_name='Заработная плата', null=False, blank=False)
    is_deleted = models.BooleanField(verbose_name='Опубликовать', null=False, default=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Date deleted', null=True, default=None)
    categories = models.ForeignKey(
        verbose_name='Катeгория вакансии',
        to='applicant.CategoryJob',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    experiences = models.CharField(verbose_name='Требуемый опыт от и до (лет)', max_length=200, null=False, blank=False, default='Нет опыта')
    author = models.ForeignKey(
        verbose_name='Автор резюме',
        to=get_user_model(),
        related_name='jobs',
        on_delete=models.CASCADE,
        null=True,
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
