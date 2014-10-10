from django import forms

class LyricForm(forms.Form):
    lyrics = forms.CharField()