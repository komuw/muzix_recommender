import json
import requests

from django.views.decorators.csrf import csrf_exempt 
from django.views.generic import View
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.conf import settings

from .forms import LyricForm

class SongView(FormView):
    """
    This view accepts lyrics input from the user, searches for songs containing that lyrics
    and then displays those songs to the user.
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

            url = 'http://api.musixmatch.com/ws/1.1/track.search'
            payload = {'q_lyrics': lyrics, 'apikey': settings.MUSIXMATCH_APIKEY}
            req = requests.get(url, params=payload)
            musix_data = json.loads(req.content)

            #print "data", musix_data['message']['body']['track_list'][0]['track']
            for i in musix_data['message']['body']['track_list']:
                track_name = i['track']['track_name']
                artist_name = i['track']['artist_name']
                print "track & artist ", track_name, artist_name

                #  now get tracks from TinySong
                songs = {}
                urlencoded = "+".join(track_name.split())
                url = 'http://tinysong.com/a/{0}'.format(urlencoded)
                payload = {'format': 'json', 'key': settings.TINYSONG_APIKEY}
                req = requests.get(url, params=payload)
                tiny_song_data = json.loads(req.content)
                import pdb; pdb.set_trace()
                songs['song_url'] = tiny_song_data
            
            template_vars ['songs'] = tiny_song_data

            cool = "COOL"
            template_vars['cool'] = cool
            

        return render(request, self.template_name, template_vars)
    