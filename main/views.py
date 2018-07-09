from django.shortcuts import render
from .forms import AddWordsForm
from .models import AddWords
from django.shortcuts import render, HttpResponseRedirect,redirect, get_object_or_404

def index(request):
    return render(request, 'index.html',{})

def dashboard(request):
    return render(request, 'dashboard.html',{})

def registration(request):
    return render(request, 'registration.html',{})  

def addwords(request):
    if request.method == "POST":
        print('first location')
        addword = AddWords()
        form = AddWordsForm(instance=addword, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('addwords')
    else:
        print('second location')
        form = AddWordsForm()
    return render(request, "Addwords.html", {'form':form})
    
def review(request):
    return render(request, 'review.html',{})

def synonym(request):
    return render(request, 'synonym.html',{})    

def reversetesting(request):
    return render(request, 'reversetesting.html',{})    

def crosswordpuzzle(request):
    return render(request, 'crosswordpuzzle.html',{})    

def wordsonline(request):
    return render(request, 'wordsonline.html',{})    

def createnotes(request):
    return render(request, 'createnotes.html',{})    

def createtest(request):
    return render(request, 'createtest.html',{})    

def sharingtest(request):
    return render(request, 'sharingtest.html',{})    

def shareindividuals(request):
    return render(request, 'shareindividuals.html',{})    

def managesharedwords(request):
    return render(request, 'managesharedwords.html',{})    

def links(request):
    return render(request, 'links.html',{})    

def alternativedictionary(request):
    return render(request, 'alternativedictionary.html',{})    
