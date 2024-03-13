from rest_framework import serializers
from .models import Search

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ('id','host','location','limit','open_now','term','price','created_at')

class CreateSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ('location',)