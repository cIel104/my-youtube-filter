from django.shortcuts import render
from django.conf import settings

api_key = getattr(settings, "settings.youtube_api_key", None)

def home_screen(request):
    return render(request, 'youtube_filter/home_screen.html')

def result_screen(request):
    if settings.DEBUG:
        password = settings.YOUTUBE_API_KEY

    filters = {
        'words' : request.POST.get('word'),
        'result' : request.POST.get('result'),
        'sort' : request.POST.get('sort'),
        #'password' : password
    }
    print(request.POST.get('word'))
    return render(request, 'youtube_filter/result_screen.html', filters)