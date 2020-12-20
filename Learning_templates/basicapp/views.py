from django.shortcuts import render

# Create your views here.
def index(request):
    mydict={'text':'My name is Mohit Sharma','number':100}
    return render(request,'basicapp/index.html',context=mydict)

def other(request):
    return render(request,'basicapp/other.html')

def relative(request):
    return render(request,'basicapp/relative.html')
