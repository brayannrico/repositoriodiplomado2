from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile (models.Model):
    Genero=((1,"M"),
            (2,"F"),
            (3,"O"),)
    documento=models.CharField(max_length=15)
    telefono=models.CharField(max_length=15)
    nacimiento=models.DateField()
    genero=models.SmallIntegerField(choices=Genero)
    user=models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        db_table='profile'


class Eps (models.Model):
    #Regimen=((1,"Contributivo"),
     #        (2,"Subsidiado"),)

    eps = models.CharField(max_length=50)


    class Meta:
        db_table='eps'


    def __str__(self):
        return self.eps


class Paciente (models.Model):
    eps=models.ForeignKey(Eps, on_delete=models.PROTECT)
    user = models.OneToOneField(User, on_delete=models.PROTECT)


    class Meta:
        db_table='paciente'


    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)



class Medico (models.Model):

    Especialidad=((1,"Alergología"),
              (2,"Cardiología"),
              (3,"Gastroenterología"),
              (4,"Medicina de urgencias"),
              (5,"Neurología"),
              (6,"Oftalmología"),)
    especialidad = models.SmallIntegerField(choices=Especialidad)
    user = models.OneToOneField(User, on_delete=models.PROTECT)


    class Meta:
        db_table='medico'

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class Agendamiento (models.Model):
    Tipocita=((1,"Medico general"),
              (2,"Odontologia"),
              (3,"Laboratorio"),)
    fecha=models.DateTimeField()
    tipocita = models.SmallIntegerField(choices=Tipocita)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)

    # Estado=((1,"Activa"),
    # (2,"En proceso"),)
    # Pago=((1,"Si"),
    # (2,"No"),)
    # estado = models.SmallIntegerfield(choices=Estado)
    # costo= models.CharField(max_length=10)
    # pago = models.SmallIntegerfield(choices=Pago)

    class Meta:
        db_table='agendamiento'
