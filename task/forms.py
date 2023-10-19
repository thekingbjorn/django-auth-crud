#from django.forms import ModelForm
from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','important']
        widgets = {
            'title': forms.TextInput(attrs={'classs':'form-control','placeholder':'Agregue su titulo'}),
            'description': forms.Textarea(attrs={'classs':'form-control','placeholder':'Agregue una descripcion'}),
            'important': forms.CheckboxInput(attrs={'classs':'form-check-input m-auto'}),
        }