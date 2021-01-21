from django.shortcuts import render, get_object_or_404,reverse
from django.urls import reverse_lazy
from django.views.generic import ListView,TemplateView,CreateView
from django.views.generic.edit import FormView
from .models import Catagory,Prod,Contactus
from .form import Contactusform

# Create your views here.

class catagory(ListView):
    model = Catagory
    paginate_by = 8
    template_name = 'index.html'

class aboutus(TemplateView):
    template_name = 'about.html'

class contactus(CreateView):
    form_class = Contactusform
    model=Contactus
    template_name = 'contactus.html'
    success_url = reverse_lazy('contactus')

def list_of_catagory(request, catagory_slug):
    catagories = Catagory.objects.all()
    post = Prod.objects.filter(status='publish')
    if catagory_slug:
        catagory = get_object_or_404(Catagory, slug=catagory_slug)
        post = post.filter(catagory=catagory)
    context = {'catagories': catagories, 'post': post, 'catagory': catagory}
    return render(request, 'home.html', context)
