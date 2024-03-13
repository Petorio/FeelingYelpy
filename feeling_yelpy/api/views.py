from django.shortcuts import render
from rest_framework import generics, status
from .serializers import SearchSerializer, CreateSearchSerializer
from .models import Search
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class SearchView(generics.ListAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer

class CreateSearchView(APIView):
    serializer_class = CreateSearchSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            location = serializer.data.get('location')
            host = self.request.session.session_key
            queryset = Search.objects.filter(host=host)
            if queryset.exists():
                search = queryset[0]
                search.location = location
                search.save(update_fields=['location'])
                return Response(SearchSerializer(search).data, status=status.HTTP_200_OK)
            else:
                search = Search(host=host, location=location)
                search.save()
                return Response(SearchSerializer(search).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)