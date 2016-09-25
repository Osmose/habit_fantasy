import os

from configurations import Configuration, values


class Core(Configuration):
    """Settings that will never change per-environment."""
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # General Settings
    ROOT_URLCONF = 'habit_fantasy.urls'
    WSGI_APPLICATION = 'habit_fantasy.wsgi.application'
    DATABASES = values.DatabaseURLValue('sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))

    INSTALLED_APPS = [
        'habit_fantasy.base',

        'rest_framework',

        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

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

    # Django Rest Framework
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
        'PAGE_SIZE': 10,
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
        ),
    }

    # Static assets
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'assets'),
    )

    # Internationalization
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True


class Base(Core):
    """Settings that may change per-environment, some with defaults."""
    # General settings
    DEBUG = values.BooleanValue(False)

    # Security settings
    SECRET_KEY = values.SecretValue()
    ALLOWED_HOSTS = values.ListValue([])
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    ]
    PASSWORD_HASHERS = values.ListValue([
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    ])


class Development(Base):
    """Settings for local development."""
    SECRET_KEY = values.Value('-)0f70plr2kzr!&qh(t(!eng15^$deqm)5348+wf_z7)eeo4)!')
    DEBUG = values.BooleanValue(True)
    AUTH_PASSWORD_VALIDATORS = values.ListValue([])
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
