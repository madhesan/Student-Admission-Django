from django import forms
from stdadmission.models import Student
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"  