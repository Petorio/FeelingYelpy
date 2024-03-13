from django.urls import path
from .views import SearchView, CreateSearchView


urlpatterns = [
    path('search', SearchView.as_view()),
    path('create-search', CreateSearchView.as_view())
]