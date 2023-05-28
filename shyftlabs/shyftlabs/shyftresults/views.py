import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from shyftlabs.shyftresults.models import ShyftResults
from django.http import JsonResponse

@csrf_exempt
# Create your views here.
def result(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            result = ShyftResults()
            if 'username' in data:
                result.shyft_username = data['username']
            if 'coursename' in data:
                result.shyft_coursename = data['coursename']
            if 'score' in data:
                result.shyftresult_score = data['score']
            result.save()
            
            return JsonResponse({'message': 'Result created successfully'})
        
        except (json.JSONDecodeError, KeyError):
            # Return an error response if the JSON data is invalid
            return JsonResponse({'error': 'Bad parameters'}, status=400)

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
                singleResult['shyft_resultuser'] = retrivedResult.shyft_username
                singleResult['shyft_resultcourse'] = retrivedResult.shyft_coursename
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