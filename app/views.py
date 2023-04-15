from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        name=request.POST['user']
        password=request.POST['password']
        print(name)
        print(password)
       # return HttpResponse('DATA SUBMITTED SUCCESFULLY')
    return render(request,'formcreate.html')
