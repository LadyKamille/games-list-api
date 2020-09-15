"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from api.game import views as game_views

urlpatterns = [
    path('', game_views.APIOverview.as_view(), name='api-overview'),
    path('games', game_views.GameList.as_view(), name='games-list'),
    path('games/<str:pk>', game_views.GameDetail.as_view(), name='game-detail'),
]
