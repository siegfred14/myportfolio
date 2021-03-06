from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os

# from django.core.mail import message, send_mail
# from django.conf import settings


# class HomeTemplateView(TemplateView):
#     template_name = 'home.html'

#     # override get context date method
#     def get_context_data(self, **kwargs):
#         # first, call super get context data
#         context = super().get_context_data(**kwargs)
#         context['about'] = About.objects.first()
#         context['services'] = Service.objects.all()
#         context['portfolio'] = WorkExperience.objects.all()
#         # context['contact'] = Contact.objects.all()
#         return context

def downloadfile(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'ResumeDeSiegfred.pdf'
    filepath = base_dir + '/files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(
        open(thefile, 'rb'), chunk_size), content_type=mimetypes.guess_type(thefile[0]))
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment;filename=%s" % filename
    return response


def home(request):
    if request.method == "POST":
        # For Email
        #     name = request.POST['name']
        #     email = request.POST['email']
        #     message = request.POST['message']

        #     send_mail('Contact Form',
        #               name,
        #               email,
        #               message,
        #               settings.EMAIL_HOST_USER,
        #               'thomasadigun@gmail.com',
        #               fail_silently=False
        #               )
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message

        contact.save()
        return HttpResponse("<h1>Thanks For Contacting Me. You'll receive a feed back in 18hrs!</h1>")

    return render(request, 'home.html')
