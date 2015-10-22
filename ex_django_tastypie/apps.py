from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangoTastypieConfig(AppConfig):
    name = 'ex_django_tastypie'
    verbose_name = _("Django with Tastypie")
