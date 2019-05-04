from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import Profile

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    birth_date = forms.DateField(
         widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'})
     )
    country = forms.CharField(max_length=100)
    photo = forms.ImageField(label="profile picture",required=False)
    class Meta:
      model = Profile
      fields = ['photo','first_name','last_name','country','birth_date'
                  ,'phone','facebook_profile']

