from django.shortcuts import render , HttpResponse
from datetime import datetime
from first.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    context = { 
        "variable" : "This is Django project" 
    }   # Variable should be assigned in dictionary

    return render(request,'index.html', context)
    # return HttpResponse('This is Home app')  #returns the message (displays text on screen)

def about(request):
    return render(request,'about.html')
    # return HttpResponse('This is about page')  #returns the message (displays text on screen)

def services(request):
    return render(request,'services.html')
    # return HttpResponse('This is services page')  #returns the message (displays text on screen)

def contact(request):
    
    if request.method == 'POST':
        # get the input text 
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        
        # Creating an object of Contact class with the parameters
        contact = Contact(name=name, email=email, phone=phone, description=description, date=datetime.today())
        contact.save()  # save or insert the data in the table
        
        # Displaying the success message
        messages.success(request, 'Form submitted successfully...')
        
    
    return render(request,'contact.html')
    # return HttpResponse('This is contact page')  #returns the message (displays text on screen)