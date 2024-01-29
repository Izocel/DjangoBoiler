from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("/", include("app.urls")),
    path("api/", include("api.urls")),
    path("admin/", admin.site.urls),
    path("debug/", include("debug_toolbar.urls")),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]