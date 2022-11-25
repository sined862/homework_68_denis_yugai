from django.db import models
from django.contrib.auth import get_user_model



class CategoryJob(models.Model):
    title = models.CharField(verbose_name='Категория вакансии', max_length=50, blank=False, null=False)

    def __str__(self):
        return self.title



class Resume(models.Model):
    title = models.CharField(
        verbose_name='Название(должность)',
        max_length=50,
        null=False,
        blank=False
    )
    category = models.ForeignKey(
        verbose_name='Катeгория вакансии',
        to='applicant.CategoryJob',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    salary = models.IntegerField(
        verbose_name='Ожидаемая заработная плата',
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        verbose_name='Автор резюме',
        to=get_user_model(),
        related_name='resumes',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовать',
        null=True,
        blank=True,
        default=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )

    def __str__(self):
        return self.title



class WorkExperience(models.Model):
    begin_date = models.DateField(
        verbose_name='Начало работы',
        null=False,
        blank=False
    )
    end_date = models.DateField(
        verbose_name='Окончание',
        null=False,
        blank=False
    )
    position = models.CharField(
        verbose_name='Должность',
        max_length=50,
        null=False,
        blank=False
    )
    organization = models.CharField(
        verbose_name='Организация',
        max_length=50,
        null=False,
        blank=False
    )
    responsibility = models.TextField(
        verbose_name='Обязанности',
        max_length=2000,
        null=False,
        blank=False
    )
    resume = models.ForeignKey(
        verbose_name='Резюме',
        to='applicant.Resume',
        related_name='work_experiences',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.organization



class Education(models.Model):
    title = models.CharField(
        verbose_name='Название учебного заведения',
        max_length=50,
        null=False,
        blank=False
    )
    faculty = models.CharField(
        verbose_name='Факультет',
        max_length=50,
        null=False,
        blank=False
    )
    speciality = models.CharField(
        verbose_name='Специальность',
        max_length=50,
        null=False,
        blank=False
    )
    end_date_education = models.DateField(
        verbose_name='Дата окончания',
        null=False,
        blank=False
    )
    resume = models.ForeignKey(
        verbose_name='Резюме',
        to='applicant.Resume',
        related_name='educations',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title