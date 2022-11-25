from django import forms
from applicant.models import Resume, WorkExperience, Education, Chat, Response
from django.forms import modelformset_factory

work_experience_formset = modelformset_factory(
    WorkExperience, 
    fields=('begin_date', 'end_date', 'position', 'organization', 'responsibility'),
    extra=1
)

education_formset = modelformset_factory(
    Education, 
    fields=('title', 'faculty', 'speciality', 'end_date_education'),
    extra=1
)

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('title', 'category', 'salary', 'is_published')


class WorkForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ('begin_date', 'end_date', 'position', 'organization', 'responsibility')


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('text',)

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'