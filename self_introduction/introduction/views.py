from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegisterForm
from .models import Register

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'


class RegisterView(generic.CreateView):
    model = Register
    form_class = RegisterForm
    template_name = 'register.html'
    context_object_name = 'register'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('introduction:register_detail', pk=self.object.pk)
    
class RegisterDetailView(generic.DetailView):
    model = Register
    template_name = 'register_detail.html'
    context_object_name = 'register_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_id = self.object.id
        back = Register.objects.filter(id__lt=current_id).order_by('-id').first() #lt=less than 
        next = Register.objects.filter(id__gt=current_id).order_by('id').first() #gt=greater than 忘れがち

        context['back'] = back
        context['next'] = next
        return context