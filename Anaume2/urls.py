from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
import REST_API
from REST_API import views as user_views
from cms import views as cms_views

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'notes', cms_views.NoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
