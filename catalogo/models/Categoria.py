from django.db import models

class Catalago (models.Model):

    nombre = models.CharField(max_length = 60)
    codigo = models.CharField(max_length = 60, null = True, blank = True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Caralogo'
        verbose_name_plural = 'Catalogos'

    def __str__(self):
        return self.nombre
