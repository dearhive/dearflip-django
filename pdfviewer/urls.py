from django.urls import path
from . import views

app_name = 'pdfviewer'

urlpatterns = [
    path('', views.pdf_viewer, name='pdf_viewer'),
] 