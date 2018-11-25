from rest_framework import serializers

class TestSerializer(serializers.Serializer):
    hoge = serializers.CharField()
    fuga = serializers.CharField(max_length=200)
    created = serializers.DateTimeField(required=False)
