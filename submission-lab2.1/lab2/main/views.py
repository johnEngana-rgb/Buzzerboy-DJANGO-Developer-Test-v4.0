from django.http import Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist

def home(request):
    return render(request, 'index.html', {})


def render_html(request, template_name):
    try:
        return render(request, template_name)
    except TemplateDoesNotExist:
        raise Http404(f"'{template_name}' could not be found")