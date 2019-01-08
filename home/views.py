from django.shortcuts import render
from account.forms import UserCreateForm
from .models import *


def home(request):

    tracks = DbTracks.objects.all().order_by("-date")

    sitename = "FBMusic"
    form = UserCreateForm()
    return render(request, 'home/index.htm', locals())