from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    path('blogs/',include("article.urls")),
]



