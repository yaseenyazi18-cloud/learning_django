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


def edit(request,pk):
    instance_edited = lapInfo.objects.get(pk=pk)
    if request.POST:
        frm = lapInfo(request.POST,instance=instance_edited)
        if frm.is_valid():
            instance_edited.save()
        # tittle=request.POST.get('name')
        # spec=request.POST.get('spec')
        # year=request.POST.get('year')
        # instance_edited.name=tittle
        # instance_edited.spec=spec
        # instance_edited.year=year
    else:
        frm = lapform(instance=instance_edited)    
    
    return render(request, 'create.html', {'frm':frm })


def delete(request, pk):
    instance = lapInfo.objects.get(pk=pk)
    instance.delete()
    lap = lapInfo.objects.all()
    return render(request, 'list.html', {'laptop':lap})
    

def list(request):
    lap = lapInfo.objects.all()
    print(lap)
    return render(request, 'list.html', {'laptop':lap})