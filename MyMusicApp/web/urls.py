from django.urls import path

from MyMusicApp.web.views import IndexView, ProfileCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create-profile/', ProfileCreateView.as_view(), name='profile-create'),
]