from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate



class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    profile_image = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'profile_image']

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        profile_image = self.validated_data.get('profile_image')

        if password != password2:
            raise serializers.ValidationError({'error': "Password doesn't match"})
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Sorry!! This email already exists"})
        
        account = CustomUser(username=username, email=email, first_name=first_name, last_name=last_name, profile_image=profile_image)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        if not user.is_active:
            raise serializers.ValidationError("Account is not active. Please confirm your email.")
        return user




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile_image']