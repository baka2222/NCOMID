import environ
from pathlib import Path

env = environ.Env()
environ.Env.read_env()
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT', cast=int),
    }
}

