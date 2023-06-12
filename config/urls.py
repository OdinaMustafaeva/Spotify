from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from playlist.views import PlaylistDetailView, PlaylistView

schema_view = get_schema_view(
    openapi.Info(
        title="Spotify",
        default_version='v1',
        description="spotify API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@blog.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("music/", include("playlist.urls")),
    path("user/", include("user.urls")),
    path("category/", include("category.urls")),
    path("playlist/", PlaylistView.as_view()),
    path("playlist/<str:id>", PlaylistDetailView.as_view())
]

swagger_urls = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns += swagger_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
