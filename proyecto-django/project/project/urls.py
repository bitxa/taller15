from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'departamentos', views.DepartamentoViewSet)
router.register(r'edificios', views.EdificioViewSet)
router.register(r'propietarios', views.PropietarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]