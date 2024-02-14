from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from books.models import Book
from .paginations import CustomPagination

from books.serializers import BookSerializer


class BookListAPI(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (JWTAuthentication,)
    pagination_class = CustomPagination

    def get_queryset(self):
        return Book.objects.all()
    
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
