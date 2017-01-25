"""Sengoku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from Sengokuapp.views import index,domain,register,login_f,user_info,message_f
from Sengoku import settings
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^register', register, name='register'),
    url(r'^login_f', login_f, name='login_f'),
    url(r'^message_f', message_f, name='message_f'),
    url(r'^domain/(?P<domainid>\d+)', domain, name='domain'),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', logout, {'next_page':'index'},name='logout'),
    url(r'^user_info', user_info, name='user_info'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
