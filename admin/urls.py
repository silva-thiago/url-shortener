"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.views import signin_view, signup_view, signout_view
from users.views import signin
from urls.views import urls_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signin),
    path('accounts/login/', signin_view),
    path('accounts/register/', signup_view),
    path('accounts/logout/', signout_view),
    path('urls/', urls_list),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
