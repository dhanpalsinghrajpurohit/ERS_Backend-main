from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializer import UserSerializer, UserSerializerWithToken, HRSerializer, userProfileSerializer, insert_Profile, \
    CustomTokenObtainPairSerializer
from .models import HRProfile, userProfile

@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    if serializer.data is not None:
        return Response({"status": "success","data":serializer.data,"message": "Register Successfully."},
                        status=status.HTTP_200_OK)
    return Response({"status": "failed", "data": [], "message": "Something went wrong."},
                    status=status.HTTP_400_BAD_REQUEST)




class UserList(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success","data":serializer.data,"message": "Register Successfully."},
                            status=status.HTTP_200_OK)
        return Response({"status": "failed","data":[],"message": "Something went wrong."},
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insertHR(request):
    user = User.objects.get(username=request.data['username'])
    data  = {"id":user.id}
    request.data.update(data)
    print(request.data)
    serializer = HRSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_users(request):
    try:
        # if request.user:
        users = userProfile.objects.all()
        serializer = userProfileSerializer(users,many=True)
        if serializer.data is not None:
            return Response({"status":"success","data":serializer.data}, status=status.HTTP_200_OK)
        return Response({"status":"failed","message":serializer.serializer.errors['non_field_errors'][0]},status=status.HTTP_204_NO_CONTENT)
        # return Response({"status":"failed","message":"Unauthorized Access"},status=status.HTTP_401_UNAUTHORIZED)
    except BaseException as exception:
        return Response({"status":"failed","message:":"Exception "+str(exception)},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_user(request):
    try:
        # if request.user:
        if request.data != {} and request.data['user']:
            print(request.data)
            user = User.objects.get(username=request.data['user'])
            user = userProfile.objects.filter(user=user)
            print(user)
            serializer = userProfileSerializer(user,many=True)
            if serializer.data is not None:
                return Response({"status":"success","data":serializer.data}, status=status.HTTP_200_OK)
            return Response({"status":"failed","message":serializer.serializer.errors['non_field_errors'][0]},status=status.HTTP_204_NO_CONTENT)
        return Response({"status":"failed","message":"Unauthorized Access"},status=status.HTTP_401_UNAUTHORIZED)
    except BaseException as exception:
        return Response({"status":"failed","message":"Exception "+str(exception)},status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Invalid Data "}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def insert_user(request):
    try:
        if request.data!= {} and request.data['user']:
            user = User.objects.get(username=request.data['user'])
            serializer = insert_Profile(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "failed", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except BaseException as e:
        return Response({"status": "failed", "message":"Enter Valid "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_user(request):
    try:
        if request.data != {} and request.data['user']:
            user = userProfile.objects.get(user=request.data['user'])
            serializer = userProfileSerializer(data=request.data, instance=user)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "failed", "message": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)
    except BaseException as e:
        return Response({"status": "failed", "message": "Enter Valid " + str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
     serializer_class = CustomTokenObtainPairSerializer