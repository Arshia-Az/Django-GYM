from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "base/index.html")


def header_component(request):
    return render(request, 'base/_Header/header.html')

def footer_component(request):
    return render(request, 'base/_Footer/footer.html')