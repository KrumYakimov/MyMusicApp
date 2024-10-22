from django.urls import include, path

from MyMusicApp.profiles.views import ProfileDetailView, ProfileDeleteView

urlpatterns = [
    path("details/", ProfileDetailView.as_view(), name="profile-details"),
    path("delete/", ProfileDeleteView.as_view(), name="profile-delete")
]