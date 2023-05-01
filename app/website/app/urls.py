from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app'),
    path('add-expense', views.add_expense, name='add-expense'),

]