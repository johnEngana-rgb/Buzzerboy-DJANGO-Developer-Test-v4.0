from django.http import Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist

def home(request):
    return render(request, 'index.html', {})


def render_html(request, template_name):
    # Remove 'profile/' prefix if it exists
    if template_name.startswith('profile/'):
        template_name = template_name.replace('profile/', '', 1)

    try:
        return render(request, template_name)
    except TemplateDoesNotExist:
        raise Http404(f"'{template_name}' could not be found")