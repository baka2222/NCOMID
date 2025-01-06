from ..models.scientific_activity_models import (ScientificActivity,
                                                 ScientificActivityContent,
                                                 Document)
from rest_framework import serializers


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'pdf']


class ScientificActContentSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(read_only=True, many=True)
    id = serializers.SerializerMethodField()
    class Meta:
        model = ScientificActivityContent
        fields = ['id', 'title_content', 'text_content', 'documents']

    def get_id(self, obj):
        return f'section{obj.id}'



class ScientificActSerializer(serializers.ModelSerializer):
    content = ScientificActContentSerializer(many=True)
    class Meta:
        model = ScientificActivity
        fields = 'id title content img'.split()


class SASearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificActivity
        fields = 'id title img'.split()








