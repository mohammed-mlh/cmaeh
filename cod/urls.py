from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.views import serve as serve_static

def _static_butler(request, path, **kwargs):
    return serve_static(request, path, insecure=True, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    re_path(r'static/(.+)', _static_butler),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)