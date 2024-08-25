from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Course, CourseInstance



def home(request):
    courses = Course.objects.all()
    return render(request,'courses/home.html',{'courses':courses})

def all_courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/view_courses.html', context)

def del_course(request, course_id):
    if course_id:
        try:
            clicked_course = Course.objects.filter(id=course_id)
            clicked_course.delete()
            return HttpResponse("Course removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid Course ID")

def del_course_ins(request, course_id):
    if course_id:
        try:
            clicked_course = CourseInstance.objects.filter(id=course_id)
            clicked_course.delete()
            return HttpResponse("Course Instance removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid Course ID")

def all_courses_ins(request):
    coursesIns = CourseInstance.objects.all()
    context = {'coursesIns':coursesIns}
    return render(request,'courses/view_courseIns.html',context)

def show_selected_data(request, course_id):
    print(course_id)
    if course_id:
        try:
            # Retrieve the course based on the provided course_id
            clicked_course = Course.objects.all()
            clicked_course = clicked_course.filter(id=course_id)
            print(clicked_course)
            context = {'clicked_course': clicked_course}
            return render(request, 'courses/show_data.html', context)
        except Course.DoesNotExist:
            return HttpResponse("Please Enter A Valid Course ID")
    else:
        return HttpResponse("Course ID not provided.")

def show_selected_data_ins(request, course_id):
    print(course_id)
    if course_id:
        try:
            # Retrieve the course based on the provided course_id
            clicked_course = CourseInstance.objects.all()
            clicked_course = clicked_course.filter(id=course_id)
            print(clicked_course)
            context = {'clicked_course': clicked_course}
            return render(request, 'courses/show_data_ins.html', context)
        except Course.DoesNotExist:
            return HttpResponse("Please Enter A Valid Course ID")
    else:
        return HttpResponse("Course ID not provided.")



def add_course(request):
    if request.method == 'POST':
        print(request.POST)
        title1 = request.POST.get('titles')
        course_code = request.POST.get('course_code')
        description = request.POST.get('description')

        if title1 and course_code and description:
            new_course = Course(title=title1, course_code=course_code, description=description)
            new_course.save()
            return HttpResponse('Course added Successfully')
        else:
            return HttpResponse('Missing data. Course not added.')

    elif request.method == 'GET':
        return render(request, 'courses/add_courses.html')
    else:
        return HttpResponse("An Exception Occurred! Course Has Not Been Added")

def add_course_ins(request):
    if request.method == 'POST':
        print(request.POST)
        title_id = request.POST.get('selectCourse')
        year = request.POST.get('year')
        sem = request.POST.get('sem')
        course_code = request.POST.get('course_code')

        print("Title ID:", title_id)


        if title_id and year and sem and course_code:
            course = get_object_or_404(Course, id=title_id)
            print(course)
            new_course_ins = CourseInstance(course=course, year=year, semester=sem, course_code=course_code)
            new_course_ins.save()
            return HttpResponse('Course Instance added Successfully')
        else:
            return HttpResponse('Missing data. Course Instance not added.')

    elif request.method == 'GET':
        courses = Course.objects.all()
        print(courses)
        return render(request, 'courses/add_courseIns.html', {'courses': courses})
    else:
        return HttpResponse("An Exception Occurred! Course Instance Has Not Been Added")