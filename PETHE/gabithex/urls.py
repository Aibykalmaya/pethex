from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('feature/', views.feature, name='feature'),
    path('product/', views.product, name='product'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404/', views.page_404, name='404'),
    path('contact/', views.contact, name='contact'),
]
