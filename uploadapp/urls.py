from django.urls import path
from . import views

from uploadapp.views import upload_image

urlpatterns = [
    path('image', views.upload_image, name='upload_image'),
    path('file', views.upload_file, name='upload_file')
]
