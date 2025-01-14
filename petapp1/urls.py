from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomLoginView, ProductUpdateView, ProductDeleteView, contact_submit_page, privacypolicypage, termspage, faqpage, aboutpage, contactpage, UserCreateView, PetUserList , PetList, PetCreateView, PetDetailView, PetUpdateView, PetDeleteView, homepage, ProductList, ProductCreateView, ProductDetailView

urlpatterns = [
    path('home/', homepage, name='home'),
    path('about/', aboutpage, name='about'),
    path('contact/', contactpage, name='contact'),
    path('contact_submit/', contact_submit_page, name="contact_submit"),
    path('privacy_policy/', privacypolicypage, name='privacy_policy'),
    path('terms/', termspage, name='terms'),
    path('faq/', faqpage, name='faq'),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('create_user/', UserCreateView, name="create_user"),
    path('petuser_list/', PetUserList.as_view(), name="petuser_list"),
    path('pet_list/', PetList.as_view(), name="pet_list"),
    path('create_pet/', PetCreateView.as_view(), name="create_pet"),
    path('pet_detail_view/<int:pk>', PetDetailView.as_view(), name="pet_detail_view"),
    path('update_pet/<int:pk>', PetUpdateView.as_view(), name="update_pet"),
    path('delete_pet/<int:pk>', PetDeleteView.as_view(), name="delete_pet"),
    path('product_list/', ProductList.as_view(), name="product_list"),
    path('create_product/', ProductCreateView.as_view(), name="create_product"),
    path('product_detail_view/<int:pk>', ProductDetailView.as_view(), name="product_detail_view"),
    path('update_product/<int:pk>', ProductUpdateView.as_view(), name="update_product"),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name="delete_product"),
]