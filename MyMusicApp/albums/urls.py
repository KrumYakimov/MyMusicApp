from django.urls import path, include
from .views import AlbumCreateView, AlbumDetailsView, AlbumEditView, AlbumDeleteView

urlpatterns = [
    path("add/", AlbumCreateView.as_view(), name="album-create"),
    path("<int:pk>/", include([
        path("details/", AlbumDetailsView.as_view(), name="album-details"),
        path("edit/", AlbumEditView.as_view(), name="album-edit"),
        path("delete/", AlbumDeleteView.as_view(), name="album-delete")
    ]))
]
