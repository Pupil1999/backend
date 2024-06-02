from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Video

# Create your views here.
class SaveVideoView(APIView):
    def post(self, request):
        video_file = request.FILES.get('video')
        if video_file:
            Video.objects.create(video_file=video_file)
            return Response("Video saved successfully", status=status.HTTP_201_CREATED)
        return Response("No video file provided", status=status.HTTP_400_BAD_REQUEST)
