from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from feedbackreview.models import Feedback
# Create your views here.
def index(request):
    feedback=Feedback.objects.all()
    dests=Destination.objects.all()
    context={
        'dests':dests,
        'feedbacks':feedback
    }
    return render(request,'home.html',context)

def search(request):
    if request.method=='GET':
        place_name=request.GET['place']
        print(place_name)    
        dest = Destination.objects.filter(name__icontains=place_name)
    context={
        'dests':dest,}
    
    return render(request,'search.html',context)
