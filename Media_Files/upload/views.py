from django.shortcuts import render, redirect, HttpResponse
from .forms import StudentForm
from .models import Student
# Create your views here.

def Add_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, 'app1/add.html', {'form':form})

def Show_view(request):
    obj = Student.objects.all()
    return render(request, 'app1/show.html', {'obj':obj})

def Update_view(request, pk):
    obj = Student.objects.get(Id = pk)
    form = StudentForm(instance=obj)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, 'app1/add.html', {'form':form})

def Delete_view(request, pk):
    obj = Student.objects.get(Id = pk )
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'app1/success.html', {})