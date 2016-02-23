import os

"""
oosyys/::::::::::::::::/:::://///:::::::::::-:-------:/++osooooooo+/::::::::::--
ooosyho:::::::::::/++osysoossssssssso+/::::-----------:/+osooo+//::------:::::--
ooosyss/::::::/++oosyhhyssyyyyhhyyyyyyys/++/:-----------:/oo+/::----------------
oooosso/::::/+ssosyyyhdyyhhyyyhddyssssysyyyhyo//----------:::-------------------
++///::::/+ssyyyyyyyhdmdmmddhyhhhmhysyyyssshhyyo/-------------------------------
///:::::/shyyyssysssyhdmmmmdddhhNdhhyyhyyyhhyyyso/:----------------------::-----
//:::/osyyhhyssssyhhhhhdmmmdmmmNNmmhysysyyyhhyyyysys/-----------------------:---
//:::+hhhyyhhyyhhyhddddmmNNmNmNMNNmdhhsyddmdyyyyyhddh/--------------------------
////oyhhhhyyhhhhdmNmNNNNmNNNNNNMMNmmmhdNNdmhdhhyhhdmmh/-------------------------
///ohhhhdhhyyhddmmNNNNNNNNNmmmNmmmdddmNNNNmmmhhhhhdmmds:------------------------
//+yddhdddhhdddmmmmmddddmdddddmmddmmmmNmmmmmmdhddmmmmmh/------------------------
//oddddddddddddhhhhyyysyhsssyhhdhhhddhhhhhhdddddmmmNNNd/------------------------
//sddmmdddddhsssssooo+osso++ossssssssssyyyhhdddmNNNNNNd:------------------------
//odmmmmdmmhsosooo++/+ooo+///+o++ooosssyyyyhhhdmNNNNNNy:------------------------
//odmmmmmddysssoo++//++++::::/+++++oosssyyhhhddmNNNNNNs-------------------------
//+dNNmmdddysssoo+++//++:::-::/+//++oosssyyhhddmmNNNNNh:------------------------
//+dmmNNmmdyssoooo++////:::::::///++ooossyyhhhdmNNNNNNy--:::--------------------
/:/omNNNNmdysssoooo++//:::::::::///++oosssyyyyhdNNNNNNd::/+o+/:::---------------
:::/hmNNNmhysssooo++//::-::--:---://+ooosssyyyyhmNNNNNm:/+oooo+oo++//:----------
/:::+hmNmmhysooooo++//:--::--::::///+oossyyyyyyhdmNNNNd//++++oooosys+:----------
:::::+dmmmhysooooo++++/////::/+/+osyhddddhhhhhhhhdNNNNs//++oosso+oso/:----------
::::::ymmmdsooosyhhhhhhhyso+//oosyhddmddhyyhhyyyyhmmmm++oooooso+osy+:-----------
::::::/yhmdoooosysssyddyysso/:+osyso/syyssysssssyhmmmy+oosssoooo+ss/:::--:::----
:::::::+yhdooooooyyohhy++/+++:/oss+///+++o+ooossyhdmdy:://+oooooos+::::::::-----
:::::::/oshso++oo+++++/+//+++//osso+//////++ooosyhdddo::::::::/+++::::::::::::--
:::::::::/ssoo++//////:::/++++/+ssso+/:::/++oooshddhy/::::::::::::::::::::::::::
:::::::---/ooo++////::::///+++//ossso+//://++osyhddho:::::::::::::::::::::::::::
::::::----:/+++++////:://++++//:+ossso+///++oosyhdy/::::::::::::::::::::::::::::
::::::------/++++/////://+++++/:/ohyhs+++oooosyyhd/:::::::::::::::::::::::::::::
::::::-------:++++//////+//osoooohmhyssoooosooyyhh::::::::::::::::::::::::::::::
:::::---------:+++++++++/++ooossssyyyssssssssoyyhh::::::::::::::::::::::::::::::
::::-----------/o++++++++ooooo++++osssyysssosoyyhs::::::::/:::::::::/:::::::::::
::::------------+o++++ooosososssosysyhysooosysyhmh::::://:/::::::::////:::::::::
::::-------------+o++++oo+osssoo+++ssssoossyyyhdNm+::://////////:///////::::::::
:::---------------+oooooo+++oosooossyysoossyhhdNNmmds+///////////////////:::::::
::::--------------:osoooooo++ooososssooossyhdmmmmmmmNmds+///////////////::::::::
::::---------------+ossssooo+++++/+++oossyhdmmmddddddmNNmdyo//////////////::::::
:::---------------+sooosyysoooo++//++osyyddmmddddddhhhdNNNNmdhssooo+///////:::::
:::-------------/smhooooosyyysoooooossyyhdmddhhhhhhhyyyhmNNNNNNNmNmmdyssoo+//:::
:::::---------/sdmNsoooooooosyyyyyyyyhhddddhyyyyyyyyysssymNmmNNNNNNNNNNNNmmddhso
:::::::::///+sdmmmNs+ooooo+++oosyyyyyyyhhyysssyyyssssssssymmmmmNNNmNNNNNNNNmmmmm
:///+++ooyhdmmmmmNNy++oooo++++++oooossssssooossssssooooosshmmmmmNNmmmNNNNmNNmmmm
/+++oshdmmmmmmNmmNNy++++++++++++++++ooooo+++ooooooooooooo+/hmmmmNNmNNNNmmNNmmmmm
+oyhdmmmNmmmmmmmmmNh+++++++++++++++++++/////++oooooooooo/--/dmmmNNmNNNmmmmmNmmmm
dmmmmmmmmmmmmmmmmmNdo+++++++///////++++//++++++o+++o++/-...-ydmNNNmmmmmmmmmmmmmm
mmmmmmmmmmmmmmmmmmNho++++///////++/+++++++++++++++++/-....../ddmNNM the kevin mm
NNNNmmmmmmmmmmmmmmNh+///////////++//+++++++///++//:.........-ddmNNNNNmmmmmNmmmmm
NNNmmmmmmmmmmmmmmmNh////////////+++///+///////:-.............sdmNNNmNmmmNNNmmmmm
mmmmmmmmmmmmmmmmmmNh////////////++++/////::--................+dmmNNNNmmmmNNmmmmm
mmmmmmmmmmmmmmmmmmms-..----:::::::::--.......................:ddmNNNmmmmmNNmmmmm
mmmmmmmmmmmmmmmmmmmy....``...................................-hdmNNNNNmmmmNmmmmN
mmmmmmmmmmdmmmmmdmmh-..``...............`..`.```````...`......yddmNNNNmmNmNmmmmm
mmmmmmmmmddddmmmmmmd:.```````````````````````````````````.....sddmmNNNmmmmmNmmmm
NmNmmmddmmddddmmmdmm+.....``````````````.````````````````.....oddmmNNNmmmmmNmmmm
NNmNmmddmdddddddddmms................`..`````````````````.....+ddmmNNNNmmmmmmmmm
Nmmmmmddddhhhddddddds-.....``....````````````````````````..``./hddmmmmmmmmmmmmmm
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# sorry github ninjas - this gets regenned before it's real :(
SECRET_KEY = 'r7-$l0dtu_*on%((#s$lkbi^_-^469_!(33_5f-pp$x*#f#dez'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api'
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
}

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.jonathanadamski.com'
EMAIL_HOST_USER = 'noreply@jonathanadamski.com'
EMAIL_HOST_PASSWORD = 'notreal'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ROOT_URLCONF = 'storybook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/Users/jon/Projects/storybook/'],
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


WSGI_APPLICATION = 'storybook.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storybook',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
