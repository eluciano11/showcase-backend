from django.utils.encoding import smart_str
from django.contrib.auth import authenticate
from django.utils.text import slugify

from rest_framework import serializers

from .models import User


class SigninSerializer(serializers.Serializer):
    """
    Serializer that handles signin endpoint data.
    """
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(min_length=6, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        self.user = authenticate(email=email, password=password)

        if self.user and self.user.is_active:
            return UserSerializer(self.user).data
        else:
            msg = 'Unable to login with provided credentials.'
            raise serializers.ValidationError(msg)


class UserSerializer(serializers.ModelSerializer):
    """
    Serializers used for User objects.
    """

    class Meta:
        model = User
        base_key = 'user'
        fields = ('id', 'email', 'first_name', 'last_name',
                  'gravatar_url', 'token', 'created_at', 'slug')


class UserSimpleSerializer(serializers.ModelSerializer):
    """
    Serializers used for User objects.
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'gravatar_url', 'created_at', 'slug')


class SignupSerializer(serializers.ModelSerializer):
    """
    Serializers used to create a user.
    """
    email = serializers.EmailField(max_length=40)
    password = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', )

    def validate_email(self, value):
        is_found = User.objects.filter(email__iexact=value)

        if is_found:
            message = 'Email already in use'
            raise serializers.ValidationError(message)

        return value

    def validate_password(self, value):
        if value:
            value = smart_str(value)

        return value

    def create_user(self, attrs):
        email = attrs['email']
        password = attrs['password']
        first_name = attrs['first_name']
        last_name = attrs['last_name']

        user = User.objects.create_user(
            email, first_name, last_name, password)
        user.save()

        return user

    def validate(self, attrs):
        user = self.create_user(attrs)
        return UserSerializer(user).data


class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    Serializer that handles change password in user settings endpoint.
    """
    current_password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(min_length=6, write_only=True)
    password2 = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('current_password', 'password1', 'password2')

    def validate_current_password(self, value):
        user = self.instance

        if user and not user.check_password(value):
            msg = 'Current password is invalid.'
            raise serializers.ValidationError(msg)

        return value

    def validate_password2(self, value):
        password_confirmation = value
        password1 = self.initial_data['password1']

        if password_confirmation != password1:
            msg = "Password doesn't match the confirmation."
            raise serializers.ValidationError(msg)

        value = smart_str(password_confirmation)

        return value

    def update(self, instance, validated_data):
        instance.change_password(validated_data.get('password2'))
        return {
            "change_password": True
        }


class ForgotPasswordSerializer(serializers.Serializer):
    """
    Serializer that handles forgot password endpoint.
    """
    email = serializers.EmailField(max_length=254)

    def validate_email(self, value):
        try:
            self.user = User.objects.get(email__iexact=value)
        except User.DoesNotExist:
            msg = 'No user found.'
            raise serializers.ValidationError(msg)

        return value

    def send_password_reset_email(self):
        self.user.send_password_reset_email()


class ResetPasswordSerializer(serializers.Serializer):
    """
    Serializer that handles reset password endpoint.
    """
    token = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate_new_password(self, value):
        if value:
            value = smart_str(value)
        return value

    def validate_token(self, value):
        self.user = User.objects.get_from_password_reset_token(value)
        if not self.user:
            msg = 'Invalid password reset token.'
            raise serializers.ValidationError(msg)

        return value

    def validate(self, attrs):
        self.user.change_password(attrs['new_password'])

        return {
            'password_reset': True,
        }


class UserSettingsSerializer(serializers.ModelSerializer):
    """
    Serializer that handles user settings endpoint.
    """
    first_name = serializers.CharField(required=False, max_length=30)
    last_name = serializers.CharField(required=False, max_length=30)
    token = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name',
            'gravatar_url', 'created_at', 'token', 'slug'
        )

    def validate_email(self, value):
        email = value.lower()
        user = self.context['request'].user

        users = User.objects.filter(
            email__iexact=email).exclude(pk=user.id)

        if users.exists():
            msg = 'Email already exists.'
            raise serializers.ValidationError(msg)

        return value

    def validate(self, data):
        user = User.objects.get(pk=self.context['request'].user.id)

        if (user.first_name.lower() != data['first_name'].lower() or
                user.last_name.lower() != data['last_name'].lower()):

            full_name = data['first_name'] + ' ' + data['last_name']
            slug = slugify(full_name)

            unique = False
            count = 2

            while not unique:
                users = User.objects.filter(
                    slug__iexact=slug).exclude(pk=user.id)

                if users.exists():
                    slug += '-' + str(count)
                    count += 1

                else:
                    data['slug'] = slug
                    unique = True

        return data
