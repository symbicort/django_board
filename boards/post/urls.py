from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('write/', post_write),
    path('detail/<int:postid>', post_detail),
    path('delete/', post_delete),
    path('update/',post_update)
]