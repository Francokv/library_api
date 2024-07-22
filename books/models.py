from django.db import models

class Author (models.Model):
    
    first_name = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Apellido'
    )

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Autor'
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# Crea aquí tu modelo de Book (Libro)
# debe tener los siguientes campos:
# title: Texto
# author: ForeignKey
# publication_year: Entero
# rating: Flotante
# pages: Entero

