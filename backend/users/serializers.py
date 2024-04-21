from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer


User = get_user_model()

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "email", "first_name", "last_name" , "password"]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }