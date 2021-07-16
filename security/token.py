from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class TokenSerializer(TokenObtainPairSerializer):

    default_error_messages = {
        'no_active_account': ('Usuário ou senha inválidos.')
    }

    @classmethod
    def get_token(cls, user):

        token = super(TokenSerializer, cls).get_token(user)
        
        # Add custom claims
        token['login'] = user.username

        
        return token


class TokenView(TokenObtainPairView):

    serializer_class = TokenSerializer