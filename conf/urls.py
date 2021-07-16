from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.authtoken import views

from security.token import TokenView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from acervo.urls import router as acervo_router

urlpatterns = [
    #path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('', include(acervo_router.urls))
]
