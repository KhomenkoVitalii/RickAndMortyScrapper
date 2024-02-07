from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from game import views
from scrapper.views import LocationView, CharacterView, EpisodeView, SeasonEpisodeView

urlpatterns = [
    path('api/v1/sign-up/', views.UserRegisterView.as_view(), name='register'),
    path('api/v1/sign-in/', views.UserLoginView.as_view(), name='login'),
    path('api/v1/logout/', views.UserLogoutView.as_view(), name="logout"),
    path('api/v1/me/', views.UserView.as_view(), name='personal_data'),
    path('api/v1/home/', view=views.HomeView.as_view(), name='home'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'api/v1/usercard', views.UserCardView, basename='usercard')
router.register(r'api/v1/location', LocationView, basename='location')
router.register(r'api/v1/character', CharacterView, basename='character')
router.register(r'api/v1/episode', EpisodeView, basename='episode')
router.register(r'api/v1/seasons-list', SeasonEpisodeView,
                basename='seasons-list')
router.register(
    r'api/v1/collection/(?P<user>[^/]+)', views.AnotherUserCardsView, basename='collection')


urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
