import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('SECRET_KEY')

ENVIRONMENT = os.getenv('STAGE', 'dev')
IS_STAGING = ENVIRONMENT == 'staging'
IS_PRODUCTION = ENVIRONMENT == 'production'
DEBUG = ENVIRONMENT == 'dev'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'landing',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

ROLLBAR = {
    'access_token': get_env_var('ROLLBAR_ACCESS_TOKEN'),
    'environment': ENVIRONMENT,
    'root': BASE_DIR,
    'exception_level_filters': [
        (Http404, 'ignored'),
    ]
}

ROOT_URLCONF = 'configuration.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'context_processors.template_visible_settings',
            ],
        },
    },
]

TEMPLATE_VISIBLE_SETTINGS = ['ENVIRONMENT']

WSGI_APPLICATION = 'configuration.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT', 3306),
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'CONN_MAX_AGE': 300,
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Detroit'
USE_I18N = True
USE_L10N = True
USE_TZ = True

if IS_PRODUCTION or IS_STAGING:
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]

BUCKET_PREFIX = os.getenv('BUCKET_PREFIX')
AWS_STORAGE_BUCKET_NAME = f'{BUCKET_PREFIX}-{ENVIRONMENT}'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_IS_GZIPPED = True
AWS_S3_CUSTOM_DOMAIN = f'static-{ENVIRONMENT}.piquantmag.com'

STATIC_URL = '/static/' if DEBUG else f'https://{AWS_S3_CUSTOM_DOMAIN}/'
ADMIN_URL = os.getenv('ADMIN_URL', r'^admin/')
