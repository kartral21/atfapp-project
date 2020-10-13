from django.urls import path
from .views import (
    indexView,
    postUser,
)

urlpatterns = [
    # ... other urls
    path('', indexView),
    path('post/user', postUser, name = "post_user"),
    # ...
]