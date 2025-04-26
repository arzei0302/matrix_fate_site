from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static

from matrix_fate.matrix_fate_app.admin import matrix_admin
from matrix_fate.finance_app.admin import finance_admin
from matrix_fate.compatibility_app.admin import compatibility_admin
from matrix_fate.child_app.admin import child_admin
from matrix_fate.prognosis_app.admin import prognosis_admin
from .views import home_redirect

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

    path('', home_redirect),
    path('matrix_auth/', include('matrix_fate.matrix_auth_app.urls')),
    path('matrix_fate/', include('matrix_fate.matrix_fate_app.urls')),
    path('finance/', include('matrix_fate.finance_app.urls')),
    path('compatibility/', include('matrix_fate.compatibility_app.urls')),
    path('child/', include('matrix_fate.child_app.urls')),
    path('prognisis/', include('matrix_fate.prognosis_app.urls')),
    path('other/', include('matrix_fate.other_app.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

