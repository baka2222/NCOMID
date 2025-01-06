from rest_framework import serializers
from ..models.news_model import New


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['id', 'title', 'text', 'created_at', 'img']

        