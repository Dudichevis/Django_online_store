from .views import (
    BaseView,
    ProductDetailView,
    CategoryDetailView,
    CartView,
    AddToCartView,
    DeleteFromCartView,
    ChangeQTYView,
    CheckoutView,
    MakeOrderView,
    PayedOnlineORderView,
    LoginView,
    RegistrationView,
    ProfileView
)
from django.contrib.auth.views import LogoutView
from django.urls import path
from .import views


urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
    path('products/<str:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add-to-cart/<str:slug>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:slug>/', views.DeleteFromCartView.as_view(), name='remove_from_cart'),
    path('change-qty/<str:slug>/', views.ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', views.CheckoutView.as_view(), name='chekcout'),
    path('make-order/', views.MakeOrderView.as_view(), name='make_order'),
    path('payed-online-order/', views.PayedOnlineORderView.as_view(), name='payed_online_order'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile')
]

