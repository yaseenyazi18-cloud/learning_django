from django.http import HttpResponse

def index(request):
    return HttpResponse(""
    "<a href='https://www.youtube.com/watch?v=84dtpjaTecQ&list=PLbasZIkCgHJGXEjcatJ3aO1NpS2PsOtoQ&index=4'>Django tutorial</a>"
    
    "\t<a href='https://www.youtube.com/watch?v=oxtvz_zaClw&list=PL4dPAKlZK9IRPvKk8AuG_lBQLKIoRVDi2&index=4'>Django project</a>""")

def about(request):
    return HttpResponse("<h1>i'm yaseen. I can do it</h1>")

def contact(request):
    return HttpResponse("<a href='/'>Back to home page I can do it</a>")