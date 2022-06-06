from django.db import models

# Create your models here.
class Sede(models.Model):
    sede =  models.CharField(max_length=50)

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"

    def __str__(self):
        return str(self.sede)

class Dependencia(models.Model):
    dependencia= models.CharField(max_length=50)

    class Meta:
        verbose_name = "Dependencia"
        verbose_name_plural = "Dependencias"

    def __str__(self):
        return str(self.dependencia)

class sedeDependencia(models.Model):
    sede=models.ForeignKey(Sede, on_delete=models.CASCADE)
    dependencia=models.ForeignKey(Dependencia, on_delete=models.CASCADE)
