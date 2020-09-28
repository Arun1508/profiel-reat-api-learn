from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('helle-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('userprofile', views.UserProfileViewSet)
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
