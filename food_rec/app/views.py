

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.contrib import messages

from .forms import KeywordForm, PriceRangeForm, LocationForm
from .models import Preference

from .yelp import YelpSearcher

# Create your views here.


def index(request):
    context = {'name': request.user}
    return render(request, 'home.html', context)


def login(request):
    return render(request, 'registration/login.html')


# PREFERENCES VIEWS


# def preference_list(request):
#     preferences = Preference.objects.all()
#     context = {'preferences': preferences}

#     return render(request, 'preferences/show.html', context)

# def preference(request):
#     context = {}
#     return render(request, '')
STEPS = {
    1: {
        'form': 'KeywordForm'
    },
    2: {
        'form': 'PriceRangeForm'
    },
    3:  {
        'form': 'LocationForm'
    }
}

SESSIONKEY_PREFIX = 'multistepform_step_'


def __getSessionData(request, step):
    ''' Get session data for a step '''
    return request.session.get(SESSIONKEY_PREFIX + str(step))


def __getFormData(request, step):
    ''' Get form data stored in session, or empty otherwise '''
    return globals()[STEPS[step]['form']](__getSessionData(request, step))


def __setFormData(request, step, data):
    ''' Store form data in session '''
    request.session[SESSIONKEY_PREFIX + str(step)] = data


def __getNextStep(request):
    ''' Try to get first step not completed by user '''
    for i in range(1, len(STEPS)):
        if __getSessionData(request, i) == None:
            return i
    return len(STEPS)  # there's data in all steps => go to last step


def create_preference(request, step):
    '''
    create a preference and save it to database
    '''
    temp_query = None
    results = None
    
    if step is None:
        request.session.flush() # remove session data
        temp_query = None
        return redirect('/step/' + str(1))
    # form = globals()[STEPS[step]['form']]() # default form for current step

    if request.method == 'POST':

        form = globals()[STEPS[step]['form']](request.POST)

        print(form)
        print(type(form))

        if step == 1:
            request.session['keywords'] = form.cleaned_data['keywords']
            return redirect('/step/' + str(2))

        elif step == 2:
            request.session['pricing_range'] = form.cleaned_data['pricing_range']
            return redirect('/step/' + str(3))

        elif step == 3:
            request.session['location'] = form.cleaned_data['location']
            request.session['distance'] = form.cleaned_data['distance']

            query = {
                'keywords': request.session['keywords'],
                'pricing_range': request.session['pricing_range'][0],
                'location': request.session['location'],
                'distance': request.session['distance']
            }

            # return render(request, 'search.html', context)
            if query != temp_query:
                searcher = YelpSearcher()
                results = searcher.search(
                    query['keywords'], query['location'], 
                    query['distance'], query['pricing_range'], 5)
                temp_query = query.copy()
                request.session['query'] = temp_query
                request.session['results'] = results
                
            if results:
                # return render(request, 'results.html', {
                #     'query': searcher.params,
                #     'results': results
                # })

                return redirect('/results/1')
            else:
                messages.error(request, 'No results found! Try another search.')
                return redirect('create-preference')

    else:
        # GET => try to get data from session (in case it was previously stored)
        form = __getFormData(request, step)

    return render(request, 'preferences/createMulti.html', {
        'form': form,
        'step': step,
        'step_last': len(STEPS)
    })

def results(request, result_num):
    all_results = request.session['results']
    chosen_result = all_results[result_num]
    return render(request, 'results.html', {'results': [chosen_result], 'result_num':result_num, 'query': request.session['query']})


# def edit_preference(request):
#     context = {}
#     return render(request, 'preferences/edit.html', context)

# def delete_preference(request):
#     return


'''
#### RESTAURANT VIEWS
    - get a preference
    - do a search based on that preference
    - get search results with list of restaurants
    - view list of restaurants
'''


def restaurants(request):
    return HttpResponse('Restaurant View')
