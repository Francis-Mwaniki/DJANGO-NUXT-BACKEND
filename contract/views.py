from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cook, Customer
from .serializers import CookSerializer,CustomerSerializer



class CooksRecipes(APIView):
    def get(self,request,format=None):
        recipes = Cook.objects.all()[0:2]
        serializer = CookSerializer(recipes,many=True)
        return Response(serializer.data)

class CooksAllRecipes(APIView):
    def get(self,request,format=None):
        recipes = Cook.objects.all()
        serializer = CookSerializer(recipes,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def CustomerEnd(request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    q = request.GET.get('query')
    if request.GET.get('query') != None:
         recipes = Cook.objects.filter(name__icontains=q)
         serializer = CookSerializer(recipes, many=True)
         return Response(serializer.data)
    else:
         return Response({"recipes": []})

   


       
