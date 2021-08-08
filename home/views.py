from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from home.models import counter
from django.utils import timezone

# Create your views here.

def index(request):
        try:
            entry = counter.objects.get(pk=1)
        except:
            post = counter()
            post.pk = 1
            post.esp_result = 0
            post.date_created = timezone.now()
            post.save()  
            
        return render(request, 'index.html',{'savecount':entry})

def counting(request):
    va1 = float(request.GET['inputNumber'])
    post = counter.objects.get(pk = 1)
    post.esp_result = va1
    post.save()
    return HttpResponseRedirect(reverse ('index'))
