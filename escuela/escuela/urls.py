"""escuela URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from core.urls import core_patterns
from registration.urls import registration_patterns
from visitante.urls import visitante_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(core_patterns)),
    path('visitante/', include(visitante_patterns)),
    path('accounts/',include(registration_patterns)),
    path('accounts/',include('django.contrib.auth.urls')),
]

if settings.DEBUG == True:
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
