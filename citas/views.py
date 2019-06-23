from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Agendamiento,Eps,Paciente,Medico,Profile
from .forms import Formulariocita,Formularioeps,Formulariopaciente,Formulariomedico,Formularioprofile
# Create your views here.

class Viendocitas(PermissionRequiredMixin,ListView):
    permission_required = 'citas.view_agendamiento'
    login_url = 'login'
    model = Agendamiento
    template_name = 'vercita.html'

    def get_queryset(self):
        queryset = super(Viendocitas, self).get_queryset()

        if self.request.user.groups.filter(name="Paciente").exists():
            queryset=queryset.filter(paciente__user=self.request.user)

        if self.request.user.groups.filter(name="Medico").exists():
            queryset=queryset.filter(paciente__user=self.request.user)

        return queryset

class Insertarcita(PermissionRequiredMixin,FormView):
    permission_required = 'citas.add_agendamiento'
    login_url = 'login'
    form_class = Formulariocita
    template_name = 'insertarcita.html'
    success_url = '/vercita/'

    def form_valid(self, form):
        form.save()
        return super() .form_valid(form)

class Editcita(PermissionRequiredMixin,UpdateView):
    permission_required = 'citas.change_agendamiento'
    login_url = 'login'
    model = Agendamiento
    form_class = Formulariocita
    template_name = 'editcita.html'
    success_url = '/vercita'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Elimcita(PermissionRequiredMixin,DeleteView):
    permission_required = 'citas.del_agendamiento'
    login_url = 'login'
    model = Agendamiento
    template_name = 'elimcita.html'
    success_url = '/vercita'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Viendoeps(PermissionRequiredMixin,ListView):
    permission_required = 'citas.view_eps'
    login_url = 'login'
    model = Eps
    template_name = 'vereps.html'
    def get_queryset(self):
        queryset = super(Viendoeps, self).get_queryset()

        if self.request.user.groups.filter(name="Paciente").exists():
            queryset=queryset.filter(paciente__user=self.request.user)

        if self.request.user.groups.filter(name="Medico").exists():
            queryset=queryset.filter(paciente__user=self.request.user)

        return queryset

class Insertareps(PermissionRequiredMixin,FormView):
    permission_required = 'citas.add_eps'
    login_url = 'login'
    form_class = Formularioeps
    template_name = 'insertareps.html'
    success_url = '/vereps/'

    def form_valid(self, form):
        form.save()
        return super() .form_valid(form)

class Editeps(PermissionRequiredMixin,UpdateView):
    permission_required = 'citas.change_eps'
    login_url = 'login'
    model = Eps
    form_class = Formularioeps
    template_name = 'editeps.html'
    success_url = '/vereps'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Elimeps(LoginRequiredMixin,DeleteView):
    permission_required = 'citas.del_eps'
    login_url = 'login'
    model = Eps
    template_name = 'elimeps.html'
    success_url = '/vereps'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Viendopaciente(PermissionRequiredMixin,ListView):
    permission_required = 'citas.view_paciente'
    login_url = 'login'
    model = Paciente
    template_name = 'verpaciente.html'
    def get_queryset(self):
        queryset = super(Viendopaciente, self).get_queryset()

        if self.request.user.groups.filter(name="Paciente").exists():
            queryset=queryset.filter(paciente__user=self.request.user)

        if self.request.user.groups.filter(name="Medico").exists():
            queryset=queryset.filter(paciente__user=self.request.user)

        return queryset

class Insertarpaciente(PermissionRequiredMixin,FormView):
    permission_required = 'citas.add_paciente'
    login_url = 'login'
    form_class = Formulariopaciente
    template_name = 'insertarpaciente.html'
    success_url = '/verpaciente/'

    def form_valid(self, form):
        form.save()
        return super() .form_valid(form)

class Editpaciente(PermissionRequiredMixin,UpdateView):
    permission_required = 'citas.change_paciente'
    login_url = 'login'
    model = Paciente
    form_class = Formulariopaciente
    template_name = 'editpaciente.html'
    success_url = '/verpaciente'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Elimpaciente(PermissionRequiredMixin,DeleteView):
    permission_required = 'citas.del_paciente'
    login_url = 'login'
    model = Paciente
    template_name = 'elimpaciente.html'
    success_url = '/verpaciente'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Viendomedico(PermissionRequiredMixin,ListView):
    permission_required = 'citas.view_medico'
    login_url = 'login'
    model = Medico
    template_name = 'vermedico.html'
    def get_queryset(self):
        queryset = super(Viendomedico, self).get_queryset()

        if self.request.user.groups.filter(name="Paciente").exists():
            queryset=queryset.filter(paciente__user=self.request.user)

        if self.request.user.groups.filter(name="Medico").exists():
            queryset=queryset.filter(paciente__user=self.request.user)

        return queryset

class Insertarmedico(PermissionRequiredMixin,FormView):
    permission_required = 'citas.add_medico'
    login_url = 'login'
    form_class = Formulariomedico
    template_name = 'insertarmedico.html'
    success_url = '/vermedico/'

    def form_valid(self, form):
        form.save()
        return super() .form_valid(form)

class Editmedico(PermissionRequiredMixin,UpdateView):
    permission_required = 'citas.change_medico'
    login_url = 'login'
    model = Medico
    form_class = Formulariomedico
    template_name = 'editmedico.html'
    success_url = '/vermedico'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Elimmedico(PermissionRequiredMixin,DeleteView):
    permission_required = 'citas.del_medico'
    login_url = 'login'
    model = Medico
    template_name = 'elimmedico.html'
    success_url = '/vermedico'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class Viendoprofile(PermissionRequiredMixin,ListView):
    permission_required = 'citas.view_profile'
    login_url = 'login'
    model = Profile
    template_name = 'verprofiles.html'
    def get_queryset(self):
        queryset = super(Viendoprofile, self).get_queryset()

        if self.request.user.groups.filter(name="Paciente").exists():
            queryset=queryset.filter(paciente__user=self.request.user)

        if self.request.user.groups.filter(name="Medico").exists():
            queryset=queryset.filter(paciente__user=self.request.user)

        return queryset

class Insertarprofile(PermissionRequiredMixin,FormView):
    permission_required = 'citas.add_profile'
    login_url = 'login'
    form_class = Formulariomedico
    template_name = 'insertarprofiles.html'
    success_url = '/verprofiles/'

    def form_valid(self, form):
        form.save()
        return super() .form_valid(form)

class Editeprofile(PermissionRequiredMixin,UpdateView):
    permission_required = 'citas.change_profile'
    login_url = 'login'
    model = Profile
    form_class = Formularioprofile
    template_name = 'editprofiles.html'
    success_url = '/verprofiles'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Elimprofile(PermissionRequiredMixin,DeleteView):
    permission_required = 'citas.del_profile'
    login_url = 'login'
    model = Profile
    template_name = 'elimprofile.html'
    success_url = '/verprofile'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


