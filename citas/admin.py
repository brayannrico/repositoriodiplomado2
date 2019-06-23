from django.contrib import admin
from citas.models import Profile,Eps,Medico,Agendamiento,Paciente,User #LLAMAR LAS TABLAS MODELS.PY
# Register your models here.

@admin.register(Agendamiento)
class Adminagendamiento (admin.ModelAdmin):
    list_display = ('fecha','tipocita','Nombre_medico','Nombre_paciente',)

    def Nombre_medico(self,medicoN):
        return "%s %s" %(medicoN.medico.user.first_name,medicoN.medico.user.last_name)
    def Nombre_paciente(self,pacienteN):
        return "%s %s" %(pacienteN.paciente.user.first_name,pacienteN.paciente.user.last_name)


@admin.register(Profile)
class Adminprofile (admin.ModelAdmin):
    list_display = ('genero','documento','telefono','nacimiento',)


@admin.register(Eps)
class Admineps (admin.ModelAdmin):
    list_display = ('id','eps',)

@admin.register(Medico)
class Admimedico (admin.ModelAdmin):
    list_display = ('user','especialidad',)


@admin.register(Paciente)
class Adminpaciente (admin.ModelAdmin):
    list_display = ('user', 'eps',)






