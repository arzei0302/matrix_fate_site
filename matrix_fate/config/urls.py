from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static

from matrix_fate_app.admin import matrix_admin
from finance_app.admin import finance_admin
from compatibility_app.admin import compatibility_admin
from child_app.admin import child_admin
from prognosis_app.admin import prognosis_admin


urlpatterns = [
    path("auth_admin/", admin.site.urls),
    path('matrix_admin/', matrix_admin.urls),
    path('finance_admin/', finance_admin.urls),
    path('compatibility_admin/', compatibility_admin.urls),
    path('child_admin/', child_admin.urls),
    path('prognosis_admin/', prognosis_admin.urls),


    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("ckeditor/", include("ckeditor_uploader.urls")),

    path('matrix_auth/', include('matrix_auth_app.urls')),
    path('matrix_fate/', include('matrix_fate_app.urls')),
    path('finance/', include('finance_app.urls')),
    path('compatibility/', include('compatibility_app.urls')),
    path('child/', include('child_app.urls')),
    path('prognisis/', include('prognosis_app.urls')),
    path('other/', include('other_app.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

