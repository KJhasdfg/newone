# sentiment_analysis_app/forms.py
from django import forms

class AnalyzedTextForm(forms.Form):
    text = forms.CharField(label='Enter text for analysis', widget=forms.Textarea)
