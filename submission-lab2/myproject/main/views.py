from django.shortcuts import render
from django.http import Http404
from django.template import TemplateDoesNotExist

def render_html(request, template_name):
    try:
        return render(request, template_name)
    except TemplateDoesNotExist:
        raise Http404(f"'{template_name}' could not be found")
