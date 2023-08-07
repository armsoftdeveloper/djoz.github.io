'''

    In This Python File You Find All Important Project URLS

'''

# Importing necessary modules,packages  & other important files
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from main.views.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls), # Admin Page URL
    path('ckeditor/', include('ckeditor_uploader.urls')), # Ckeditor
    path('' , include('main.urls'))  # Main App
]

# Check , If Debug Then Run Debugging Mode
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Handler For 404 Page
handler404 = pageNotFound
