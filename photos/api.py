from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from photos.models import Photo
from photos.serializers import PhotoListSerializer, PhotoSerializer
from photos.views import PhotosQueryset


"""
class PhotoListAPI(APIView):
    def get(self, request, *args, **kwargs):
        photos = Photo .objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)
"""


class PhotoListAPI(ListCreateAPIView, PhotosQueryset):
    queryset = Photo.objects.all().order_by('id')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    #serializer_class = PhotoListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PhotoListSerializer
        else:
            return PhotoSerializer
            
    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PhotoDetailAPI(RetrieveUpdateDestroyAPIView, PhotosQueryset):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_photos_queryset(self.request)
