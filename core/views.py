from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.http import HttpResponse


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        # first, call super get context data
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['portfolio'] = WorkExperience.objects.all()
        # context['contact'] = Contact.objects.all()
        return context


def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message

        contact.save()
        return HttpResponse("Thanks For Contacting Me. You'll receive a feed back in 18hrs!")
    return render(request, 'home.html')
