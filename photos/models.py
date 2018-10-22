from django.contrib.auth.models import User
from django.db import models

from photos.settings import LICENSES
from photos.validators import badwords_detector


# Create your models here.


PUBLIC = 'PUB'
PRIVATE = 'PRI'

VISIBILITY = (
    (PUBLIC, 'Pública'),
    (PRIVATE, 'Privada')
)

class Photo(models.Model):
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(
        blank=True, null=True, default="", validators=[badwords_detector])
    created_at = models.DateTimeField(auto_now_add=True)#guarda en el momento que se crea
    modified_at = models.DateTimeField(auto_now=True)#guarda cuando se modifica
    license = models.CharField(max_length=3, choices=LICENSES)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)
    #_methos pethod privado
    #__ method metodos reservados
    def __str__(self):
        return self.name
