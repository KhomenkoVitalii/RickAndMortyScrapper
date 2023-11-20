from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from game.views import sign_in, sign_up, logout_request, home, UserCardView
from scrapper.views import LocationView, CharacterView, EpisodeView, SeasonEpisodeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sign-up/', sign_up, name='register'),
    path('sign-in/', sign_in, name='login'),
    path('logout/', logout_request, name="logout"),
    path('admin/', admin.site.urls),
    path('home/', view=home, name='home'),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

router = routers.DefaultRouter()
router.register(r'api/usercard', UserCardView, basename='usercard')
router.register(r'api/location', LocationView, basename='location')
router.register(r'api/character', CharacterView, basename='character')
router.register(r'api/episode', EpisodeView, basename='episode')
router.register(r'api/seasons-list', SeasonEpisodeView,
                basename='seasons-list')


urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
