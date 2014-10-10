import requests

from django.views.decorators.csrf import csrf_exempt 
from django.views.generic import View
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
    
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(SongView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        template_vars = {}
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if not form.is_valid():
            return self.form_invalid(form)
        else:
            #import pdb; pdb.set_trace()
            lyrics = form.cleaned_data.get('search_lyrics')
            cool = "COOL"
            template_vars['cool'] = cool
            

        return render(request, self.template_name, template_vars)
    