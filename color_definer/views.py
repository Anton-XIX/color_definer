from rest_framework.views import APIView
from .models import UserImage
from .serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status


class ImageUploaderView(APIView):
    queryset = UserImage.objects.all()
    parser_classes = [MultiPartParser]
    serializer_class = ImageSerializer

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"Color code for your image": UserImage.objects.all().last().color})
            # return Response(serializer.data,status=status.HTTP_201_CREATED,content_type='multipart/form-data',)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
