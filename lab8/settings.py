DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'second_db',
        'USER': 'root',
        'PASSWORD': '123456789',
        'HOST': 'db',
        'PORT': '3306',
    }
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', 'web']