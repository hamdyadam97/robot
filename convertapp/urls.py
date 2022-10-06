from django.urls import path
from .views import *
app_name = 'convertapp'
urlpatterns = [
    path('audio',ConvertAudioView.as_view(), name='convert'),

]
