from django.shortcuts import render

def home_screen(request):
    return render(request, 'youtube_filter/home_screen.html')
