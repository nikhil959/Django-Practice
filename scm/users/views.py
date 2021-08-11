from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import UsersSerializers
from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers
from .models import Users
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import jwt
from django.conf import settings


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

@csrf_exempt
def users_api(request):
    if request.method == "GET":
        users_res = Users.objects.all()
        serializer = UsersSerializers(users_res, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data["full_name"] = data["first_name"]+ " "+ data["last_name"]
        data["password"] = make_password(data["password"])
        serializer = UsersSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"response": "User Created Successfully"}, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def login(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        user_res = Users.objects.get(email_id=data["email_id"])
        # user_res = serializers.serialize("json",user_res)
        user_res = user_res.__dict__
        if check_password(data["password"], user_res["password"]):
            payload_data = {
                "sub": "4242",
                "name": "Jessica Temporal",
                "nickname": "Jess"
            }
            token = jwt.encode(
                payload=payload_data,
                key=settings.SECRET_KEY
            )
            print(token)
            print(jwt.decode(token, key=settings.SECRET_KEY, algorithms=['HS256', ]))
            return JsonResponse({"response": "Logged In Successfully"}, status=201)
        return JsonResponse({"response": "Log in Failed"}, status=400)

@csrf_exempt
def get_token(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        if not data or not {"email", "password"}.issubset(data.keys()):
            JsonResponse({"response": "Required Fields Missing"}, status=400)
        user_res = Users.objects.get(email_id=data["email_id"])
        user_res = UsersSerializers(user_res).data
        if check_password(data["password"], user_res["password"]):
            token = jwt.encode(
                payload=user_res,
                key=settings.SECRET_KEY
            )
            return {"Token": token}, 200
        else:
            return {"response": "Invalid Credentials"}, 403

# @csrf_exempt
def validate_token(token):
    data = jwt.decode(token, key=settings.SECRET_KEY, algorithms=['HS256', ])



