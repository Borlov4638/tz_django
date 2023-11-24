from rest_framework import generics
from .models import Image
from .serializers import ImageSerializer
from rest_framework.parsers import BaseParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser

class ImageView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [JSONParser]

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request, *args, **kwargs):
        # Обработка GET-запроса для получения списка изображений
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Обработка POST-запроса для создания нового изображения
        return self.create(request, *args, **kwargs)

class ImageRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
