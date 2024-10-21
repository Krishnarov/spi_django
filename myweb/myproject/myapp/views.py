from django.shortcuts import render ,HttpResponse

# Create your views here.
def From_get(data):
    return render(data,"index.html")
def about(data):
    return render(data,"index2.html")
def contact (data):
    return HttpResponse(data,'this is a contact page')