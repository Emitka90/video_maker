from django.shortcuts import render

from .models import Video


def index(request):
    template_name = 'homepage/index.html'
    videos = Video.objects.values(
        'text', 'created_at'
        ).order_by('-created_at')[:5]
    context = {
        'videos': videos
    }
    return render(request, template_name, context)
