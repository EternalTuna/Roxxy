"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-social-card/', views.create_social_card, name='create_social_card'),
    path('social-card/<int:social_card_id>/', views.view_social_card, name='view_social_card'),
    path('', views.base, name = 'home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
]
