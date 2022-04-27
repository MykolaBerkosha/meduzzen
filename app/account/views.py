from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from django.contrib.auth.models import User, UserManager


class AccountsAPI(APIView):

    permission_classes = (IsAdminUser, )

    def get(self, request):
        try:
            user = User.objects.get(id=request.GET.get('user_id'))
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

    def post(self, request):

        user = UserManager.objects.create()

        return Response({
            'status': 'OK',
            'user_id': user.pk
        })