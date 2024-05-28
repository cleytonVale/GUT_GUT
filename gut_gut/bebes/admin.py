from django.contrib import admin

from django.contrib import admin
from .models import Bebe, Alimentacao, TrocaDeFralda, Sono, ConsultaMedica

admin.site.register(Bebe)
admin.site.register(Alimentacao)
admin.site.register(TrocaDeFralda)
admin.site.register(Sono)
admin.site.register(ConsultaMedica)

