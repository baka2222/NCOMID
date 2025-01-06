from rest_framework import serializers
from ..models.banners_model import Banner

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id','title', 'text', 'img']