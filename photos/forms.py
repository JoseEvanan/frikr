from django import forms
from django.core.exceptions import ValidationError
from nbformat import ValidationError

from photos.models import Photo
from photos.settings import BADWORDS


class PhotoForm(forms.ModelForm):
    """
    Formulario para el modelo photo
    """
    class Meta:
        model = Photo
        exclude = ['owner']
    
    def clean(self):
        """
        Valida si en la descripcion se han puesto tacos definidos
        :return: Diccionario con los attributos OK
        """
        cleaned_data = super(PhotoForm, self).clean()
        description = cleaned_data.get('description', '')

        for badword in BADWORDS:
            if badword.lower() in description.lower():
                raise ValidationError('La palabraa {0} no está permitida'.format(badword))
        #SI todo va OK, se devuelven todos lo datos
        return cleaned_data

        
