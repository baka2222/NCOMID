from rest_framework import serializers
from ..models.contacts_model import Contacts, SocialMedia

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = 'id title text icon'.split()


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = 'id title url icon'.split()