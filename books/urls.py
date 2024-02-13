from django.urls import path
from .views import BookListAPI

urlpatterns = [
    path('v1/book-list/', BookListAPI.as_view(), name='book-list'),
]
