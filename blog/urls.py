from django.urls import include, path
from rest_framework import routers
from config import views
from django.contrib import admin
from django.urls import path, include

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin', include(admin.site.urls)),
    path('api/', include('config.urls'))
]