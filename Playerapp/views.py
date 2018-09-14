from django.shortcuts import render
from Playerapp.models import Player
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class List(ListView):
    model = Player
    template_name = 'index.html'

class Detail(DetailView):
    model = Player
    
    template_name = 'detail.html'
class Create(CreateView):
    model = Player
    fields = ('__all__')
    template_name = 'create.html'

class Update(UpdateView):
    model = Player
    fields = ('Awards',)

    template_name = 'update.html'


class Delete(DeleteView):
    model = Player
    success_url = reverse_lazy('Playerapp:list')
    template_name = 'delete.html'

def about(request):
    return render(request,'about.html')
def login(request):
    return render(request,'login.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'