
import asyncio

from django.forms import model_to_dict
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from django.contrib.auth.models import User

from apps.accounts.forms import CreateUserForm
from apps.accounts.serializers import UpdateSerializer


class ListAPI(APIView):

    permission_classes = (IsAdminUser, )

    def get(self, request):

        user = User.objects.all().values()

        return Response({
            'user': list(user),
        })

    def post(self, request):

        form = CreateUserForm(data=request.data)

        if not form.is_valid():
            return Response({
                'status': 'ERROR',
                **dict(form.errors)
            })

        data = form.cleaned_data
        password = data.pop('password')

        user = User.objects.create(**data)
        user.set_password(password)
        user.save()

        return Response({
            'user': model_to_dict(user)
        })


class ObjectAPI(APIView):

    permission_classes = (IsAdminUser, )

    def get(self, request, user_id):

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({
                'status': "User not found"
            })

        if not user.is_active:
            return Response({
                'status': "User is not active"
            })

        return Response({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        })

    def patch(self, request):
        user = self.request.user
        serializer = UpdateSerializer(user, data=request.data, partial=True)
        print(user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({
                'status': "User not found"
            })

        user.delete()

        return Response({'status': 'User removed'})
