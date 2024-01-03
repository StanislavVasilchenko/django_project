from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Name: {name}, Email: {email}, Message: {message}')
    return render(request, 'main/index.html')
