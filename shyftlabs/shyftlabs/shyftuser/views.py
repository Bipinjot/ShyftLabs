import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from shyftlabs.shyftuser.models import ShyftUser
import datetime
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
def getUser(request):
    if request.method == "GET":
        if request.GET['id']:
            try:
                retrieve = ShyftUser.objects.get(id=request.GET['id'], isdeleted=False)
                result = {}
                result['shyft_name'] = retrieve.shyft_name
                result['shyft_familyname'] = retrieve.shyft_familyname
                result['shyft_email'] = retrieve.shyft_email
                result['shyft_dob'] = str(retrieve.shyft_dob)
            except:
                return HttpResponse("User not found", status=500)
        return HttpResponse(json.dumps(result), content_type = "application/json")
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            shyftuser = ShyftUser()
            
            if 'name' in data:
                shyftuser.shyft_name = data['name']
            if 'dob' in data:
                shyftuser.shyft_dob = datetime.datetime.strptime(data['dob'], "%Y-%m-%d")
            if 'email' in data:
                shyftuser.shyft_email = data['email']
            if 'familyname' in data:
                shyftuser.shyft_familyname = data['familyname']
            if 'type' in data:
                shyftuser.shyft_usertype = data['type']
            
            shyftuser.save()
            
            return JsonResponse({'message': 'User created successfully'})
        
        except (json.JSONDecodeError, KeyError):
            # Return an error response if the JSON data is invalid
            return JsonResponse({'error': 'Bad parameters'}, status=400)
@csrf_exempt
def getAllUser(request):
    if request.method == "GET":
        retrieve = ShyftUser.objects.filter(isdeleted=False)
        users = []
        for retrivedUsers in retrieve:
            singleUser = {}
            singleUser['shyft_userid'] = retrivedUsers.id
            singleUser['shyft_name'] = retrivedUsers.shyft_name
            singleUser['shyft_familyname'] = retrivedUsers.shyft_familyname
            singleUser['shyft_email'] = retrivedUsers.shyft_email
            singleUser['shyft_dob'] = str(retrivedUsers.shyft_dob)
            users.append(singleUser)
        return HttpResponse(json.dumps(users), content_type="application/json")

@csrf_exempt
def deleteUser(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            if 'userid' in data:
                try:
                    retrieve = ShyftUser.objects.get(id=data['userid'])
                    retrieve.isdeleted = True
                    retrieve.save()
                    return JsonResponse({'message': 'User Delete action succeeded'})
                except ShyftUser.DoesNotExist:
                    return JsonResponse({'error': 'User not found'}, status=404)
            
            return JsonResponse({'error': 'Invalid request'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    
    # Return a 405 Method Not Allowed response for non-POST requests
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)