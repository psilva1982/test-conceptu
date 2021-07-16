
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from acervo.api.serializers import CategorySerializer

from acervo.models import Category

class CategoryViewSet(viewsets.ModelViewSet):

    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    serializer_class = CategorySerializer

    queryset = Category.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('id', 'name')
    ordering = ('id',)