from .models import User
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firstname','lastname','email','role', 'address','donation','phone')