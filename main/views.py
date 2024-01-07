from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Student


class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar',)
    success_url = reverse_lazy('main:index')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar', 'is_active',)

    # success_url = reverse_lazy('main:index')

    def get_success_url(self):
        return reverse('main:student-detail', kwargs={'pk': self.object.pk})


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('main:index')


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


def toggle_activity(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if student.is_active:
        student.is_active = False
    else:
        student.is_active = True
    student.save()
    return HttpResponseRedirect(reverse('main:index'))
