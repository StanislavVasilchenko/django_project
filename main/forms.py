from django import forms

from main.models import Student, Subject


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('is_active',)


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = ('students',)
