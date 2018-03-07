from django import forms

from .models import Attachment

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ('object_id', 'attachment', )