from django.db.models import fields
from rest_framework import serializers
from wines.models import Wine

# wine serializer


class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = '__all__'
