import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from shyftlabs.shyftuser.models import ShyftUser
import datetime

# Create your views here.
@csrf_exempt
def getUser(request):
    if request.method == "GET":
        if request.GET['id']:
            try:
                retrieve = ShyftUser.objects.get(id=request.GET['id'], isdeleted=False)
                result = {}
                result['name'] = retrieve.shyft_name
                result['shyft_familyname'] = retrieve.shyft_familyname
                result['shyft_email'] = retrieve.shyft_email
                result['shyft_dob'] = str(retrieve.shyft_dob)
            except:
                return HttpResponse("User not found", status=500)
        return HttpResponse(json.dumps(result), content_type = "application/json")
    if request.method =="POST":
        shyftuser = ShyftUser()
        try:
            if request.POST['name']:
                shyftuser.shyft_name = request.POST['name']
            if request.POST['dob']:
                shyftuser.shyft_dob = datetime.datetime.fromisoformat(request.POST['dob'])
            if request.POST['email']:
                shyftuser.shyft_email = request.POST['email']
            if request.POST['familyname']:
                shyftuser.shyft_familyname = request.POST['familyname']
            if request.POST['type']:
                shyftuser.shyft_familyname = request.POST['type']
            shyftuser.save()
        except:
            return HttpResponse("Bad parameters", status=400)
        return HttpResponse("post request, please.", content_type="text/plain")
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
    if request.POST:
        try:
            if request.POST['userid']:
                retrieve = ShyftUser.objects.get(id=request.POST.get('userid'))
                retrieve.isdeleted = True
                retrieve.save()
        except:
            return HttpResponse("User not found", status=500)
        return HttpResponse("User Delete action succeeded", content_type="application/json")