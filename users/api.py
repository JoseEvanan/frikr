from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404

"""
#View personalizada
class UserListAPI(View):
    def get(self, request, *args, **kwargs):
        users = User .objects.all()
        serializer = UserSerializer(users, many=True)
        serialized_users = serializer.data
        renderer = JSONRenderer()
        json_users = renderer.render(serialized_users)#Lista de diccionarios -> JSON
        return HttpResponse(json_users)"""

class UserListAPI(APIView):
    def get(self, request, *args, **kwargs):
        """
        API users
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response (serializer.data)
    
    def post(self, request):
        """
        Crea la foto 
        :param request: HttpRequest
        :return: HttpResponse
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                           status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):
    def get(self, request, *args, **kwargs):
        """
        API users
        """
        user = get_object_or_404(User, pk=kwargs.get('pk')) #Leer como retorna si salir del metodo
        serializer = UserSerializer(user)
        return Response (serializer.data)
    
    def put(self, request, *args, **kwargs):
        """
        API users
        """
        user = get_object_or_404(User, pk=kwargs.get(
            'pk'))  # Leer como retorna si salir del metodo
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        API users
        """
        user = get_object_or_404(User, pk=kwargs.get(
            'pk'))  # Leer como retorna si salir del metodo
        user.delete()
        #serializer = UserSerializer(instance=user, data=request.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
