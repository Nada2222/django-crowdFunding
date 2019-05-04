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

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
   first_name=forms.CharField(label="First Name")
   last_name=forms.CharField(label="Last Name")
   phone_regex = RegexValidator(regex=r'^(\+20)?\d{10,13}$', message="Phone number must be entered in the format: '+2099999999999'. Up to 13 digits allowed.")
   phone = forms.CharField(validators=[phone_regex], max_length=13) # validators should be a list
   facebook_profile = forms.CharField(max_length=100)

   birth_date = forms.DateField(
         widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'})
     )
   country = forms.CharField(max_length=100)
   photo = forms.ImageField(label="profile picture",required=False)
   class Meta:
      model = Profile
      fields = ['photo','first_name','last_name','country','birth_date'
                  ,'phone','facebook_profile']

