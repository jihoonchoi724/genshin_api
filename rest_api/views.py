
from rest_framework import viewsets
from rest_framework import permissions
from rest_api.models import Character
from rest_api.serializers import CharacterBasicSerializer, CharacterSerializer


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
