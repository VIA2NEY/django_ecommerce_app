from django.shortcuts import render, get_object_or_404

# Create your views here.
def home_index(request):
    return render(request, 'home_index.html')