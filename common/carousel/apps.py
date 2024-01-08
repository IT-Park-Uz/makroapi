from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CarouselConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'common.carousel'
    verbose_name = _("Carousel")