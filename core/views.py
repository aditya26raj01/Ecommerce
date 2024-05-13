from django.shortcuts import render
from product.models import *
# Create your views here.
def frontpage(request):
    products=Product.objects.all()[0:3]
    context={"products":products}
    return render(request,"frontpage.html",context)

def salepage(request):
    products=Product.objects.all()
    context={"products":products}
    return render(request,"shoppingpage.html",context)

def product_page(request,pk):
    specific_product=Product.objects.get(pk=pk)
    context={"specific_product":specific_product}
    return render(request,"product.html",context)