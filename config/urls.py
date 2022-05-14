from django.contrib import admin
from django.urls import path,include
from myuser.views import UserViewSet
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('', UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='Python18 API',
        default_version='v1',
        description='May API',
    ),
    public = True
)

urlpatterns = [
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0)),
    path('admin/', admin.site.urls),
    path('users/', include(router.urls)),
    path('posts/',include('post.urls')),
    path('comments/', include('comment.urls')),
    path('api-auth/', include('rest_framework.urls')),

]
