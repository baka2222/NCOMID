from rest_framework import serializers

from apps.main_page.models.general_structure_model import GeneralStructure

class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralStructure
        fields = ['id','title', 'description']
        
