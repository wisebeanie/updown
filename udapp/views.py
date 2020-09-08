from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def udMain(request):
    return render(request, 'udMain.html')

def name(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('udMain')

    else:
        form = UserForm()
        return render(request, 'name.html', {'form': form})

def udGame(request):
    return render(request, 'udgame.html')
