from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
import jwt
# from scm.users import Users

# Create your views here.

# @csrf_exempt
# def get_token(request):
#     if request.method == "POST":
#         data = JSONParser().parse(request)
#         user_res = Users.objects.get(email_id=data["email_id"])
#         # user_res = serializers.serialize("json",user_res)
#         user_res = user_res.__dict__
#         if check_password(data["password"], user_res["password"]):
#             payload_data = {
#                 "sub": "4242",
#                 "name": "Jessica Temporal",
#                 "nickname": "Jess"
#             }
#             token = jwt.encode(
#                 payload=payload_data,
#                 key=settings.SECRET_KEY
#             )
#             print(token)
#             return JsonResponse({"response": "Logged In Successfully"}, status=201)
#         return JsonResponse({"response": "Log in Failed"}, status=400)
