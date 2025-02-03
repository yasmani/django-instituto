from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarcurso/', views.registrarcurso),
    path('edicioncurso/<codigo>', views.editarcurso),
    path('editacurso/', views.editacurso),
    path('eliminarcurso/<codigo>', views.eliminarcurso)

]