from django import forms

from homepage.models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('text',)
