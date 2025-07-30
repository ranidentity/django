from .models import User
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def users(request):
    allusers = User.objects.all().values()
    template = loader.get_template('all_users.html')
    context ={
        'allusers': allusers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    user = User.objects.get(id=id)
    template=loader.get_template('details.html')
    context = {
        'user':user,
    }
    return HttpResponse(template.render(context, request))