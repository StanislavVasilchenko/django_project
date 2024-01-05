from django.urls import path

from main.views import contact, StudentListView, StudentDetailView

app_name = 'main'

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('student-detail/<int:pk>', StudentDetailView.as_view(), name='student-detail'),
]
