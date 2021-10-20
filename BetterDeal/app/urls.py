from django.urls import path, include
from . import views
from .views import SearchResultsView


urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='app-about'),
    path('searchresults/', SearchResultsView.as_view(), name='searchresults' ),
    path('search', views.Search.as_view(), name='search'),
]
