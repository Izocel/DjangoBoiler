from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api import views

schema_view = get_schema_view(
   openapi.Info(
      title="Django Boiler - API",
      default_version='v1',
      description="Django Boiler - API",
      contact=openapi.Contact(email="webdevteam@rvdprojects.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('v1/users/', views.UserList.as_view()),
    path('v1/users/<pk>/', views.UserDetails.as_view()),
    path('v1/groups/', views.GroupList.as_view()),
    
    path('v1/docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
