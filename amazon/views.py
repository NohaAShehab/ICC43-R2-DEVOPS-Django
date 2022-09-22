from django.shortcuts import render
from django.http import  HttpResponse
from amazon.models import Product
from django.views.generic import DetailView
from django.views.generic.edit import  CreateView, UpdateView , DeleteView
# Create your views here.
from amazon.forms import ProductModelForm


def getHomepage(request):
    return  HttpResponse("---> this home page ----> ")


def homepage(request):
    return render(request, "amazon/homepage.html")


def getProducts(request):
    allproducts = Product.get_all_productes()
    # return HttpResponse(products)
    context = {"products":allproducts}
    return render(request, "amazon/index.html", context={"products":allproducts})


# ### class based views


class ProductDetailedView(DetailView):
    model = Product
    template_name = "amazon/show.html"


class CreateProductView(CreateView):
    template_name = "amazon/create.html"
    success_url = "/amazon/products"
    form_class = ProductModelForm


class EditProductView(UpdateView):
    template_name = "amazon/edit.html"
    form_class = ProductModelForm
    success_url = "/amazon/products"
    model =  Product


class DeleteProductView(DeleteView):
    template_name = "amazon/delete.html"
    success_url = "/amazon/products"
    model =  Product





