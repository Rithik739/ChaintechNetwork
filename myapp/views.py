from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.http import HttpResponse
import random
from .form import UserForm


quotes = [
    "The best way to predict the future is to create it.",
    "Do not watch the clock. Do what it does. Keep going.",
    "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.",
    "One cannot and must not try to erase the past merely because it does not fit the present.",
    "Yesterday's the past, tomorrow's the future, but today is a gift.",
    "Change is the law of life.",
    "Success is not final; failure is not fatal: It is the courage to continue that counts.",
    "Believe you can and you're halfway there."
]

# View for Home Page
def home(request):
    current_time = datetime.now()  
    random_quote = random.choice(quotes) 
    form = UserForm()


    return render(request, 'home.html', {
        'current_time': current_time, 
        'random_quote': random_quote,
        'form': form,
       
    })

# View for About Page
def about(request):
    return render(request, 'about.html')

# View for Contact Page
def contact(request):
    return render(request, 'contact.html')


#view for Submitted data page
# def form(request):

#     # Create an instance of the UserForm
#     submitted_data = None

#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             # submitted_data = form.cleaned_data
#             return HttpResponseRedirect(reverse('form_page'))
#         else:
#             form = UserForm() 

#     return render(request, 'form.html',{
#         'submitted_data': submitted_data 
#     })
# def form(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             # Process the form data
#             return HttpResponse('Form submitted successfully')
#     else:
#         form = UserForm()
    
#     return render(request, 'submit-form.html', {'form': form})

def form(request):
    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = UserForm(request.POST)
        submitted_data = None
        
        if form.is_valid():
            submitted_data = form.cleaned_data

            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            # Pass the submitted data to the new template (submit-form.html)
            return render(request, 'submit-form.html', {'name': name, 'email': email})
    else:
        # If GET request, render the empty form
        form = UserForm()

    # Render the form page
    return render(request, 'form.html', {'form': form})