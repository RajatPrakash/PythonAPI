from django.shortcuts import render
import io
import requests
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def StudentCreate(request):
  if request.method =='POST':
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serialiser = StudentSerializers(data =python_data)
    if serialiser.is_valid():
      serialiser.save()
      return_message = {'msg':'Data Created'}
      json_data = JSONRenderer().render(return_message)
      return HttpResponse(json_data,content_type = 'application/json')
    # else:
    #   json_data = JSONRenderer.render(serialiser.errors)
    #   return HttpResponse(json_data,content_type = 'application/json')
