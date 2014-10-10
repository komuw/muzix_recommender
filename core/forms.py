from django import forms

class LyricForm(forms.Form):
    search_lyrics = forms.CharField()