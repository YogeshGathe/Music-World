from functools import partial
import json
from django.shortcuts import render

from api.models import Chord
from .serializer import ChordSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#Model object- Single song chord

def chord_detail(request, pk):
    cd = Chord.objects.get(id=pk)
    serializer = ChordSerializer(cd)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

#Model object- All song chord

def all_chord_detail(request):
    cd = Chord.objects.all()
    serializer = ChordSerializer(cd, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def chord_create(request): 
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        serializer= ChordSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def chord_delete(request): 
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        id=pythondata.get('id')
        chrd=Chord.objects.get(id=id)
        chrd.delete()
        res={'msg':'Data Deleted!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def chord_update(request): 
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        id=pythondata.get('id')
        chrd=Chord.objects.get(id=id)
        serializer= ChordSerializer(chrd, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Partially Updated!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
        

    
            



