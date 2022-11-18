from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль:', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        label='Подтвердите пароль:', 
        strip=False, 
        required=True,
        widget=forms.PasswordInput
        )
    first_name = forms.CharField(
        label='Имя*:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        label='Имя пользователя*:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        label='Номер телефона*:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.CharField(
        label='Адрес электронной почты*:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    facebook = forms.CharField(
        label='Ссылка на Facebook:',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    linkedin = forms.CharField(
        label='Ссылка на Linkedin:',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    avatar = forms.ImageField(
        label='Фотография:',
        required=False
    )
    password = forms.CharField(
        label='Пароль*:',
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-1'})
    )
    password_confirm = forms.CharField(
        label='Подтверждение пароля*:',
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-1'})
    )

    class Meta:
        model = get_user_model()
        fields = ('is_employer', 'username', 'first_name', 'phone', 'email', 'facebook', 'linkedin', 'avatar', 'password', 'password_confirm')


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя:',
        widget=forms.TextInput(attrs={'class': 'form-control rounded-1'})
    )
    password = forms.CharField(
        label='Пароль:',
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-1'})
    )

