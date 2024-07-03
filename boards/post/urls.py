from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('write/', post_write),
    path('detail/<int:post_id>', post_detail),
    path('delete/<int:post_id>', post_delete),
    path('update/<int:post_id>',post_update),

    path('comment/write/<int:post_id>', comment_write),
    path('comment/update/<int:comment_id>', comment_update),
    path('comment/delete/<int:comment_id>', comment_delete),
]