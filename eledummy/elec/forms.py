from django import forms
from .models import Student

class UserForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['user','name','department','mobile','mail']

class CourseForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['course_chosen']
    
class UpdateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','mobile','mail']

