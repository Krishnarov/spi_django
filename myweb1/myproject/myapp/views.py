from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('this is a contact page')
    return render(request,'index.html')
def about(request):
    return render(request,'index1.html')
def contact(request):
    return render(request,'nidex2.html')