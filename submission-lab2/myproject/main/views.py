from django.shortcuts import render
from django.http import Http404

def render_html(request, template_name):
    try:
        return render(request, template_name)
    except TemplateDoesNotExist:
        raise Http404("Template does not exist")
