from django.urls import path
from .views import post_detail, post_list

app_name='blog'

urlpatterns = [
    path('', post_list, name='posts'),
    path('/<id>', post_detail, name='post_detail'),
]