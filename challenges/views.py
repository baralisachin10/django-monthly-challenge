from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    'january':'Eat no meat for entire month!',
    'february':'walk 20 minutes per day!',
    'march':'Learn everyday django for 20 minutes!',
    'april':'Eat no meat for entire month!',
    'may': 'learn python',
    'june':'walk 20 minutes per day!',
    'july': 'Learn everyday django for 20 minutes!',
    'august':'Eat no meat fro entire month',
    'september': 'learn javascript',
    'october':'Celebrate birthday',
    'november':'enjoy the rain in november',
    'december' : None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys());
    return render(request,'challenges/index.html',{
        'months':months,
    })



def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month');

    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args= [redirect_month])
    return HttpResponseRedirect(redirect_path);



def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html',{
            'text': challenge_text,
            'month_name':month,
        });
    except:
        raise Http404()

