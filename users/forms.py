#Django
from django import forms
from django.contrib.auth.password_validation import validate_password

#Models 
from django.contrib.auth.models import User
from users.models import Profile

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=4)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(widget=forms.EmailInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already in use')
        
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already in use')
        
        return email
    
    def clean(self):
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password_confirmation != password:
            raise forms.ValidationError('Passwords do not match.')
        
        validate_password(password=password)
        
        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=14, required=False)
    picture = forms.ImageField(required=False)