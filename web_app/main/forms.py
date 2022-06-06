from .models import Student
from django.forms import ModelForm, TextInput, Textarea


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'spec']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя?'
            }),
            "spec": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Специальность?'
            })
        }
