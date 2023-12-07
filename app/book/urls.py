from django.urls import path
from . import views

app_name = "book"
urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.BookListView.as_view(), name="list"),
]
