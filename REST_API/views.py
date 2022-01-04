from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from REST_API.serializers import UserSerializer, NoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
