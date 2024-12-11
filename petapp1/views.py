from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Pet, Product, PetUser
from .forms import PetUserForm

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

"""class UserCreateView(CreateView):
    model = PetUser
    template_name = "user_create_form.html"
    fields = ['fname', 'lname', 'email1', 'phone1', 'address1', 'my_file1']
    success_url = reverse_lazy('petuser_list')"""


def UserCreateView(request):
    if request.method == 'POST':
        pet_user_form = PetUserForm(request.POST)
        if pet_user_form.is_valid():
            pet_user_form.save()
            return redirect('petuser_list')
    else:
        pet_user_form = PetUserForm()
    return render(request, 'user_create_form.html', {'pet_user_form':pet_user_form})

class PetUserList(ListView):
    model = PetUser
    template_name = "petuser_list.html"
    context_object_name = 'users'

class PetList(ListView):
    model = Pet
    template_name = "pet_list.html"
    context_object_name = 'pets'

class PetCreateView(CreateView):
    model = Pet
    template_name = "pet_create_form.html"
    fields = ['name', 'breed', 'age', 'price', 'type', 'description', 'image']
    success_url = reverse_lazy('pet_list')

class PetDetailView(DetailView):
    model = Pet
    template_name = "pet_detail_view.html"

class PetUpdateView(UpdateView):
    model = Pet
    template_name = "pet_update_form.html"
    fields = ['name', 'breed', 'age', 'price', 'type', 'description']
    success_url = reverse_lazy('pet_list')

class PetDeleteView(DeleteView):
    model = Pet
    template_name = "pet_delete_view.html"
    success_url = reverse_lazy('pet_list')


class ProductList(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    template_name = "product_create_form.html"
    fields = ['product_name', 'category', 'price', 'quantity_in_stock', 'description', 'image']
    success_url = reverse_lazy('product_list')

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail_view.html"