from django.shortcuts import render, get_list_or_404, redirect
from .models import Alumno
from .forms import AlumnoForm

def lista_alumnos(request):
    alumnos = Alumno.objects.all();
    return render(request, "aplicacionPrimaria/lista_alumnos.html", {"alumnos": alumnos})

def detalle_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'aplicacionPrimaria/detalle_alumno.html', {'alumno': alumno})

def nuevo_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save()
            return redirect('detalle_alumno', pk=alumno.pk)
    else:
        form = AlumnoForm()
    return render(request, 'aplicacionPrimaria/editar_alumno.html', {'form': form})

def editar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            alumno = form.save()
            return redirect('detalle_alumno', pk=alumno.pk)
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'aplicacionPrimaria/editar_alumno.html', {'form': form})

def eliminar_alumno(request, pk):
    """
    Vista para eliminar un alumno.
    """
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('lista_alumnos')
    return render(request, 'aplicacionPrimaria/eliminar_alumno.html', {'alumno': alumno})
