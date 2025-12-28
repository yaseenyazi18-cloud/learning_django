from django.shortcuts import render

# Create your views here.
def create(request):
    if request.POST:
        print(request.POST)
        print(request.POST.get('name'))
        print(request.POST.get('year'))
    return render(request,'create.html')

def edit(request):
    return render(request, 'edit.html')

def list(request):
    lap = { 'laptop': [{
        'name':'Lenovo IQL',
        'spec' : ' Intel Core i7-1165G7 · Intel Iris Xe Graphics G7 (96EU) ',
        'year' : '8 month',
        'sucess' : True,
        'img':'laptops.jpg'
        },
        {
        'name':'dsi',
        'spec' : ' Intel Core i7-1165G7 · Intel Iris Xe Graphics G7 (96EU) ',
        'year' : '8 month',
        'sucess' : True,
        'img':'surtop.jpg'
        },               
        {
        'name':'acer',
        'spec' : ' Intel Core i7-1165G7 · Intel Iris Xe Graphics G7 (96EU) ',
        'year' : '8 month',
        'sucess' : True,
        'img':'lap.jpeg'
        },
        {
        'name':'hp',
        'spec' : ' Intel Core i7-1165G7 · Intel Iris Xe Graphics G7 (96EU) ',
        'year' : '8 month',
        'sucess' : True,
        'img':'surtop.jpg'
        },
        {
        'name':'asuse',
        'spec' : ' Intel Core i7-1165G7 · Intel Iris Xe Graphics G7 (96EU) ',
        'year' : '8 month',
        'sucess' : True,
        'img':'lap.jpeg'
        },
        {
        'name':'IQL',
        'spec' : ' Intel Core i7-1165G7 · Intel Iris Xe Graphics G7 (96EU) ',
        'year' : '8 month',
        'sucess' : True,
        'img':'laptops.jpg'
        },               
        ]}
    return render(request, 'list.html', lap)