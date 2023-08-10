from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from .models import Visitor
from datetime import datetime
import pytz


def get_date_time():
    # Example date and time
    current_datetime = datetime.now(pytz.timezone("Asia/Kolkata"))

    # Format date as "DD/MM/YYYY"
    formatted_date = current_datetime.strftime("%d/%m/%Y")

    # Format time as "HH:MM AM/PM"
    formatted_time = current_datetime.strftime("%I:%M %p")

    # Combine date and time into a single string
    formatted_datetime_string = f"{formatted_date} {formatted_time}"

    return formatted_datetime_string


def apply(request):
    context = {}
    context['ids']: ['1844', '120033', '7413', '7020', '7713', '7090', '501511']
    context['names'] = [
        'Prof. Rajkumar - Associate Director (1st Year)',
        'Dr. Rajakoti - Assistant Director (1st Year)',
        'G.Srinivasa Rao - Junior Assistant',
        'B.Suresh - Junior Assistant',
        'B.Praveen Kumar - Attendant',
        'B.Appala Naidu - Attendant',
        'S.Surya Devi - Attendant',
    ]
    options = [
        "Certificate Verification", "Duplicate ID Card", "Course Registration",
        "Original TC, CC, submission (who are not submitted earlier)",
        "Admission Cancellation", "Timetables doubts", "Fee estimations",
        "Study certificates (Bank loans, Passport, Bus pass, etc…)",
        "Employee children’s bonafide certificates (Railway, Police, ARMY/NAVY, NMDC, others)",
        "Income tax exemption certificates",
        "Bus pass stamping (GITAM special & General)",
        "Bus Timings routes Information", "Moodle problems", "Coursera Issues",
        "Student portal passwords", "Email passwords", "Wifi connecting",
        "Students phone numbers changing", "Parents phone numbers changing",
        "Library Books Enquiry", "Mentors Details", "Class Teachers Details",
        "Dusters", "Markers", "Chalk piece", "NCC application stamping",
        "Sports details", "Tuition fee Issues", "Attendance Issues",
        "Marks Issues (Mid, Internals)", "RCE (Repeat Continues Evaluation)",
        "Summer Term", "Results", "Leaves enquiry",
        "Class Room for extra Class"
    ]

    context['reasons'] = options
    if request.POST:
        # print(f"\n{request.POST}\n")
        name = request.POST['name']
        regNum = request.POST['registrationnumber'].upper()
        mobile = request.POST['MobileNumber']
        reason_for_visiting = request.POST['reason_for_visiting']
        whom_did_you_meet = request.POST['whom_did_you_meet']
        description = request.POST['description']
        isProblemSolved = request.POST.get('problem_solved', False) == 'yes'
        rating = request.POST['rating']
        date = get_date_time()

        # Create a new Visitor object and save it to the database
        visitor = Visitor(
            name=name,
            regNum=regNum,
            mobile=mobile,
            reason_for_visiting=reason_for_visiting,
            whom_did_you_meet=whom_did_you_meet,
            description=description,
            isProblemSolved=isProblemSolved,
            rating=rating,
            date=date,
        )
        visitor.save()

        return render(request, 'success.html')

    return render(request, 'apply.html', context)


@login_required(login_url="feedbackapp:login")
def home(request):
    context = {}
    visitors = Visitor.objects.all()
    context['visitors'] = visitors
    return render(request, "home.html", context)


@login_required(login_url="feedbackapp:login")
def view(request, id):
    context = {}
    # visitor = Visitor.objects.get(regNum=regNum)
    visitor = get_object_or_404(Visitor, id=id)
    context['visitor'] = visitor
    return render(request, 'view.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect("feedbackapp:home")

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("feedbackapp:home")
        return redirect("feedbackapp:login")

    return render(request, "login.html")


@login_required(login_url="feedbackapp:login")
def logout(request):
    auth.logout(request)
    return redirect("feedbackapp:login")
