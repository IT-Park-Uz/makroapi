from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductConfig(AppConfig):
    name = "common.product"
    verbose_name = _("Product")

    def ready(self):
      import common.signals
