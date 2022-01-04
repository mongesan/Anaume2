from django.contrib.auth.models import User
from rest_framework import serializers
from REST_API.models import Note


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['url', 'user', 'title']
