from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DiscountConfig(AppConfig):
    name = "common.discount"
    verbose_name = _("Discount")
