from django.shortcuts import render,HttpResponse

def index(request):
    context={

        "numbers":[12,3,4,5,6,7]
        
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")
