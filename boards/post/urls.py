from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('write/', post_write),
    path('detail/<int:post_id>', post_detail),
    path('delete/<int:post_id>', post_delete),
    path('update/<int:post_id>',post_update)
]