from django import forms

from photos.models import Photo


class PhotoForm(forms.ModelForm):
    """
    Formulario para el modelo photo
    """
    class Meta:
        model = Photo
        exclude = ['owner']