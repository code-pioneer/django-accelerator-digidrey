from .models import Contactus
from django import forms
from django.forms import Textarea

class PartialContactusForm(forms.ModelForm):

    class Meta:
        model = Contactus
        widgets = {
            "feedback": Textarea(attrs={"rows": 4, "class":"form-control"}),
        }
        exclude = ["user","tm"]