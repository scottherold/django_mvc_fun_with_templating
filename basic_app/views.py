from django.shortcuts import render

# Create your views here.
def index(request):
    """Renders the basic_app/index.html webpage"""
    return render(request, 'basic_app/index.html')


def other(request):
    """Renders the basic_app/other.html webpage"""
    return render(request, 'basic_app/other.html')


def relative(request):
    """Renders the basic_app/relative_url_templates.html webpage"""
    return render(request, 'basic_app/relative_url_templates.html')