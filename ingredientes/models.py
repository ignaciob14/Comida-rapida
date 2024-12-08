from django.db import models

class ComidaRapida(models.Model):
    nombre = models.CharField(
        max_length=100, 
        verbose_name="Nombre del Producto"
    )

    categoria = models.CharField(
        max_length=50,
        choices=[
            ('Hamburguesas', 'Hamburguesas'),
            ('Pizzas', 'Pizzas'),
            ('Bebidas', 'Bebidas'),
            ('Postres', 'Postres')
        ],
        default='Hamburguesas',
        verbose_name="Categoría"
    )

    precio = models.PositiveIntegerField(
        null=False,
        verbose_name="Precio (CLP)"
    )

    ingredientes = models.TextField(
        verbose_name="Ingredientes Principales",
        help_text="Ejemplo: Carne, queso, tomate, lechuga"
    )

    tamanio = models.CharField(
        max_length=200,
        choices=[
            ('Chico', 'Chico'),
            ('Mediano', 'Mediano'),
            ('Grande', 'Grande')
        ],
        default='Mediano',
        verbose_name="Tamaño"
    )

    disponible = models.BooleanField(
        default=True,
        verbose_name="¿Disponible?"
    )

    def __str__(self):
        return f"{self.nombre} - {self.categoria} - {'Disponible' if self.disponible else 'No Disponible'}"
