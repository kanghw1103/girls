from django.contrib import admin
from django.urls import path, include
# from . import views

urlpatterns = [
    # path('', views.homepage, name='home'),
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]
