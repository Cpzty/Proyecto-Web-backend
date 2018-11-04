"""apis_recetas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views import generic
from rest_framework.schemas import get_schema_view
from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


from apis import views as apis_views
from usuarios import views as usuarios_views



# Router creation
router = DefaultRouter()

# Client

router.register(
    r'categoria',
    apis_views.CategoriaModelViewSet,
)


router.register(
    r'recetas',
    apis_views.RecetaModelViewSet
)


router.register(
    r'CreateUser',
    usuarios_views.UserModelViewSet
)

router.register(
    r'userfavs',
    usuarios_views.FavsUserModelViewSet
)
"""
router.register(
    r'favorito',
    apis_views.FavoritoModelViewSet
)

router.register(
    r'recetario',
    apis_views.RecetasCreadasModelViewSet
)
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    url(r'^api/v1/auth/token/obtain/$', obtain_jwt_token),
    url(r'^api/v1/auth/token/refresh/$', refresh_jwt_token),
    url(r'^api/v1/auth/token/verify/$', verify_jwt_token),
]


