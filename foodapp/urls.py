from . import views
from django.urls import path

urlpatterns = [
    #food
    path('', views.index,name='index'),
    #food/1
    path('<int:item_id>',views.detail,name='detail'),
    path('items/', views.item,name='item'),
]
