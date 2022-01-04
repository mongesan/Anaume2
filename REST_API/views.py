from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from REST_API.serializers import UserSerializer, NoteSerializer
from REST_API.models import Note


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('title')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAdminUser]
