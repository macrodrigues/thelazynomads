from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, 'main/index.html')

def posts(request):
    pass

def post_info(request):
    pass