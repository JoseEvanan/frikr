from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()  # read only
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Crea una isntancia de user a partir de los datos de 
        validated_data que contiene valores deserializados
        :param valdiated_data: Dicionario de datos de usuario
        :return: objeto user.
        """
        instance  = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza  una instancia de User a partir de los datos del diccionario 
        validated_data que contine valores deserializados
        :param instance: objeto User a actualizar
        :param validated_data: Dicionario de datos de usuario
        :return: objeto user.
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))

        instance.save()
        return instance

    def validate_username(self,data):
        """
        Valida si existe un usuario con ese nombre
        """
        print(data)
        user = User.objects.filter(username=data)
        
        #Si estoy creado ( no hay instancia) comprobar si hay usuarios con ese username
        
        if not self.instance and len(user) != 0:
            raise serializers.ValidationError(
                " Ya existe un usuario con ese username ")
        #Si estoy actualizando, el nuevo username es diferene  al de la instancia( esta cambaido el userna,e)
        # y ecise usuarios registrados con ese nuevo username
        elif self.instance and self.instance.username != data and len(user) != 0:
            raise serializers.ValidationError(
                " Ya existe un usuario con ese username ")
        else:
            return data
            #965079339

        
