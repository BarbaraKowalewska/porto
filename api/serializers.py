from rest_framework import serializers

from jobs.models import Job


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('image', 'summary')