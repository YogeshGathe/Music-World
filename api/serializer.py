from rest_framework import serializers
from .models import Chord

#serializer for chords.

class ChordSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    singer = serializers.CharField(max_length=100)
    chord = serializers.CharField(max_length=10)

    def create(self, validate_data):
        return Chord.objects.create(**validate_data)


    def update(self, instance, validated_data):
        instance.title=validated_data.get('title', instance.title)
        instance.singer=validated_data.get('singer', instance.singer)
        instance.chord=validated_data.get('chord', instance.chord)
        instance.save()
        return instance


