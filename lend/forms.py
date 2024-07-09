
from django import forms
from .models import *
class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ['text']


class MemberForm(forms.ModelForm):
    class Meta:
        model=Member
        fields = ['first_name', 'last_name', 'mobile_number']