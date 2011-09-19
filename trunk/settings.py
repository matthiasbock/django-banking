DEBUG = True
TEMPLATE_DEBUG = True 

ADMINS = (
    ('webmaster', 'webmaster@localhost'),
)

MANAGERS = ADMINS

from Django.databases import BankingDB

DATABASES = {
	    BankingDB: {
		'ENGINE': 'mysql',
		'NAME': BankingDB
		'USER': 'Django',
		'PASSWORD': 'Django-PW',
		'HOST': 'localhost',
		'PORT': '',
	    }
	}

TEMPLATE_DIRS = (
	'/var/www/Django/banking/templates',
)

LANGUAGE_CODE = 'de'
TIME_ZONE = 'Germany/Berlin'
USE_I18N = False

MEDIA_URL = '/banking/static/'
MEDIA_ROOT = '/var/www/Django/banking/static/'

SECRET_KEY = ''

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

ROOT_URLCONF = 'banking.urls'

INSTALLED_APPS = (
#    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
#    'django.contrib.admin',
    'banking.main',
)

LOGIN_URL = '/banking/Login'

