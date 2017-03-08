"""imagersite URL Configuration."""


from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.routers import DefaultRouter

from imagersite import views


# router = DefaultRouter()
# router.register(r'photos', views.APIUserPhotoListView, base_name="photos")

urlpatterns = [
    url('', include('social_django.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home_view, name='home'),
    url(r'^registration/', include('registration.backends.hmac.urls')),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^profile/', include('imager_profile.urls')),
    url(r'^images/', include('imager_images.urls')),
    url(r'^api/v1/', include('imager_api.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
