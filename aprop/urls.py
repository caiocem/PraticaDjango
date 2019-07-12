"""aprop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin, auth
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.urls import include, path
from django.utils.functional import curry
from django.views.defaults import page_not_found, server_error
from rest_framework import routers

from aprop.input import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'projetos', views.ProjetoViewSet)
router.register(r'colaborador', views.ColaboradorViewSet)
router.register(r'apropriacao', views.ApropriacaoViewSet)

handler500 = curry(server_error, template_name='admin/500.html')
handler404 = curry(page_not_found, template_name='admin/404.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #    path('auth/', include('rest_framework_social_oauth2.urls')),
    #    path('api-auth/', include('rest_framework.urls',
    #                              namespace='rest_framework')),
    #    path('accounts/', include('django.contrib.auth.urls')),
    path('social/', include('allauth.urls')),

    #    path('login/', views.home, name='home'),
    #   path('rest-auth/', include('rest_auth.urls')),
    #    path('accounts/login/', LoginView.as_view(), name='admin/login.html'),
    path('ap/', views.ApropriacaoList.as_view(), name='apropriacao_list'),
    path('ap/view/<int:pk>',
         views.ApropriacaoView.as_view(),
         name='apropriacao_view'),
    path('ap/new', views.ApropriacaoCreate.as_view(), name='apropriacao_new'),
    path('ap/view/<int:pk>',
         views.ApropriacaoView.as_view(),
         name='apropriacao_view'),
    path('ap/edit/<int:pk>',
         views.ApropriacaoUpdate.as_view(),
         name='apropriacao_edit'),
    path('ap/delete/<int:pk>',
         views.ApropriacaoDelete.as_view(),
         name='apropriacao_delete'),
]
