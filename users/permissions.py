from rest_framework.permissions import BasePermission




class UserPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Priemro en ejecutarse

        DEfine si el usuario authenticado en request.user tiene permiso para realizar el (GET, POST, PUT o DELETE)
        :param request:
        :param view:
        :return:
        """
        from users.api import UserDetailAPI
        #Si quiere crear u usuario sea quien sea, debe poder crearlo
        if request.method == "POST0":
            return True
        #si es superuser, puede acer lo que quiera
        elif request.user.is_superuser:
            return True
        # si no es POST( es GET, PUT o DELETE), el usuario no es superuser
        # la peticion va a la vista de detalle, entonces lo permitimos
        # para tomar la decision en el metodo has_object_permission
        elif isinstance(view, UserDetailAPI):
            return True
        #si la peticion es un GET de listado, o lo permitimos (porque s llega
        #aqui, el usuario o es superusuario y solo pueden los superuser)
        else:
            #GEt a /api/1.0/photos
            return False


    def has_object_permission(self, request, view, obj):
        """
        Segundo en ejecutarse

        SI el usuario authenticado tiene permissio para realizar la accion (GEt, PUT o DELETE)sobre el objeto  obj

        :param request:
        :param view:
        :param obj:
        :return:
        """
        return request.user.is_superuser or request.user == obj