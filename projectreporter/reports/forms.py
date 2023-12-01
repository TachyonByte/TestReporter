from django import forms
from .models import TestResult

class TestresultForm(forms.ModelForm):

    class Meta:
        model = TestResult
        fields = ('comment', 'result',)