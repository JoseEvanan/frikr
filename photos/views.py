from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

from photos.forms import PhotoForm
from photos.models import PUBLIC, Photo


# Create your views here.

def home(request):
    """
    Esta función devuelve elhome de mi página
    """
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {}
    context['photos'] = photos[:5]
    return render(request, 'photos/home.html', context)

def detail(request, pk):
    """
    Carga la página de detalle de una foto
    :param request: HttpRequest
    :param pk: id de la photo
    :return: HttpResponse
    """
    possible_photos = Photo.objects.filter(pk=pk)
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

@login_required()
def create(request):
    """
    Muestra un formulario para crea una foto y la crea si la peticion es POST
    :param request: HttpRequest
    :return: HttpResponse
    """
    error_messages = []
    success_message = []
    if request.method == "POST":
        photo_with_owner = request.user #usuario autenticado
        form = PhotoForm(request.POST, instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save() #Guarda el objeto y devolver
            form = PhotoForm()
            success_message = "Guardado con éxito!"
            success_message += "<a href='{0}'>".format(
                reverse('photo_detail', args=[new_photo.pk]))
            success_message += "Ver foto"
            success_message += "</a>"
    else:
        form = PhotoForm()
    context = {
        'errors': error_messages,
        'success_message': success_message,
        'form': form
    }
    return render(request, 'photos/new_photo.html', context)
