from django.contrib import admin
from .models import Commande, CommandeArticle

# Register your models here.

admin.site.register(Commande)
admin.site.register(CommandeArticle)

class CommandeArticleInline(admin.StackedInline):
    model = CommandeArticle
    extra = 0

class CommandeAdmin(admin.ModelAdmin):
    model = Commande
    inlines = [CommandeArticleInline]
    readonly_fields = ('date_ordered',)

admin.site.unregister(Commande)
admin.site.register(Commande, CommandeAdmin)
