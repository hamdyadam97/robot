import os
import random
import youtube_dl
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import ConvertAudio
from convertapp.serializer import ConvertAudioSerializer
from pytube import YouTube
import ffmpeg
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
drive = GoogleDrive(gauth)


class ConvertAudioView(generics.GenericAPIView):
    serializer_class = ConvertAudioSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        # video = user['link_video']
        video_url = user['link_video']
        video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
        x = random.randint(1, 999)
        filename = f"{x}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        folder = '1IRrjYoHhUzeB0-9Jjq5bAt_DHXUpJLoF'
        gfile = drive.CreateFile({'parents': [{'id': folder}], 'title': filename})
        gfile.SetContentFile(filename)
        gfile.Upload()
        serializer.save(link=gfile.metadata['alternateLink'])
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)