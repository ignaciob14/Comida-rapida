from django.contrib import admin
from .models import ComidaRapida

@admin.register(ComidaRapida)
class ComidaRapidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'tamanio', 'disponible') 
    list_filter = ('categoria', 'disponible') 
    search_fields = ('nombre',)  
