"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from .api import api
from core.api import api
from clientele.api import api as clientele_api
# from gallery.api import api as gallery_api
from core.views import get_csrf_token
# from about.api import api as about_api
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
    path('api/v1/clientele/', clientele_api.urls),
    # path('api/v1/gallery/', gallery_api.urls),
    path('api/v1/csrf/', get_csrf_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)