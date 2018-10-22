
from django.core.exceptions import ValidationError

from photos.settings import BADWORDS


def badwords_detector(value):
    """
    Valida si en value se han puesto tacos en settings.BADWORDS
    :return: Boolean
    """
    print("ENTRA A FUNCION")
    for badword in BADWORDS:
        if badword.lower() in value.lower():
            print("ERROR")
            raise ValidationError(
                'La palabraa {0} no está permitida'.format(badword))
    #SI todo va OK, se devuelven todos lo datos
    return True