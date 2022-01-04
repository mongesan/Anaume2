from django.shortcuts import render
from cms.models import Note
from rest_framework import viewsets, permissions
from REST_API.serializers import UserSerializer, NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('title')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAdminUser]

