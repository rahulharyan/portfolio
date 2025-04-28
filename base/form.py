from django import forms
from base.models import Visiter

class visiterForm(forms.ModelForm):
    class Meta:
        model=Visiter
        fields=['full_name','email','phone','subject','message']
        widgets={
            'full_name':forms.TextInput(attrs={'placeholder': 'Your Full Name'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'phone':forms.TextInput(attrs={'placeholder':'Your Phone number'}),
            'subject':forms.TextInput(attrs={'placeholder':'Subject'}),
            'message':forms.Textarea(attrs={'placeholder':'Your message'})
        }