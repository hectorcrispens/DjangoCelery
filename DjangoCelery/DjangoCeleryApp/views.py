from django.shortcuts import render, HttpResponse
from DjangoCelery.task import *
import json
# Create your views here.
def prueba(request):
    res = ''
    for x in range(1000000):
        res = res + genstr(x)+'\n'
    return HttpResponse("Hola Mundo " + res)

def resp(request):
    # some JSON:
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    # parse x:
    y = json.loads(x)
    return HttpResponse(y["age"])