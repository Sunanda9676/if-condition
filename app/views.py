from django.shortcuts import render

# Create your views here.
def ifcondition(request):
    d={'a':20}
    return render(request,'ifcondition.html',d)
