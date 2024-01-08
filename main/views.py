from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import StudentForm, SubjectForm
from main.models import Student, Subject


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('main:index')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return reverse('main:student-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            form.instance = self.object
            formset.save()
        return super().form_valid(form)


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
