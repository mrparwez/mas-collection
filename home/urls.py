from django.urls import path
from . import views

urlpatterns=[
    path("index/", views.IndexPage.index, name="index"),
    path("about/",views.AboutUsPage.about, name="about"),
    path("products/", views.ProductsPage.products, name="product"),
    path("product_detail/", views.ProductDetailsPage.product_detail, name="product_detail"),
    path("contact/", views.ContactPage.contact, name="contact"),
    path("cart/", views.CartPage.cart, name="cart"),
    path("checkout/", views.CheckoutPage.checkout, name="checkout"),
    path("register/", views.RegisterPage.register, name="register"),
]