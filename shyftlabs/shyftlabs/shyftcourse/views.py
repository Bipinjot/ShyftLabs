import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from shyftlabs.shyftcourse.models import ShyftCourse


# Create your views here.
@csrf_exempt
def course(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            if 'coursename' in data:
                course = ShyftCourse()
                course.shyft_coursename = data['coursename']
                course.save()
                return JsonResponse({'message': 'Post request for course save'})
            
            return JsonResponse({'error': 'Invalid request'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

            
    if request.method == "GET":
        try:
            if request.GET['courseid']:
                retrieve = ShyftCourse.objects.get(id=request.GET['courseid'], isdeleted=False)
                result = {}
                result['courseid'] = retrieve.id
                result['coursename'] = retrieve.shyft_coursename
        except:
            return HttpResponse("Course not found", status=500)
        return HttpResponse(json.dumps(result), content_type="application/json")

@csrf_exempt
def deleteCourse(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            if 'courseid' in data:
                try:
                    retrieve = ShyftCourse.objects.get(id=data['courseid'])
                    retrieve.isdeleted = True
                    retrieve.save()
                    return JsonResponse({'message': 'Delete action succeeded'})
                except ShyftCourse.DoesNotExist:
                    return JsonResponse({'error': 'Course not found'}, status=404)
            
            return JsonResponse({'error': 'Invalid request'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

@csrf_exempt
def allcourse(request):
    if request.method == "GET":
        retrieve = ShyftCourse.objects.filter(isdeleted=False)
        courses = []
        for retrivedCourses in retrieve:
            singleCourse = {}
            singleCourse['shyft_courseid'] = retrivedCourses.id
            singleCourse['shyft_coursename'] = retrivedCourses.shyft_coursename
            courses.append(singleCourse)
        return HttpResponse(json.dumps(courses), content_type="application/json")