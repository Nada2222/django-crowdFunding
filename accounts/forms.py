from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name=forms.CharField(label="First Name")
    last_name=forms.CharField(label="Last Name")
    phone = forms.IntegerField()
    birth_date = forms.DateField(required=False)
    country = forms.CharField(max_length=100)
    facebook_profile = forms.CharField(max_length=100)
    photo = forms.ImageField(label="profile picture",required=False)

    class Meta:
        model = User
        fields = ("username","first_name","last_name" ,"phone","birth_date","country","email","photo", "facebook_profile","password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.phone = self.cleaned_data["phone"]
        user.birth_date = self.cleaned_data["birth_date"]
        user.country = self.cleaned_data["country"]
        user.facebook_profile = self.cleaned_data["facebook_profile"]
        user.photo = self.cleaned_data["photo"]

        if commit:
            user.save()
        return user


