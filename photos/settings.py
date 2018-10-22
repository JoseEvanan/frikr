from django.conf import settings

COPYRIGTH = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

DEFAULT_LICENSES = (
    (COPYRIGTH, 'Copyrigth'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)

LICENSES = getattr(settings, 'LICENSES', DEFAULT_LICENSES)

BADWORDS = getattr(settings, 'PROJECT_BADWORDS', [])
