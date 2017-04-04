from django.shortcuts import render

def hair(request):
    return render(request, 'hair/hair_index.html', {})