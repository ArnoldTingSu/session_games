from django.shortcuts import render, HttpResponse, redirect
import random


# Create your views here.
def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
        request.session['activity'] = []
    return render(request,'ng_interface.html')

def process(request):
    request.session['gold'] +=1
    return redirect('/')

def farm(request):
    payout = round(random.random()*10) + 10
    request.session['activity'].append(f"You visited the farm and earned {payout} gold!")
    request.session['gold'] += payout
    return redirect('/')

def cave(request):
    payout = round(random.random()*5) + 5
    request.session['activity'].append(f"You visited the cave and earned {payout} gold!")
    request.session['gold'] += payout
    return redirect('/')

def house(request):
    payout = round(random.random()*3) + 2
    request.session['activity'].append(f"You visited the house and earned {payout} gold!")
    request.session['gold'] += payout
    return redirect('/')

def casino(request):
    payout = round(random.random()*100) - 50
    if payout < 0:
        request.session['activity'].append(f"You visited the casino and lost {payout} gold!")
    else:
        request.session['activity'].append(f"You visited the casino and earned {payout} gold!")
    request.session['gold'] += payout
    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['activity'] = []
    return redirect('/')