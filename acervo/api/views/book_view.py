
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from acervo.api.serializers import BookSerializer

from acervo.models import Book

class BookViewSet(viewsets.ModelViewSet):

    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    serializer_class = BookSerializer

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_fields = ('category'),
    search_fields = ('name', 'author')
    ordering_fields = ('id', 'name')
    ordering = ('name')

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(user=user)

    
    def perform_create(self, serializer):
        try: 
            serializer.save(user=self.request.user)
        except:
            raise serializers.ValidationError('Você já cadastrou um livro com este nome e autor.')
