from django.shortcuts import render
from django.http import HttpResponse
from .models import Notefile
from skynote_app import forms


# Create your views here.
def login(request):
    diction={}
    return render(request,"skynote_app/login.html", context=diction)

def registration(request):
    diction = {}
    return render(request,"skynote_app/registration.html", context=diction)

def index(request):
    new_form = forms.notes_form() 
    diction = {'form_note': new_form}
    
    if request.method == 'POST':
        new_form = forms.notes_form(request.POST)
        if new_form.is_valid():
            # new_form.save(commit=True)
            title = new_form.cleaned_data['title']
            note_text = new_form.cleaned_data['note_text']
            note = Notefile(title=title, note_text=note_text)
            note.save()
            # return library(request)
    return render(request,"skynote_app/index.html", context=diction)

def library(request):
    notes = Notefile.objects.all()
    diction = {'notes': notes}
    return render(request,"skynote_app/library.html", context=diction)

def note_details(request):
    notes = Notefile.objects.all()
    diction = {'notes': notes}
    return render(request,"skynote_app/note_details.html", context=diction)

def test(request):
    diction = {}
    return render(request,"skynote_app/test.html", context=diction)