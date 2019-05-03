from django import forms
from . import models


class Form_comment(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='text', max_length=1000)


class Form_donation(forms.Form):
    donation = forms.IntegerField(label='donation')


class Form_reportProject(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='text', max_length=1000)


class Form_reportComment(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='text', max_length=1000)


class Form_Project(forms.ModelForm):
    categories = []
    cats = models.Category.objects.values_list('name')
    for cat in cats:
        categories.append(str(cat[0]))

    title = forms.CharField(widget=forms.Textarea, label='title', max_length=100)
    details = forms.CharField(widget=forms.Textarea, label='details', max_length=1000)
    start_date = forms.DateField(required=False, label="start_date")
    end_date = forms.DateField(required=False, label="end_date")
    total_target = forms.IntegerField(required=False)
    category = forms.ModelChoiceField(queryset=models.Category.objects, label="category")

    class Meta:
        model = models.Project
        fields = ('title', 'details', 'total_target', 'start_date', 'end_date', 'category')


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = models.Images
        fields = ('image',)


class TagForm(forms.ModelForm):
    tag = forms.CharField(label='Tag')

    class Meta:
        model = models.Tag
        fields = ('tag',)
