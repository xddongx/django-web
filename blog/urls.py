"""my_site_prj URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('create/', views.PostCreate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:pk>/update_comment/', views.CommentUpdate.as_view()),
    path('<int:pk>/delete_comment/', views.comment_delete),
    path('<int:pk>/update/', views.PostUpdate.as_view()),
    path('<int:pk>/post_delete/', views.post_delete),
    path('', views.PostList.as_view()),

]
