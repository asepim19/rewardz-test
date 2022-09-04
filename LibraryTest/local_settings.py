DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library',
        'USER': 'postgres',
        'PASSWORD': 'a1s2e3p4',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}