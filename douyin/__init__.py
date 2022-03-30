import django

__title__ = 'GreaterWMS DouYin'
__version__ = '1.0.0'
__author__ = 'Elvis Shi'
__license__ = 'GPL v3'

VERSION = __version__

if django.VERSION < (3, 2):
    default_app_config = 'douyin.apps.DouyinConfig'
