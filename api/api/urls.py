from django.contrib import admin
from django.urls import path

from django.conf.urls import include

from rest_framework import routers

from auth import views
from rest_framework.authtoken import views as rest_framework_views

from auth.views import CustomAuthToken



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('get-auth-token/', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('auth/', views.ExampleAuthentication)
]