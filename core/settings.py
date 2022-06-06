from corsheaders.defaults import default_headers
import os, environ

from pathlib import Path
env =  environ.Env()
environ.Env.read_env()
DEBUG=env('DEBUG')
SECRET_KEY=env('SECRET_KEY')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #3rdPary
    'core',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    #DevApps
    'apps.Empresa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #whitenoise
      'whitenoise.middleware.WhiteNoiseMiddleware',
    #corsHeaders
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default':{
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'd4gj9uaq4gjt7g',
    'USER': 'jdakwhxqqmttrk',
    'PASSWORD': '9a719803cc34192654478c4278e5b22b9a36878d2b7258c9504d9ea9989cc4e5',
    'HOST': 'ec2-52-54-212-232.compute-1.amazonaws.com',
    'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_WHITELIST=(
    #Allow_VueJS_COMMS
    'http://127.0.0.1:8080',
    'http://localhost:8080',
    #Allow_Django_COMMS
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    #Add The other sites needed
    #ex: http://www.mysite.com/
    )

CORS_ALLOW_HEADERS = list(default_headers) + [
'contenttype',
]

REST_FRAMEWORK = {
    'DEFAUTL_PERMISSION_CLASSES':[
    'rest_framework.permissions.AllowAny',]
}


#Heroku config
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

#STATICFILES config
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#DatabaseConfig
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
