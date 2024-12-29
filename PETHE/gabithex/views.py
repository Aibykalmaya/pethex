from django.shortcuts import render

def index(request):
    return render(request, 'gabithex/index.html')

def about(request):
    return render(request, 'gabithex/about.html')

def service(request):
    return render(request, 'gabithex/service.html')

def blog(request):
    return render(request, 'gabithex/blog.html')

def feature(request):
    return render(request, 'gabithex/feature.html')

def product(request):
    return render(request, 'gabithex/product.html')

def team(request):
    return render(request, 'gabithex/team.html')

def testimonial(request):
    return render(request, 'gabithex/testimonial.html')

def page_404(request):
    return render(request, 'gabithex/404.html')

def contact(request):
    return render(request, 'gabithex/contact.html')
