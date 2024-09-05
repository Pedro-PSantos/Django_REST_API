from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request, format=None):

    if request.method == 'GET':

        #get all the drinks from the database
        drinks = Drink.objects.all()
        #serialize the drinks
        serializer = DrinkSerializer(drinks, many=True)
        #return the drinks in a JSON response
        return Response(serializer.data)
    
    if request.method == 'POST':

        #create a drink serializer
        serializer = DrinkSerializer(data=request.data)
        #if the serializer is valid
        if serializer.is_valid():
            #save the serializer
            serializer.save()
            #return the serializer in a JSON response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):
    
    #get the drink by id
    try: #see if the drink exists and get it if yes
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist: #if the drink does not exist show a 404 error
        return Response(status=status.HTTP_404_NOT_FOUND)

    #if the drink exists
    #check the request method
    #if the request method is GET
    if request.method == 'GET':
        #serialize the drink
        serializer = DrinkSerializer(drink)
        #return the drink in a serialized JSON response
        return Response(serializer.data)
    
    #if the request method is PUT
    elif request.method == 'PUT':
        #serialize the drink
        serializer = DrinkSerializer(drink, data=request.data)
        #if the serializer is valid
        if serializer.is_valid():
            #save the data
            serializer.save()
            #return the data in a JSON response
            return Response(serializer.data)
        #if the serializer is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #if the request method is DELETE
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)