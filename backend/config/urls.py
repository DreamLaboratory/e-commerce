from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("__debug__/", include("debug_toolbar.urls")),
]
urlpatterns += i18n_patterns(
    path(_("admin/"), admin.site.urls),
    path("", include("src.apps.v1")),
    path("chaining/", include("smart_selects.urls")),
    path("rosetta/", include("rosetta.urls")),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
