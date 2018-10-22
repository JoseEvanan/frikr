from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, ListView
from django.db.models import Q

from photos.forms import PhotoForm
from photos.models import PUBLIC, Photo

class OnlyAuthenticatedView(View):
    def get(self, request):
        if request.user.is_authenticated:
            
            print("LOGEADO")
            return super(OnlyAuthenticatedView, self).get(request)
        else:
            print("NO LOGEADO")
            return redirect('users_login')
            #redirigir a login
    
    def post(self, request):
        if request.user.is_authenticated:
            return super(OnlyAuthenticatedView, self).get(request)
        else:
            redirect('home')
            #redirigir a login
            

#####
class PhotosQueryset(object):
    
    
    def get_photos_queryset(self,request):
        if not request.user.is_authenticated:
            photos = Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser:
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(Q(owner=request.user) |
                                          Q(visibility=PUBLIC))
        return photos


# Create your views here.
class HomeView(View):
    def get(self, request):
        """
        Esta función devuelve elhome de mi página
        """
        photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
        context = {}
        context['photos'] = photos[:5]
        return render(request, 'photos/home.html', context)


class DetailView(View, PhotosQueryset):
    @method_decorator(login_required())
    def get(self, request, pk):
        """
        Carga la página de detalle de una foto
        :param request: HttpRequest
        :param pk: id de la photo
        :return: HttpResponse
        """
        possible_photos =  self.get_photos_queryset(
            request).filter(pk=pk).select_related('owner')
        #JOIN Solo una llamada
        #sino haria dos llamdas para photo y para user
        #relacion reversa  prefec
        photo = possible_photos[0] if len(possible_photos) == 1 else None
        if photo:
            #Cargar template detatlle
            context = {
                'photo': photo
            }
            print(photo.owner)
            return render(request, 'photos/detail.html', context)
        else:
            return HttpResponseNotFound("NO existe la foto")


class CreateView(View):
    
    @method_decorator(login_required())
    def get(self, request):
        """
        Muestra un formulario para crea una foto 
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = PhotoForm()
        context = {
            'form': form
        }
        return render(request, 'photos/new_photo.html', context)
    
    @method_decorator(login_required())
    def post(self, request):
        """
        Crea la foto 
        :param request: HttpRequest
        :return: HttpResponse
        """
        error_messages = []
        success_message = ''
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user  # usuario autenticado
        form = PhotoForm(request.POST, instance=photo_with_owner)
        if form.is_valid():
            print("FORMULARIO VALIDO")
            new_photo = form.save()  # Guarda el objeto y devolver
            print(new_photo)
            print("GUARDAR OBJETO")
            form = PhotoForm()
            success_message = "Guardado con éxito!"
            success_message += "<a href='{0}'>".format(
                reverse('photo_detail', args=[new_photo.pk]))
            success_message += "Ver foto"
            success_message += "</a>"
        context = {
            'errors': error_messages,
            'success_message': success_message,
            'form': form
        }
        return render(request, 'photos/new_photo.html', context)


class PhotoListView(View, PhotosQueryset):
    def get(self, request):
        """
        Response:
        - The photos publics if user authenticated
        - The photos of user authenticared or publics other users
        - If user superadmin, all photos
        :param request: HttpRequest
        :return: HttpResponse
        """
        photos = self.get_photos_queryset(request)
        context = {
            'photos':photos
        }
        return render(request, 'photos/photos_list.html', context)


class UserPhotosView(ListView):
    model = Photo
    template_name = 'photos/user_photos.html'

    def get_queryset(self):
        queryset = super(UserPhotosView, self).get_queryset()
        return queryset.filter(owner=self.request.user)

