from rest_framework import serializers
from apps.main_page.models.resources_model import Journal, Link, Report, Resource

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id','title', 'url']
        
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id','title', 'url']


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id','title', 'url']


class JournalAndReportSerializer(serializers.ModelSerializer):
    journal = JournalSerializer(many=True, read_only=True)
    report = ReportSerializer(many=True, read_only=True)

    class Meta:
        model = Resource
        fields = ['id', 'journal', 'report']