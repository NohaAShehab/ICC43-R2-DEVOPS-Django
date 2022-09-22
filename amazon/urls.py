from django.urls import path
from amazon.views import  getHomepage, homepage, getProducts,\
    ProductDetailedView, CreateProductView, EditProductView, DeleteProductView

urlpatterns = [
    path('home', getHomepage),
    path('homep', homepage),
    path('products', getProducts,name = "products.index"),
    path("products/<int:pk>", ProductDetailedView.as_view(), name='products.show'),
    path("products/create", CreateProductView.as_view(), name='products.create'),
    path("products/edit/<int:pk>", EditProductView.as_view(), name='products.edit'),
    path("products/delete/<int:pk>", DeleteProductView.as_view(), name='products.delete'),
]
