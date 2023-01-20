from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static , settings



urlpatterns = [
    path(
        'admin/', admin.site.urls),
    path(
        '',include('HomeApp.urls')),
    path(
        "",include('Accounts.urls'),
    ),
]


urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
