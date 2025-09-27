from django.contrib import admin
from django.urls import path
from core.views import hello, home, about_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello, name='hello'),
    path('home/', home, name='home'),
    path('about/', about_view, name='about'),
]
