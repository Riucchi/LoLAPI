from django.urls import path
from .views import ChampionsView, ChampionDetailView

urlpatterns = [path('champions/',ChampionsView.as_view(),name="search-champs"),
               path('champions/<str:champion_name>/', ChampionDetailView.as_view(), name="champion-view")
               ]