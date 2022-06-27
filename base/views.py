from django.shortcuts import render
from .forms import VideoForm  
from django.http import HttpResponse
from .models import Video
# Create your views here.
def index(request):  
    if request.method == 'POST':  
        student = VideoForm(request.POST, request.FILES)  
        if student.is_valid():  
            
            instance = Video( name = request.POST['title'],video=request.FILES['file'])
            instance.save()
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = VideoForm()  
        return render(request,"upload.html",{'form':student})  
    
    