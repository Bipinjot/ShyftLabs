import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from shyftlabs.shyftresults.models import ShyftResults

from shyftlabs.shyftcourse.models import ShyftCourse

from shyftlabs.shyftuser.models import ShyftUser

@csrf_exempt
# Create your views here.
def result(request):
    if request.POST:
        try:
            result = ShyftResults()
            if request.POST['userid']:
                user = ShyftUser.objects.get(id=request.POST['userid'], isdeleted=False)
                if user:
                    result.shyftresult_user = user
            else:
                return HttpResponse("userid: Bad parameters", status=400)
            if request.POST['courseid']:
                course = ShyftCourse.objects.get(id=request.POST['courseid'], isdeleted=False)
                if course:
                    result.shyftresult_course = course
            else:
                return HttpResponse("courseid: Bad parameters", status=400)
            if request.POST['score']:
                result.shyftresult_score = request.POST['score']
            else:
                return HttpResponse("score: Bad parameters", status=400)
            result.save()
        except:
            return HttpResponse("Error in saving result", status=500)
    return HttpResponse("Result save action succeeded", content_type="application/json")

@csrf_exempt
def getAllResults(request):
    resultJson = []
    if request.method == "GET":
        try:
            results = ShyftResults.objects.filter(isdeleted=False)
            if 'courseid' in request.GET:
                results = results.filter(shyftresult_course__id=request.GET['courseid'])
            if 'userid' in request.GET:
                results = results.filter(shyftresult_user__id=request.GET['userid'])
            for retrivedResult in results:
                singleResult = {}
                singleResult['shyft_resultid'] = retrivedResult.id
                singleResult['shyft_resultuser'] = retrivedResult.shyftresult_user.id
                singleResult['shyft_resultcourse'] = retrivedResult.shyftresult_course.id
                singleResult['shyft_resultscore'] = retrivedResult.shyftresult_score
                resultJson.append(singleResult)
        except:
            return HttpResponse("Bad parameters", status=400)
    return HttpResponse(json.dumps(resultJson), content_type="application/json")

@csrf_exempt
def deleteResult(request):
    if request.method == "POST":
        try:
            if 'resultid' in request.POST:
                result = ShyftResults.objects.get(id=request.POST['resultid'], isdeleted=False)
                result.isdeleted = True
                result.save()
                return HttpResponse("Result Deleted", status=200)
            else:
                return HttpResponse("Bad parameters", status=400)
        except:
            return HttpResponse("Bad parameters", status=400)