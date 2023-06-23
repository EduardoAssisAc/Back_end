from django.contrib import admin
from agenda.models import Local, Convidado, Compromisso


class ConvidadosInline(admin.TabularInline):
    model = Compromisso.convidados.through


class ConvidadoAdmin(admin.ModelAdmin):
    inlines = [ConvidadosInline,
    ]


class CompromissoAdmin(admin.ModelAdmin):
    inlines = [ConvidadosInline,
    ]
    exclude = ['convidados']


# Register your models here.
admin.site.register(Compromisso, CompromissoAdmin)
admin.site.register(Local)
admin.site.register(Convidado, ConvidadoAdmin)


