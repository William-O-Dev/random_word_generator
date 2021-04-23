from django.shortcuts import render, redirect

from django.utils.crypto import get_random_string

def index(request):

    return render(request, "index.html")


def random_word(request):
    if 'attempts' not in request.session:
        request.session['attempts']=0
    
    request.session['random_word']=get_random_string(length=14)
    request.session['attempts']+=1
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/random_word')

