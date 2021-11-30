
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog1/', include('blog1.url')),
    path('instagram', include('instagram.urls')),
]
