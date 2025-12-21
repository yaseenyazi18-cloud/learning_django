from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    yazi = "Hey I'm Muhammed Yasseem"
    hana = "Hey i'm Hana Fathima"
    data = {'yzi':yazi,
            'hana':hana
    }
    return render(request, "index.html", data)

def analyze(request):
    if request.method == "GET":
        text = request.GET.get('textname')
        removeponc = request.GET.get("removeponc", "off")
        capitalize = request.GET.get("capitalize", "off")
        lowercase = request.GET.get("lowercase", "off")
        
        
        punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        analyzed = ""
        if removeponc == "on":
            
            for char in text:
                if char not in punctuation:
                   analyzed = analyzed + char
                
        if capitalize == "on":
                analyzed = text.upper()

        if lowercase == "on":
            analyzed = text.lower()
              
             
            data = { 
                    'text':analyzed
            }
                   


                  
        else:
            return HttpResponse("Error")


    return render(request, "analyze.html", data)            
        # if Capitalize == "on":
           
        #     for char in text:
        #         if char not in punctuation:
        #             analyzed = analyzed + char
        #             captxt = analyzed.upper()
        #         data = { 
        #             'captxt':captxt
        #             }

        # elif Lowercase == "on":
        #         analyzed = ""
        #         for char in text:
        #             if char not in punctuation:
        #                 analyzed = analyzed + char
        #                 captxt = analyzed.upper()
        #                 lowtext = analyzed.lower()    
        #             data = {
        #                 'lowtext':lowtext 
        #             } 

        

                 
       



def about(request):
    return HttpResponse("<h1>i'm yaseen. I can do it</h1>")

def contact(request):
    return HttpResponse("<a href='/'>Back to home page I can do it</a>")