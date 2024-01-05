from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from main.models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Name: {name}, Email: {email}, Message: {message}')
    context = {
        'title': 'Контакты',
    }
    return render(request, 'main/contact.html', context)


class StudentDetailView(DetailView):
    model = Student
    template_name = 'main/student_detail.html'

