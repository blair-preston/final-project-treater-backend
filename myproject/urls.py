"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
router.register(r'locations', views.LocationViewSet)
router.register(r'parks', views.ParkViewSet)
router.register(r'breeds', views.BreedViewSet)
router.register(r'genders', views.GenderViewSet)
router.register(r'socializations', views.SocializationViewSet)
router.register(r'aggressions', views.AggressionViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'sizes', views.SizeViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'dogs', views.DogViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'connections', views.ConnectionViewSet)
router.register(r'conversations', views.ConversationViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'comments', views.CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('test/', include('myapp.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)