from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static , settings



urlpatterns = i18n_patterns(
    path(
        'admin/', admin.site.urls),
    path(
        '',include('HomeApp.urls')),
    path(
        "",include('Accounts.urls'),
    ),
    path(
        "", include('StoreApp.urls'),
    ),
    path(
        "", include('Cart.urls'),
    ),
    path(
        "", include('Order.urls'),
    ),
    path('rosetta/', include('rosetta.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path("chaining/", include("smart_selects.urls")),
)


urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
