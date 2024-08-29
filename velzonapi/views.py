from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from velzonapi.models import State,Users,City
from velzonapi.serializers import StateSerializer, UsersSerializer,CitySerializer
from django.contrib.auth import authenticate, login
from rest_framework import status
from .serializers import LoginSerializer
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist



class LoginView(APIView):
    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return JsonResponse({"message": "Login successful"}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class Login_View(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#             login(request, user)
#             return JsonResponse({"message": "Login successful"}, status=status.HTTP_200_OK)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET'])
def getDate(request):
    state = State.objects.all()
    serializer = StateSerializer(state, many=True)
    return JsonResponse(serializer.data, safe=False)
@api_view(['GET'])
def getCity(request):
    city = City.objects.all()
    serializer = CitySerializer(city, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def user_getDate(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def addState(request): 
    serializer = StateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


@api_view(['POST'])
def addUsers(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

@api_view(['POST'])
def addCity(request): 
    serializer = CitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

@api_view(['PUT'])
def updateState(request, id):
    item1 = State.objects.get(id=id)
    serializer = StateSerializer(item1, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "Updated Successfully"}, safe=False)
    return JsonResponse({"error": "Failed to update"}, safe=False)

@api_view(['PUT'])
def updateUsers(request, id):
    item1 = Users.objects.get(id=id)
    serializer = UsersSerializer(item1, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "Updated Successfully"}, safe=False)
    return JsonResponse({"error": "Failed to update"}, safe=False)

@api_view(['DELETE'])
def deteteState(request,id):
    item=State.objects.get(id=id)
    item.delete()
    return JsonResponse("Deleted successfully")
 

      