"""agendamiento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import TemplateView

from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from citas.views import Viendocitas,Viendoeps,Viendopaciente,Viendomedico,Viendoprofile
from citas.views import Insertarcita,Insertarmedico,Insertarpaciente,Insertareps,Insertarprofile
from citas.views import Editcita, Editeps, Editmedico, Editpaciente, Editeprofile
from citas.views import Elimcita, Elimeps, Elimpaciente, Elimmedico, Elimprofile
from django.conf.urls.static import static
from agendamiento import settings

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls), # admin site
    path('vercita/', Viendocitas.as_view()),
    path('vereps/', Viendoeps.as_view()),
    path('verpaciente/', Viendopaciente.as_view()),
    path('vermedico/', Viendomedico.as_view()),
    path('verprofiles/', Viendoprofile.as_view()),
    path('insertarcita/', Insertarcita.as_view()),
    path('insertarmedico/', Insertarmedico.as_view()),
    path('insertarpaciente/', Insertarpaciente.as_view()),
    path('insertareps/', Insertareps.as_view()),
    path('insertarprofile/', Insertarprofile.as_view()),
    path('editcita/<int:pk>/', Editcita.as_view()),
    path('editeps/<int:pk>/', Editeps.as_view()),
    path('editmedico/<int:pk>/', Editmedico.as_view()),
    path('editpaciente/<int:pk>/', Editpaciente.as_view()),
    path('editprofiles/<int:pk>/', Editeprofile.as_view()),
    path('elimcita/<int:pk>/', Elimcita.as_view()),
    path('elimeps/<int:pk>/', Elimeps.as_view()),
    path('elimpaciente/<int:pk>/', Elimpaciente.as_view()),
    path('elimmedico/<int:pk>/', Elimmedico.as_view()),
    path('elimprofile/<int:pk>/', Elimprofile.as_view()),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view()),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
