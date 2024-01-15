from django import forms
from django.core.exceptions import ValidationError

from main.models import Student, Subject


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class StudentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('is_active',)

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']
        if 'sky.pro' not in cleaned_data:
            raise ValidationError('Почта должна относиться к организации')
        return cleaned_data


class SubjectForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Subject
        exclude = ('students',)
