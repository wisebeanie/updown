from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['user']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '이름을 입력하세요.'}
            ),
        }

