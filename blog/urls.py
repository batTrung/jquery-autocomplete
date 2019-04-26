from django.urls import path
from . import views

urlpatterns = [
    path("", views.search ,name='search'),
    path("get-search/", views.get_search, name="get_search"),
]
