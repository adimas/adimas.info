"""
Django settings for adimas project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# -*- coding: utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
gettext = lambda s: s
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^#c-ov(f6^6(5mwjsq29e=krjz(%$a5u4#qa1-s)r49z^n5!ke'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'tinymce',
    'taggit',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'adimas.urls'

WSGI_APPLICATION = 'adimas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'adimas_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
    }
}

TINYMCE_DEFAULT_CONFIG = {
    # General options
    'mode' : "textareas",
    'theme' : "advanced",
    'plugins' : "pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,wordcount,advlist,autosave",

    # Theme options
    'theme_advanced_buttons1' : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,fontselect,fontsizeselect,",  # fullscreen,code",
    'theme_advanced_buttons2' : "bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,|,forecolor,backcolor",
    # 'theme_advanced_buttons3' : "tablecontrols,|,hr,sub,sup,|,charmap",

    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_resizing' : 'true',

    # Example content CSS (should be your site CSS)
    # content_css : "/css/style.css",

    'template_external_list_url' : "lists/template_list.js",
    'external_link_list_url' : "lists/link_list.js",
    'external_image_list_url' : "lists/image_list.js",
    'media_external_list_url' : "lists/media_list.js",

    # Style formats
    'style_formats' : [
        {'title' : 'Bold text', 'inline' : 'strong'},
        {'title' : 'Red text', 'inline' : 'span', 'styles' : {'color' : '#ff0000'}},
        {'title' : 'Help', 'inline' : 'strong', 'classes' : 'help'},
        {'title' : 'Table styles'},
        {'title' : 'Table row 1', 'selector' : 'tr', 'classes' : 'tablerow'}
    ],

    'width': '700',
    'height': '400'
}



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATIC_URL = "/static/"
MEDIA_URL = "/media/"

TINYMCE_DEFAULT_CONFIG = {
  'file_browser_callback': 'mce_filebrowser'
}
TEMPLATE_DIRS = (
    # The docs say it should be absolute path: PROJECT_PATH is precisely one.
    # Life is wonderful!
    os.path.join(PROJECT_PATH, "templates"),
)
STATICFILES_DIRS = (
    # The docs say it should be absolute path: PROJECT_PATH is precisely one.
    # Life is wonderful!
   "/home/geroulia/workspace/adimas/static",
)
CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
)
LANGUAGES = [
    ('en', 'English'),
]
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)
