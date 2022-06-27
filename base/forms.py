from django import forms  
class VideoForm(forms.Form):  
    title = forms.CharField(label="Enter first name",max_length=50)  
      
   
    file      = forms.FileField() # for creating file input  