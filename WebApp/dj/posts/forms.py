from django import forms
from .models import SocialCard

class SocialCardForm(forms.ModelForm):
    class Meta:
        model = SocialCard
        fields = ['title', 'image']