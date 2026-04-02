from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Post


class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)
    bio = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        return phone or None

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'phone',
            'email',
            'avatar',
            'bio',
            'password1',
            'password2'
        ]


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'avatar', 'bio']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'video', 'description']

    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')

        if not image and not video:
            raise forms.ValidationError('Загрузи хотя бы фото или видео.')

        return cleaned_data
