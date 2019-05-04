"""crowdFunding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include
from project import views
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static

=======
>>>>>>> c1e30cfb0050b6ff6eb3be8c26ba002274d586c9
# from accounts import views


urlpatterns = [
<<<<<<< HEAD
   # path('userprojects/', views.list_user_projects),
=======
    # path('userprojects/', views.list_user_projects),
>>>>>>> c1e30cfb0050b6ff6eb3be8c26ba002274d586c9
    path('', views.home),
    path('admin/', admin.site.urls),
    path('projects/',include('project.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),



<<<<<<< HEAD
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
]
>>>>>>> c1e30cfb0050b6ff6eb3be8c26ba002274d586c9
