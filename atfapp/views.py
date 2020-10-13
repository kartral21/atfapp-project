from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .serializer import UserSerializer
from .models import User
from atfappproject.settings import *
from atfappproject import constants

def indexView(request):
    form = UserSerializer()
    users = User.objects.all()
    return render(request, "index.html", {"form": form, "users": users})

def postUser(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = UserSerializer(request.POST)
        logger.info("{} : database transaction committed".format(constants.MESSAGE))
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            logger.info("{} : Useractivity created".format(str(ser_instance)))
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            logger.exception("Exception: {}".format(form.errors))
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)
