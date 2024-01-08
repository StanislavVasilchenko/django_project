from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import MaterialCreateView, MaterialListView, MaterialDetailView, MaterialUpdateView, \
    MaterialDeleteView

app_name = MaterialsConfig.name

urlpatterns = [
    path('create/', MaterialCreateView.as_view(), name='create'),
    path('view/', MaterialListView.as_view(), name='view'),
    path('detail/<int:pk>', MaterialDetailView.as_view(), name='detail'),
    path('update/<int:pk>', MaterialUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', MaterialDeleteView.as_view(), name='delete'),
]
