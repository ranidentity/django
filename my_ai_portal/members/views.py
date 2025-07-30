from django.template import loader
from django.http import HttpResponse
from .models import Member

# Create your views here.
def members(request):
    mymember = Member.objects.all().values()
    template = loader.get_template('first.html')
    return HttpResponse(template.render())
