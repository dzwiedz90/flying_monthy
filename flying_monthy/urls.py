"""flying_monthy URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from users.views import main_page_view, register
from posts.views import CreateMemeView
=======
from users.views import main_page_view, register, logout
>>>>>>> a7873d88dc066b52ae9a842f0dd7b45cc5920fd0
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', main_page_view, name='home'),
<<<<<<< HEAD
    path('add/', CreateMemeView.as_view(), name='post'),
    # REST FRAMEWORK URLS
    path('api/users/', include('users.api.urls', 'users_api')),
    path('register/', register, name='register'),
=======
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    # REST FRAMEWORK URLS
    path('api/users/', include('users.api.urls', 'users_api')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> a7873d88dc066b52ae9a842f0dd7b45cc5920fd0


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
