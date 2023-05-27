import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from shyftlabs.shyftcourse.models import ShyftCourse


# Create your views here.
@csrf_exempt
def course(request):
    if request.method == "POST":
        if request.POST['coursename']:
            course = ShyftCourse()
            course.shyft_coursename = request.POST['coursename']
            course.save()
            return HttpResponse("Post request for course save", content_type="text/plain")
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
    if request.method == "POST":
        try:
            if request.POST['courseid']:
                retrieve = ShyftCourse.objects.get(id=request.POST.get('courseid'))
                retrieve.isdeleted = True
                retrieve.save()
        except:
            return HttpResponse("Course not found", status=500)
        return HttpResponse("Delete action succeeded", content_type="application/json")

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