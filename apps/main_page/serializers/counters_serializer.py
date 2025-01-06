from rest_framework import serializers
from ..models.counters_model import Counter


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = 'title number icon'.split()