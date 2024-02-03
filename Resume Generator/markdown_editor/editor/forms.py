from django import forms
from .models import MarkdownDocument

class MarkdownForm(forms.ModelForm):
    class Meta:
        model = MarkdownDocument
        fields = ['title', 'content']
