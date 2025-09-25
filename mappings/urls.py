from django.urls import path
from . import views

urlpatterns = [
    path('mappings/', views.MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:pk>/', views.MappingDetailView.as_view(), name='mapping-detail'),
    path('mappings/patient/<int:patient_id>/', views.PatientMappingsView.as_view(), name='patient-mappings'),
]