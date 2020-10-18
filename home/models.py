from django.db import models
from django.http import HttpResponseRedirect
from wagtail.core.models import Page


class HomePage(Page):
    max_count = 0

    # def serve(self, request):
    #     # Redirect to blog index page
    #     return HttpResponseRedirect('/gioi-thieu/')
