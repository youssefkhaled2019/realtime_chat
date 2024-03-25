from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    # context["myname"]="youssef"
    return render(request ,"personal/home.html",context)