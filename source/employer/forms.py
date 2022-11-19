from django import forms

from source.employer.models import Job


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('title', 'description', 'salary', 'categories', 'experiences')
