from django.urls import path
from .views import SaveVideoView

urlpatterns = [
    path('save_video', SaveVideoView.as_view(), name='save_video'),
]