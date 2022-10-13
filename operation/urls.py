from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.add,name='add'),
    path('display',views.display,name='display'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('edit',views.edit,name='edit')

]
