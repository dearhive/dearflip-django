# DearFlip PDF Viewer Django Integration

This project demonstrates how to integrate the DearFlip PDF viewer into a Django application.

## Setup Instructions

### 1. Install Django

```bash
pip install django
```

### 2. Set Up Django Project Structure

```bash
django-admin startproject mysite
cd mysite
python manage.py startapp pdfviewer
```

### 3. Include DearFlip Resources

1. Download DearFlip from the official website or add it to your project
2. Create a structure like this:
```
public/
├── dflip/
│   ├── css/
│   ├── js/
│   ├── sound/
│   └── images/
└── pdf/
    └── your-sample-pdf.pdf
```

### 4. Configure Django Settings

Add the following to your `settings.py`:

```python
INSTALLED_APPS = [
    # ... other apps
    'pdfviewer',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add this line
        'APP_DIRS': True,
        # ... other settings
    },
]

# Static files configuration
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'public',
]

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### 5. Create a Template

Create `templates/pdf_viewer.html`:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PDF Viewer with dFlip</title>
    
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    
    <!-- dFlip CSS -->
    <link rel="stylesheet" type="text/css" href="{% static 'dflip/css/dflip.min.css' %}">
    
    <!-- dFlip JavaScript -->
    <script src="{% static 'dflip/js/dflip.min.js' %}"></script>
</head>
<body>
    <div class="container">
        <h1>PDF Viewer</h1>
        
        <!-- PDF display container -->
        <div class="_df_book" id="pdf-container" 
             source="{{ pdf_url }}"
             data-height="500"
             data-width="auto"
             data-auto-sound="true">
        </div>
    </div>
</body>
</html>
```

### 6. Create a View

In `pdfviewer/views.py`:

```python
from django.shortcuts import render
from django.conf import settings

def pdf_viewer(request):
    # Path to the sample PDF, relative to the static directory
    pdf_url = settings.STATIC_URL + 'pdf/your-sample-pdf.pdf'
    
    context = {
        'pdf_url': pdf_url,
    }
    
    return render(request, 'pdf_viewer.html', context)
```

### 7. Configure URLs

Create `pdfviewer/urls.py`:

```python
from django.urls import path
from . import views

app_name = 'pdfviewer'

urlpatterns = [
    path('', views.pdf_viewer, name='pdf_viewer'),
]
```

Update `mysite/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pdf/', include('pdfviewer.urls')),
    path('', include('pdfviewer.urls')),  # Optional: Make PDF viewer the homepage
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 8. Run Migrations and Start Server

```bash
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see your PDF displayed with DearFlip.

## Additional Configuration

You can customize the DearFlip viewer by adding additional attributes to the div with `_df_book` class. See the [official DearFlip documentation](https://dearflip.com/docs/) for more options.

## License

Make sure to purchase a valid license from [DearFlip](https://dearflip.com/) if you're using this in a production environment. 