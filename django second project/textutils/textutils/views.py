from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     yazi = "Hey I'm Muhammed Yasseem"
#     hana = "Hey i'm Hana Fathima"
#     data = {'yzi':yazi,
#             'hana':hana
#     }
#     return render(request, "index.html", data)
def index(request):
    return render(request, 'index.hyml')

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
                if char in punctuation:
                   text = text.replace(char,"")
                else:
                    analyzed += char

                  
        if  capitalize == "on" and lowercase == "on" or capitalize == "off" and lowercase == "off":
            if capitalize == "off" and lowercase == "off":
                data = {
                    
                'text': text,
                }
            elif capitalize == "on" and lowercase == "on":
                data = {
                    'error': True,
                    'error_msg': "You cannot select both Uppercase and Lowercase at the same time."
                }
            return render(request, "analyze.html", data) 
           
        elif capitalize == "on":
            analyzed = text.upper()
            error = False   

        elif lowercase == "on":
           analyzed = text.lower()
           error = False
              
             
        data = { 
            'text':analyzed,
            'error':error
            }
        
        return render(request, "analyze.html", data)  
    else:
        data = {
            'text':text
            }
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