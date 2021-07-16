from rest_framework import routers

from acervo.api.views.book_view import BookViewSet
from acervo.api.views.category_view import CategoryViewSet

router = routers.DefaultRouter()

router.register(r'books', BookViewSet, basename='books'),
router.register(r'categories', CategoryViewSet)