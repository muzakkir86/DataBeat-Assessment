from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserRegistration, UserLoginView, MovieViewSet, CastViewSet

'''
    Movies and cast are the default api
    To check registration and login just type 
    For registration : http://127.0.0.1:8000/registration
    For login : http://127.0.0.1:8000/login
    
    These are optional
    For movies: http://127.0.0.1:8000/movies
    For cast: http://127.0.0.1:8000/cast
'''

router = DefaultRouter()
router.register('movies', MovieViewSet, 'movies')
router.register('cast', CastViewSet, 'cast')

urlpatterns = [
    path('registration/', UserRegistration.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('', include(router.urls))
]
