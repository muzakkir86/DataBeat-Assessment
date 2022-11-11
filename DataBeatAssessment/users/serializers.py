from rest_framework import serializers
from .models import User


# UserRegistrationSerializer class to perform user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password']

    extra_kwargs = {
        'password': {'write_only': True}
    }

    # validating password and confirm password are same or not
    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError('Password and confirm password are not same')

        return attrs

    '''
        If password and confirm password are same
        Creating user
    '''

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# UserLoginSerializer to perform login
class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'password']



