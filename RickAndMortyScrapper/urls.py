from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from game import views
from scrapper.views import LocationView, CharacterView, EpisodeView, SeasonEpisodeView

urlpatterns = [
    path('sign-up/', views.UserRegisterView.as_view(), name='register'),
    path('sign-in/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    path('me/', views.UserView.as_view(), name='personal_data'),
    path('admin/', admin.site.urls),
    path('home/', view=views.HomeView.as_view(), name='home'),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

router = routers.DefaultRouter()
router.register(r'api/usercard', views.UserCardView, basename='usercard')
router.register(r'api/location', LocationView, basename='location')
router.register(r'api/character', CharacterView, basename='character')
router.register(r'api/episode', EpisodeView, basename='episode')
router.register(r'api/seasons-list', SeasonEpisodeView,
                basename='seasons-list')
router.register(
    r'api/collection/(?P<user>[^/]+)', views.AnotherUserCardsView, basename='collection')


urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
