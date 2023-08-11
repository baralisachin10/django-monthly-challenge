from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
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
    'december' : 'Enjoy Christmas!'
}

# Create your views here.

def index(request):
    list_item = ""
    months = list(monthly_challenges.keys());

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge',args=[month])
        list_item += f'<li><a href="{month_path}"><h1>{capitalized_month}</h1></a></li>'

    response_data = f"<ul>{list_item}</ul>"
    return HttpResponse(response_data)



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
        return HttpResponseNotFound('<h1>Invalid month</h1>')

