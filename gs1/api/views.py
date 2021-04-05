from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

#Model Object - single Student data
def StudentDetails(request,pk):
  stu = Student.objects.get(id=pk)
  serializer = StudentSerializer(stu)
  JsonData = JSONRenderer().render(serializer.data)
  return HttpResponse(JsonData,content_type = 'application/json')

def StudentData(request):
  stu = Student.objects.all()
  serializer = StudentSerializer(stu,many = True)
  JsonData = JSONRenderer().render(serializer.data)
  return HttpResponse(JsonData,content_type = 'application/json')

