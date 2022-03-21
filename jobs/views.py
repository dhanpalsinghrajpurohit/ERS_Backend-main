import http
import json

import rest_framework.exceptions
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from django.db.models import Q
from django.core.mail import send_mail

# from .models import Jobs, Applicant,ShortlistCandidate,SelectedCandidate
# from .serializer import JobSerializer,ApplicantSerializer,ShortlistCandidateSerializer,SelectedCandidateSerializer,JobUpdateSerializer,checkStatusSerializer,shortlistjobSerializer,selectedlistjobSerializer
from .serializer import *
from userAccounts.serializer import userProfileSerializer
from userAccounts.models import userProfile
#,AppliedCandidateSerializer
# Create your views here.

## insert job
@api_view(['POST'])
def  insertJob(request):
    if request.method == "POST":
        user = User.objects.get(username=request.data['username'])
        data = {"user": user.id}
        request.data.update(data)
        print(request.data)
        jobs = JobSerializer(data=request.data)
        if jobs.is_valid():
            jobs.save()
            return Response({"status": "success", "data": jobs.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": jobs.errors}, status=status.HTTP_400_BAD_REQUEST)

# fetch all jobs
@api_view(['GET'])
def get_jobs(request):
    send_mail('subject', 'body of the message', 'dhanpal.singh.rajpurohit09@gmail.com', ['kayamap866@shackvine.com'])
    print(request.data)
    jobs = Jobs.objects.all()
    serializer = JobSerializer(jobs,many=True)
    if serializer.data is not None:
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#fetch single job
@api_view(['POST'])
def get_singlejob(request):
    if request.data != {} and request.data['id']:
        job = Jobs.objects.filter(id=request.data['id'])
        serializer = JobSerializer(job,many=True)
        if serializer.data is not None:
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"status": "error", "message": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)

#fetch job user specific
@api_view(['POST'])
def get_job(request):
    if request.data != {}:
        user = User.objects.get(username=request.data['username'])
        data = {"user": user.id}
        request.data.update(data)
        applied = Applicant.objects.filter(user=request.data['user']).values('job')
        my_task_ids = [d['job'] for d in applied]
        job =  Jobs.objects.exclude(id__in=my_task_ids)
        serializer = JobSerializer(job,many=True)
        if serializer is not None:
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
             return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"status": "error", "data": None,"message":"Please Signin!!!"}, status=status.HTTP_400_BAD_REQUEST)

# delte job
@api_view(['DELETE'])
def delete_job(request):
    try:
        if request.data != {} and request.data['id']:
            job = Jobs.objects.get(id=request.data['id'])
            job.delete()
            return Response({"status": "success", "message": "Job Deleted."}, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"status": "failed", "message": "Error Occured. "+str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."}, status=status.HTTP_400_BAD_REQUEST)

#update job for admin
@api_view(['PUT'])
def update_job(request):
    try:
        if request.data != {} and request.data['id']:
            job = Jobs.objects.get(id=request.data['id'])
            serializer = JobUpdateSerializer(data=request.data,instance=job,partial=True)
            print(serializer)

            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                return Response({"status": "success", "message": "Job Updated."}, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"status": "failed", "message": "Error Occured. " + str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."}, status=status.HTTP_400_BAD_REQUEST)

#apply job
@api_view(['POST'])
def applyjob(request):
    print(request.data)
    if request.method == "POST":
        user = User.objects.get(username=request.data['username'])
        data = {"user": user.id}
        request.data.update(data)
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#fetch applicant
@api_view(['GET'])
def get_applicant(request):
    applicant = Applicant.objects.distinct()
    data = []
    for row in applicant:
        dict = {
            'id':row.job.id,
            'title':row.job.title
        }
        data.append(dict)
    return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)

#delete applicant
@api_view(['DELETE'])
def delete_applicant(request):
    try:
        if request.data != {} and request.data['job']:
            applicant = Applicant.objects.filter(job=request.data['job'],user=request.data['id'])
            applicant.delete()
            return Response({"status": "success", "message":"Data deleted successful."}, status=status.HTTP_200_OK)
        return Response({"status": "success", "message": "Invalid required data."}, status=status.HTTP_400_BAD_REQUEST)
    except BaseException as exption:
        return Response({"status": "success", "message": "Error occured"+str(exption)}, status=status.HTTP_400_BAD_REQUEST)

#get user details
@api_view(['POST'])
def get_applicantdetails(request):
    try:
        if request.data and request.data['jobid'] is not None:
            users = userProfile.objects.filter(user__applicant__job=request.data['jobid'],user__applicant__is_shortlist="1")
            serializer = userProfileSerializer(users, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    except BaseException as exception:
        return Response({"status": "failed", "message":"Exception : "+str(exception)}, status=status.HTTP_400_BAD_REQUEST)
    return  Response({"status": "failed","message":"Enter Valid Data."}, status=status.HTTP_400_BAD_REQUEST)

#insert in shortlist table
@api_view(['POST'])
def insert_shortlist(request):
    if request.data != {}:
        # if request.user:
        serializer = ShortlistCandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    return  Response({"status": "failed","data": serializer.errors,"message":"Enter Valid Data."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_shortlist(request):
    try:
        if request.data != {} and request.data['job'] and request.data['user']:
                serializer = ShortlistCandidate.objects.get(job=request.data['job'],user=request.data['user'])
                serializer = ShortlistCandidateSerializer(data=request.data,instance=serializer)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"status": "failed", "message": "Error Occured."},
                            status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."},status=status.HTTP_400_BAD_REQUEST)

#fetch all shortlisted user
@api_view(['POST'])
def get_shortlist(request):
    try:
        if request.data != {} and request.data['job']:
            serializer = userProfile.objects.filter(user__shortlistcandidate__job=request.data['job'],user__shortlistcandidate__is_shortlist="1")
            serializer = userProfileSerializer(serializer,many=True)
            if serializer.data is not None:
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"status": "failed", "message": "Error Occured."},
                            status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."},status=status.HTTP_400_BAD_REQUEST)

#fetch all selected job based on user
@api_view(['POST'])
def get_shortlistUser(request):
    try:
        if request.data != {} and request.data['user']:
            user = User.objects.get(username=request.data['user'])
            job = ShortlistCandidate.objects.filter(user=user.id,is_shortlist="3")
            serializer = shortlistjobSerializer(job,many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"status": "failed", "message": "Error Occured."},
                            status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."},status=status.HTTP_400_BAD_REQUEST)

#fetch all rejected job based on user
@api_view(['POST'])
def get_shortlistRejectUser(request):
    try:
        if request.data != {} and request.data['user']:
            user = User.objects.get(username=request.data['user'])
            job = Applicant.objects.filter(user=user.id,is_shortlist="2")
            serializer = shortlistjobSerializer(job,many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"status": "failed", "message": "Error Occured."},
                            status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."},status=status.HTTP_400_BAD_REQUEST)

#insert selected user
@api_view(['POST'])
def insert_selectedlist(request):
    print(request.data)
    try:
        if request.data != {} and request.data['job'] and request.data['user']:
        # update
            serializer = ShortlistCandidate.objects.get(job=request.data['job'], user=request.data['user'])
            serializer = ShortlistCandidateSerializer(data=request.data, instance=serializer)
            if serializer.is_valid():
                serializer.save()
                #insert
                serializer = SelectedCandidateSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"status": "failed", "message": "Error Occured."+str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."},status=status.HTTP_400_BAD_REQUEST)

#fetch user who is selected for admin
@api_view(['POST'])
def get_selectedlist(request):
    print(request.data)
    try:
        if request.data != {} and request.data['job']:
            serializer = userProfile.objects.filter(user__selectedcandidate__job=request.data['job'])
            serializer = userProfileSerializer(serializer, many=True)
            # selectedlist = SelectedCandidate.objects.filter(job=request.data['job'])
            # serializer = SelectedCandidateSerializer(selectedlist,many=True)
            if serializer.data is not None:
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"status": "failed", "message": "Error Occured."},status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."},status=status.HTTP_400_BAD_REQUEST)

#fetch selected candidate job based on user
@api_view(['POST'])
def get_selectjob_User(request):
    try:
        if request.data != {} and request.data['user']:
            user = User.objects.get(username=request.data['user'])
            job = SelectedCandidate.objects.filter(user=user.id)
            serializer = selectedlistjobSerializer(job,many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"status": "failed", "message": "Error Occured."},
                            status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."},status=status.HTTP_400_BAD_REQUEST)

#fetch rejected candidate job based on user
@api_view(['POST'])
def get_selectedjob_RejectUser(request):
    try:
        if request.data != {} and request.data['user']:
            user = User.objects.get(username=request.data['user'])
            job = ShortlistCandidate.objects.filter(user=user.id, is_shortlist="2")
            serializer = shortlistjobSerializer(job, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"status": "failed", "message": "Error Occured."},
                        status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."}, status=status.HTTP_400_BAD_REQUEST)


#fetch unsechduled job
@api_view(['POST'])
def get_schedule(request):
    try:
        if request.data != {} and request.data['user']:
            user = User.objects.get(username=request.data['user'])
            applicant = Applicant.objects.filter(user=user.id,is_shortlist="1")
            serializer = scheduleSerializer(applicant,many=True)
            if serializer.data is not None:
                return Response({"status":"success","data":serializer.data,"message":"data getted successfully."},status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"status": "failed", "error":"ERROR : "+str(e), "message": "error occured"},
                 status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."}, status=status.HTTP_400_BAD_REQUEST)

#insert schedule
@api_view(['POST'])
def insert_schedule(request):
    try:
        if request.data != {} and request.data['user']:
            user = User.objects.get(username=request.data['user'])
            data={ 'user':user.id}
            request.data.update(data)
            serializer = scheduleSerializer1(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":"success","data":serializer.data,"message":"data getted successfully."},status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"status": "failed", "error":"ERROR : "+str(e), "message": "error occured"},
                 status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def show_schedule(request):
    try:
        if request.data != {} and request.data['user']:
            user = User.objects.get(username=request.data['user'])
            schedule = Schedule.objects.filter(user=user.id)
            serializer = scheduleSerializer1(schedule, many=True)
            if serializer.data is not None:
                return Response({"status": "success", "data": serializer.data, "message": "data getted successfully."},
                                status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"status": "failed", "error": "ERROR : " + str(e), "message": "error occured"},
                        status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": "failed", "message": "Enter Valid Data."}, status=status.HTTP_400_BAD_REQUEST)
