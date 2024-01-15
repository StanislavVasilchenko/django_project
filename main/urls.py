from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import contact, StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, \
    StudentDeleteView, toggle_activity

app_name = 'main'

urlpatterns = [
    path('', cache_page(60)(StudentListView.as_view()), name='index'),
    path('contact/', contact, name='contact'),
    path('student-detail/<int:pk>', StudentDetailView.as_view(), name='student-detail'),
    path('student-create/', StudentCreateView.as_view(), name='student-create'),
    path('update/<int:pk>', StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name='delete'),
    path('acrivity/<int:pk>', toggle_activity, name='acrivity'),
]
