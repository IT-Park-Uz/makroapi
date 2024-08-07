from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from api.product.views import upload_products

# from rest_framework.authtoken.views import obtain_auth_token


# API URLS
urlpatterns = [
    # API base url
    # path('auth/', include("api.auth.urls")),
    path("api/", include("api.api_router")),
    path(settings.ADMIN_URL, admin.site.urls),
    # DRF auth token
    # path("auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="docs"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('test/<int:pk>/', upload_products, name='upload'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    # Django Admin, use {% url 'admin:index' %}
    # User management
    # path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
