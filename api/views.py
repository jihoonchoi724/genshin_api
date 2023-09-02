from django.shortcuts import render
from api.models import Character
from api.serializers import CharacterBasicSerializer, CharacterSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

class CharacterViewSet(viewsets.ModelViewSet):
  queryset = Character.objects.all().order_by("name")
  serializer_class = CharacterBasicSerializer
  detail_serializer_class = CharacterSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def get_serializer_class(self):
    if self.action == 'retrieve':
      if hasattr(self, 'detail_serializer_class'):
        return self.detail_serializer_class
    return super(CharacterViewSet, self).get_serializer_class()

class AddCharacterViewSet(viewsets.ModelViewSet):
  queryset = Character.objects.all().order_by("name")
  serializer_class = CharacterSerializer
  permission_classes = [permissions.IsAuthenticated]