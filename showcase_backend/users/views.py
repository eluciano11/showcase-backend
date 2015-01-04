from rest_framework.response import Response
from rest_framework import generics

from . import serializers
from .models import User
from ..utils.views import RetrieveUpdateView


class LoginView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.SigninSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.DATA)

        if serializer.is_valid():
            return Response(serializer.validated_data)

        return Response(serializer.errors)


class SignupView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.SignupSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.DATA)

        if serializer.is_valid():
            return Response(serializer.validated_data)

        return Response(serializer.errors)


class ForgotPasswordView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.ForgotPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.DATA)

        if serializer.is_valid():
            serializer.send_password_reset_email()
            return Response(serializer.validated_data)

        return Response(serializer.errors)


class ResetPasswordView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.ResetPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.DATA)

        if serializer.is_valid():
            return Response(serializer.validated_data)

        return Response(serializer.errors)


class UserSettingsView(RetrieveUpdateView):
    model = User
    serializer_class = serializers.UserSettingsSerializer

    def get_object(self):
        return self.request.user


class ChangePasswordView(generics.UpdateAPIView):
    model = User
    serializer_class = serializers.ChangePasswordSerializer

    def get_object(self):
        return self.request.user
