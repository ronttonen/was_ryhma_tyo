from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from was_ryhma_tyo.models import Announcements
from was_ryhma_tyo.forms import AnnouncementForm
from django.core.validators import validate_email
from django.core.mail import EmailMessage
import json

class Home(View):
    def get(self, request):
        return render(template_name="index.html", request=self.request)


class ListAnnouncements(View):
    Announcements = Announcements
    def get(self, request):
        anns = self.Announcements.objects.all().order_by('-creation_date')
        return render(template_name="announcements.html", request=self.request, context={'anns': anns})

class CreateAnnouncement(View):
    Announcements = Announcements
    Form = AnnouncementForm
    def get(self, request):
        form = self.Form
        return render(template_name='create_announcement.html', request=self.request,context={'form':form})

    def post(self, request):
        form = self.Form(request.POST)
        if not form.is_valid():
            return HttpResponse('Form not valid')
        title = request.POST.get('title')
        name = request.POST.get('name')
        description = request.POST.get('custom_text')
        exp_date = request.POST.get('expiration_date')
        email = request.POST.get('email')
        type = request.POST.get('category')
        if validate_email(email):
            return HttpResponse('Email not valid')
        ann = self.Announcements(title=title, custom_text=description, email=email, expiration_date=exp_date, name=name, category=type)
        ann.save()
        return redirect('/announcement/{}'.format(ann.id))


class ViewAnnouncement(View):
    Announcements = Announcements
    def get(self, request, id):

        ann = get_object_or_404(self.Announcements, id=id)
        return render(template_name="announcement.html", request=self.request, context={'ann': ann})
