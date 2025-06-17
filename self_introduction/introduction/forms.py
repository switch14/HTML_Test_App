from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'belonging', 'hobby']
        labels = {
            'name': '名前',
            'belonging': '所属',
            'hobby': '趣味（カンマ区切りで複数入力可）',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '例: 山田 太郎'}),
            'belonging': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '例: 10期生'}),
            'hobby': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '例: 読書, 映画鑑賞, 旅行'}),
        }
