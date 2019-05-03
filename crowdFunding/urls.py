<<<<<<< HEAD
"""crowdFunding08 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
=======
"""crowdFunding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
>>>>>>> d36c4b517eab3c21da3097626b93ef170b2a126d
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
<<<<<<< HEAD

urlpatterns = [
=======
from project import views
# from accounts import views


urlpatterns = [
    # path('userprojects/', views.list_user_projects),
    path('', views.home),
>>>>>>> d36c4b517eab3c21da3097626b93ef170b2a126d
    path('admin/', admin.site.urls),
    path('projects/',include('project.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),



]
