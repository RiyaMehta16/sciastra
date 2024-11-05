# courses/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course,Enrollment
from django.contrib.auth.decorators import login_required

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})



@login_required
def payment(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        Enrollment.objects.create(user=request.user, course=course)
        return render(request, 'courses/payment_confirmation.html', {'course': course})  # Redirect to confirmation page
    return render(request, 'courses/payment.html', {'course': course})
