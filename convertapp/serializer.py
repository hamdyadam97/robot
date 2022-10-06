from rest_framework import serializers
from setuptools.command.upload import upload

from .models import ConvertAudio


class ConvertAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConvertAudio
        fields = ['link_video','link']




