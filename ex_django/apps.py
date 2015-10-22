from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangoConfig(AppConfig):
    name = 'ex_django'
    verbose_name = _("Django")
