from .forms import StudentForm
from .models import Student
from django.shortcuts import render, redirect


def index(request):
    things = Student.objects.all()
    return render(request, "main/index.html", {'title': 'main page', 'things': things})


def about(request):
    return render(request, "main/about.html")


def add(request):
    error = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'error...'

    form = StudentForm()
    info = {
        'form': form,
        'error': error
    }
    return render(request, "main/add.html", info)