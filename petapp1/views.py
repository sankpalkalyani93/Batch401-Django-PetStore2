from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission
from .models import Pet, Product, PetUser
from .forms import CustomAuthenticationForm, PetUserForm, PetForm, ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')

def contactpage(request):
    return render(request, 'contact.html')

def contact_submit_page(request):
    return render(request, 'contact_submit.html')

def privacypolicypage(request):
    return render(request, 'privacy_policy.html')

def termspage(request):
    return render(request, 'terms.html')

def faqpage(request):
    return render(request, 'faq.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        # If "remember me" is not checked, set session expiry to browser close
        if not form.cleaned_data.get('remember_me'):
            self.request.session.set_expiry(0)  # Session expires on browser close
        return super().form_valid(form)

@login_required
def assign_permission_to_user(request):
    try:
        # Assign "can_add_pet" permission to "shree94"
        pet_user = get_object_or_404(PetUser, username="shree94")
        permission = Permission.objects.get(codename="can_add_pet")
        pet_user.user_permissions.add(permission)

        # Assign "can_update_pet" permission to "rohit94"
        pet_user2 = get_object_or_404(PetUser, username="sakshi2000")
        permission2 = Permission.objects.get(codename="can_update_pet")
        pet_user2.user_permissions.add(permission2)

        return HttpResponse("Permissions added successfully.")
    except Exception as e:
        return HttpResponse(f"Error while assigning permissions: {e}")

def UserCreateView(request):
    if request.method == 'POST':
        pet_user_form = PetUserForm(request.POST)
        if pet_user_form.is_valid():
            pet_user_form.save()
            return redirect('petuser_list')  
        else:
            print("Form errors:", pet_user_form.errors) 
    else:
        pet_user_form = PetUserForm()
    return render(request, 'user_create_form.html', {'pet_user_form': pet_user_form})

class PetUserList(ListView):
    model = PetUser
    template_name = "petuser_list.html"
    context_object_name = 'users'

class PetList(ListView):
    model = Pet
    template_name = "pet_list.html"
    context_object_name = 'pets'

class PetCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Pet
    form_class = PetForm
    template_name = "pet_create_form.html"
    success_url = reverse_lazy('pet_list')

    permission_required = 'petapp1.can_add_pet'

class PetDetailView(DetailView):
    model = Pet
    template_name = "pet_detail_view.html"

class PetUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Pet
    template_name = "pet_update_form.html"
    fields = ['name', 'breed', 'age', 'price', 'type', 'description']
    success_url = reverse_lazy('pet_list')

    permission_required = 'petapp1.can_update_pet'

class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = "pet_delete_view.html"
    success_url = reverse_lazy('pet_list')


class ProductList(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = 'products'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_create_form.html"
    success_url = reverse_lazy('product_list')

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail_view.html"

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = "product_update_form.html"
    fields = ['product_name', 'category', 'price', 'quantity_in_stock', 'description', 'image']
    success_url = reverse_lazy('product_list')

    permission_required = 'petapp1.can_update_product'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_delete_view.html"
    success_url = reverse_lazy('product_list')