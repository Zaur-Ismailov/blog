
from django.contrib import admin
from django.urls import path, include 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(('app.urls','app'), namespace='app')),
    path("users/", include(('users.urls','users'), namespace='users')),
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)