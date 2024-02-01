from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import User
from rest_framework.response import Response

# User APIs.
@api_view(['POST'])
def create_user(request):
    
    name = request.data.get('name')
    email = request.data.get('email')
    membershipDate = request.data.get('membershipDate')
    if not name or not email or not membershipDate:
        return Response({"message": "Please provide all the required fields"}, status=400)
    user = User.objects.create(name=name, email=email, membershipDate=membershipDate)
    if not user:
        return Response({"message": "Something went wrong"}, status=500)
    return Response({"message": "User created successfully"}, status=201)

#get all users
@api_view(['GET'])
def all_users(request):
    users = User.objects.all()
    if not users:
        return Response({"message": "No users found"}, status=404)
    return Response({"users": users.values()}, status=200)

#get users by their id
@api_view(['POST'])
def get_user(request):
    userid = request.data.get('userid')
    if not userid:
        return Response({"message": "Please provide the userid"}, status=400)
    user = User.objects.filter(userid=userid)
    if not user:
        return Response({"message": "No user found"}, status=404)
    return Response({"user": user.values()}, status=200)