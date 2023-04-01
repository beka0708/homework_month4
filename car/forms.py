from django import forms
from . import models


class CarForm(forms.ModelForm):
    class Meta:
        model = models.Cars
        fields = '__all__'


class CarComment(forms.ModelForm):
    class Meta:
        model = models.CommentCar
        fields = '__all__'