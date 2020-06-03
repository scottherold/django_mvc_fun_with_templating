from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Creates a dictionary of text and a number to be passed to the view.

    Renders the basic_app/index.html webpage with the context dictionary.
    """
    context_dict = {'text':'Hello World', 'number': 100}
    return render(request, 'basic_app/index.html', context_dict)


def other(request):
    """Renders the basic_app/other.html webpage"""
    return render(request, 'basic_app/other.html')


def relative(request):
    """Renders the basic_app/relative_url_templates.html webpage"""
    return render(request, 'basic_app/relative_url_templates.html')