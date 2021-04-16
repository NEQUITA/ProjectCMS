from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

import django

admin.autodiscover()

def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),
]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
