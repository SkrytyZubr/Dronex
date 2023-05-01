from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')
def add_expense(request):
    return render(request, 'app/add_expense.html')