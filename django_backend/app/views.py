from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from app.serializers import UserSerializer
from .models import User, Messages
import hashlib
import hmac

@api_view(['GET'])
def index(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
@csrf_exempt

def login(request):
    if request.method == "POST":
        data = request.body
        if request.content_type == 'application/json':
            data = json.loads(data)
            username = data.get('username')
            password = data.get('password')
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return JsonResponse({'error': 'Invalid username or password.'}, status=401)
            if user.password == password:
                # set session variables if login is successful
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return JsonResponse({'message': 'Login successful.'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid username or password.'}, status=401)
        else:
            return JsonResponse({'error': 'Request body must be in JSON format.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

        

@api_view(['POST'])
@csrf_exempt
def signup(request):
    if request.method == "POST":
        data = request.body
        if request.content_type == 'application/json':
            data = json.loads(data)
        user = User.objects.create(username=data['username'], password=data['password'])
        user.save()
        return HttpResponse("Sign In S ucess")
    else:
        return HttpResponse("Post request only")

@api_view(['POST'])
@csrf_exempt
def send_message(request):
    if request.method == "POST":
        data = request.body
        if request.content_type == 'application/json':
            data = json.loads(data)
            # assuming the request data has keys 'user' and 'content'
            username_1 = data.get('username_1')
            username_2 = data.get('username_2')
            content = data.get('content')
            # create a new Message instance
            message = Messages.objects.create(username_1=username_1, username_2=username_2, content=content)
            # return a success response
            return JsonResponse({'message': 'Message sent successfully.'}, status=201)
        else:
            # return an error response if the request body is not in JSON format
            return JsonResponse({'error': 'Request body must be in JSON format.'}, status=400)
    else:
        # return an error response if the request method is not POST
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

'''
TODO
- login security 
    - master key
    - key function generator
    - user signup in with password and username
    - user key function generator to generator a hash value/key
    - the hash value is stored in server 
    - when user logins
    - the server gets the username 
- message security
    - HMAC - sha256
    

- create user -> 
object: {
    public: xxxxx
    
}
'''
def hmac_digest(key, message):
    key = bytes(key, "utf-8")
    message = bytes(message, "utf-8")
    dig = hmac.new(key, message, hashlib.sha256)
    return dig.hexdigest()

def secrete_key_generator():

    pass

def hmac_decode(key, message):

    pass

