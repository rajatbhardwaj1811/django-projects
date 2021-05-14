from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='shop_index'),
    path('aboutus/', views.aboutus,name='aboutus'),
    path('contactus/', views.contactus,name='contactus'),
    path('tracker/', views.tracker,name='tracker'),
    path('prodview/<int:myid>', views.prodview,name='prodview'),
    path('checkout/',views.checkout)
]