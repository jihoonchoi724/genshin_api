from rest_framework import serializers
from rest_api.models import Character, Talent, Constellation


class CharacterBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ["character_id", "name", "vision", "weapon", "nation", "rarity",
                  "birthday", "release_version", "title", "affiliation", "constellation_name"]


class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = ["order", "talent_type", "talent_name", "talent_desc"]


class ConstellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constellation
        fields = ["con_number", "con_name", "con_desc"]


class CharacterSerializer(serializers.ModelSerializer):
    talents = TalentSerializer(many=True)
    constellations = ConstellationSerializer(many=True)

    class Meta:
        model = Character
        fields = ["character_id", "name", "vision", "weapon", "nation", "rarity", "birthday",
                  "release_version", "title", "affiliation", "constellation_name", "talents",
                  "constellations"]

    def create(self, validated_data):
        talents_data = validated_data.pop("talents")
        constellations_data = validated_data.pop("constellations")
        character = Character.objects.create(**validated_data)

        for talent in talents_data:
            Talent.objects.create(character=character, **talent)

        for constellation in constellations_data:
            Constellation.objects.create(character=character, **constellation)

        return character
