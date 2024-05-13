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