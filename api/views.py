import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def addNumbers(request):
  if request.method == 'POST':
    try:
      numbers = json.loads(request.body)['numbers']
      response = json.dumps({'addition': sum(numbers)})
    except:
      response = json.dumps({'error': 'Request contains non-numeric data!'})
  else:
    response = json.dumps({'error': 'Request must be POST!'})
  return HttpResponse(response, content_type='text/json')


@csrf_exempt
def multiplyNumbers(request):
  if request.method == 'POST':
    try:
      numbers = json.loads(request.body)['numbers']
      product = 1
      for number in numbers:
        product *= number
      response = json.dumps({'product': product})
    except:
      response = json.dumps({'error': 'Request contains non-numeric data!'})
  else:
    response = json.dumps({'error': 'Request must be POST!'})
  return HttpResponse(response, content_type='text/json')