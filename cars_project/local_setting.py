# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b==oy$k-)%fwno@q#jjr8*09tc(d1%qhinka=j+k1r5)1_*qzp'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD' : 'password',

    }
}