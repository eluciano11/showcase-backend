from rest_framework.response import Response
from rest_framework import generics

from django.shortcuts import get_object_or_404

from . import serializers
from .models import User
from ..utils.views import RetrieveUpdateView


class LoginView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.SigninSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.DATA)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class SignupView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.SignupSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.DATA)
        print request.DATA
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class ForgotPasswordView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.ForgotPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.DATA)
        serializer.is_valid(raise_exception=True)
        serializer.send_password_reset_email()
        return Response(serializer.validated_data)


class ResetPasswordView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.ResetPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.DATA)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


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


class UsersView(generics.ListAPIView):
    model = User
    serializer_class = serializers.UserSimpleSerializer
    queryset = User.objects.all()
    authentication_classes = ()
    permission_classes = ()


class SpecificUserView(generics.RetrieveAPIView):
    model = User
    serializer_class = serializers.UserSimpleSerializer
    lookup_field = 'id'
    authentication_classes = ()
    permission_classes = ()

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs['id'])
