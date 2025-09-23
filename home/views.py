from django.shortcuts import render, HttpResponse

# Create your views here.
class IndexPage:
    def index(request):
        return render(request, "index.html")
    
class AboutUsPage:
    def about(request):
        return render(request, "about.html")
    
class ProductsPage:
    def products(request):
        return render(request, "products.html")
    
class ProductDetailsPage:
    def product_detail(request):
        return render(request, "product_detail.html")
    
class ContactPage:
    def contact(request):
        return render (request, "contact.html")

class CartPage:
    def cart(request):
        return render (request, "cart.html")
    
class CheckoutPage:
    def checkout(request):
        return render(request, "checkout.html")
    
class RegisterPage:
    def register(request):
        return render(request, "register.html")
    
