from django.urls import path, include
from .views import SongCreateView, SongServeView, SongPlayView

urlpatterns = [
    path('create/', SongCreateView.as_view(), name='create-song'),
    path("<int:pk>/", include([
        path("serve/", SongServeView.as_view(), name='serve-song'),
    path("play/", SongPlayView.as_view(), name='play-song'),
    ]))
]