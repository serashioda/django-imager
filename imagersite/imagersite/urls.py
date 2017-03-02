"""imagersite URL Configuration."""


from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from imagersite import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home_view, name='home'),
    url(r'^registration/', include('registration.backends.hmac.urls')),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^images/', include('imager_images.urls')),
    url(r'^profile/', include('imager_profile.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
