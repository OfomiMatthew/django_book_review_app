
from django.contrib import admin
from django.urls import path,include
from Reviews import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Reviews.urls')),
    
    
]
