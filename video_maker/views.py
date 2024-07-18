import os

import cv2
import numpy
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from .forms import VideoForm


def video_generator(text):
    out = cv2.VideoWriter(
        "video_text.mp4",
        cv2.VideoWriter_fourcc(*'mp4v'),
        24,
        (100, 100)
    )
    frame = numpy.zeros((100, 100, 3), dtype=numpy.uint8)
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_thickness = 1
    font_color = (255, 255, 255)
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)
    x, y = 100, 100 // 2

    while True:
        frame.fill(0)
        x -= 5
        cv2.putText(
            frame,
            text,
            (x, y),
            font,
            font_scale,
            font_color,
            font_thickness
        )
        out.write(frame)
        if x + text_size[0][0] < 0:
            break

    out.release()
    return out


def video_maker(request):
    form = VideoForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        text = request.POST.get('text')
        form.save()
        video_generator(text)
        video_path = os.path.join(settings.BASE_DIR, "video_text.mp4")
        with open(video_path, 'rb') as video_file:
            response = HttpResponse(video_file, content_type='video/avi')
            response['Content-Disposition'] = 'attachment; filename="video_text.mp4"'
            return response
    return render(request, 'video_maker/form_to_video.html', context)
