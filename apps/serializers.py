from rest_framework.serializers import ModelSerializer

from apps.models import User


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ()

class RegisterModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name','last_name','date_of_birth','address','phone_number','password']
