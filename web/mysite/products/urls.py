from . import views
from django.urls import path


app_name = 'products'
urlpatterns = [

path('', views.ProductList.as_view(), name='index'),
path('<int:prod_id>/',views.Show_detail.as_view(),name='detail'),
path('add_new/',views.add_new,name = 'add_new'),
path('<int:prod_id>/delete/',views.delete,name='delete')
]
