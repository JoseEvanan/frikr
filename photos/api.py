from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from photos.models import Photo
from photos.serializers import PhotoListSerializer, PhotoSerializer


"""
class PhotoListAPI(APIView):
    def get(self, request, *args, **kwargs):
        photos = Photo .objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)
"""


class PhotoListAPI(ListCreateAPIView):
    queryset = Photo.objects.all().order_by('id')
    #serializer_class = PhotoListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PhotoListSerializer
        else:
            return PhotoSerializer
            

class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
