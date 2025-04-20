from django.shortcuts import render
from django.conf import settings

# Create your views here.

def pdf_viewer(request):
    # Path to the sample PDF, relative to the static directory
    pdf_url = settings.STATIC_URL + 'pdf/the-three-musketeers.pdf'
    
    context = {
        'pdf_url': pdf_url,
    }
    
    return render(request, 'pdf_viewer.html', context)
