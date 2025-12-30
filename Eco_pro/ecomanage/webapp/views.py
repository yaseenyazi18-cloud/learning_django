from django.shortcuts import render
from . models import lapInfo
from . forms import lapform


# Create your views here.
def create(request):
    frm=lapform()
    if request.POST:
      frm = lapform(request.POST)
      if frm.is_valid:
          frm.save()
    else:
        frm = lapform()      
          
    return render(request,'create.html', {'frm' : frm })


def edit(request):
    return render(request, 'edit.html')

def list(request):
    lap = lapInfo.objects.all()
    return render(request, 'list.html', {'laptop':lap})