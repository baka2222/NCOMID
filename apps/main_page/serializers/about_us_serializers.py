from ..models.about_us_models import (AboutUs,
                                      Charter,
                                      Directorate,
                                      History,
                                      AboutNCOMID)
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['description']


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['description']

class CharterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charter
        fields = ['id', 'title', 'files']


class DirectorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directorate
        fields = ['id', 'name', 'description', 'photo']


class AboutNCOMIDSerializer(serializers.ModelSerializer):
    history = SerializerMethodField()
    about_us = SerializerMethodField()
    charter = CharterSerializer(many=True, read_only=True)
    directorate = DirectorateSerializer(many=True, read_only=True)
    
    class Meta:
        model = AboutNCOMID
        fields = ['id', 'history', 'about_us', 'charter', 'directorate']

    def get_history(self, obj):
        history = obj.history.first()
        return HistorySerializer(history).data if history else None 
    
    def get_about_us(self, obj):
        about_us = obj.about_us.first()
        return AboutUsSerializer(about_us).data if about_us else None