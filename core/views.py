import requests

from django.views.generic.edit import FormView
from django.shortcuts import render

from .forms import LyricForm

class SongView(FormView):
    """
    Takes the lyrics entered by user and generates songs that the user can listen
    to.
    """
    form_class = LyricForm
    template_name = "songs.html"

    def post(self, request, *args, **kwargs):
        template_vars = {}
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if not form.is_valid():
            return self.form_invalid(form)
        else:
            lyrics = form.cleaned_data.get('lyrics')
            
            template_vars['companies'] = companies
            

        return render(request, template_name, template_vars)
