from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):


    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate = collaborate_form.save(commit=False)
            collaborate.name = request.POST.get('name')
            collaborate.email = request.POST.get('email')
            collaborate.message = request.POST.get('message')
            collaborate.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Collaboration request succesfully submitted!'
            )

    collaborate_form = CollaborateForm()





    return render(
        request,
        "about/about.html",
        {
        "about": about,
        "collaborate_form": collaborate_form, 
        },
    )


