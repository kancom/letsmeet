from letsmeet.settings.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': '127.0.0.1',
        'NAME': 'lmeet_db',
        'USER': 'lmeet_user',
        'PORT': 8088,
        'PASSWORD': 'tridect'
    },
}

MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("mapCenterLocationName", "moscow, ru"),
        # ("GooglePlaceAutocompleteOptions", {
        #     'componentRestrictions': {
        #         'country': 'uk'
        #     }
        # }),
        ("markerFitZoom", 12),
    ),
    "GOOGLE_MAP_API_KEY":
    "AIzaSyDHkpCBqGeGr9CWhMdfAoEvw8cNXJlD98M"
}

ALLOWED_HOSTS = ['*']

LANGUAGE_CODE = 'ru'
