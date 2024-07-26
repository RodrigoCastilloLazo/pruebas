from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alumnos, name='lista_alumnos'),
    path('alumno/<int:pk>/', views.detalle_alumno, name='detalle_alumno'),
    path('alumno/nuevo/', views.nuevo_alumno, name='nuevo_alumno'),
    path('alumno/<int:pk>/editar/', views.editar_alumno, name='editar_alumno'),
    path('alumno/<int:pk>/eliminar/', views.eliminar_alumno, name='eliminar_alumno'),
]
