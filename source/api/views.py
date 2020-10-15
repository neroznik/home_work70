import json

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import ensure_csrf_cookie



@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')



def add_view(request, *args, **kwargs):
    data = None
    if request.body:
        data = json.loads(request.body)
    if type (data['A']) != int or (data['B']) != int:
        return HttpResponseBadRequest
    else:
        answer_add = data['A'] + data['B']
        answer = {'answer': answer_add
    }
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response

def subtract_view(request, *args, **kwargs):
    data = None
    if request.body:
        data = json.loads(request.body)
    if type (data['A']) != int or (data['B']) != int:
        return HttpResponseBadRequest
    else:
        answer_add = data['A'] - data['B']
        answer = {'answer': answer_add
    }
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response

def multiply_view(request, *args, **kwargs):
    data = None
    if request.body:
        data = json.loads(request.body)
    if type(data['A']) != int or (data['B']) != int:
        return HttpResponseBadRequest
    else:
        answer_add = data['A'] + data['B']
        answer = {'answer': answer_add
                  }
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response

def divide_view(request, *args, **kwargs):
    data = None
    if request.body:
        data = json.loads(request.body)
    if type(data['A']) != int or (data['B']) != int:
        return HttpResponseBadRequest
    elif  data['B'] != 0:
        answer_add = data['A'] / data['B']
        answer = {'answer': answer_add}
    else:
        answer = {'answer': 'Division by zero!'}
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response