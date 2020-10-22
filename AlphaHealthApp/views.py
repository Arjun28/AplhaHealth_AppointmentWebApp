from django.shortcuts import render, HttpResponse
from django.http import JsonResponse 
import json
from AlphaHealthApp.models import Users
from AlphaHealthApp.models import UsersInfo
from AlphaHealthApp.models import UsersAppointments


def index(request):
    return render(request, 'AlphaHealthApp/index.html')

def PatientLogin(request):
    return render(request, 'AlphaHealthApp/patient_login.html')

def DoctorView(request):
    return render(request, 'AlphaHealthApp/doctor_page.html')

def NewPatient(request):
    return render(request, 'AlphaHealthApp/patient_register.html')


def CreatePatient(request):
    usrName = request.POST['userName']
    userPswd = request.POST['userPswd']
    new_fname = request.POST['newFName']
    new_lname = request.POST['newLName']
    new_age = request.POST['newAge']    

    newUser = Users(userName = usrName, password = userPswd) 
    newUser.save() 
    
    newUserInfo = UsersInfo(userName = usrName, firstName = new_fname, lastName = new_lname, age =new_age) 
    newUserInfo.save()    

    return JsonResponse({'status' : 'successful'})


def PatientUpdate(request):
    usrName = request.POST['userName']
    new_fname = request.POST['newFName']
    new_lname = request.POST['newLName']
    new_age = request.POST['newAge']

    updateUser = UsersInfo.objects.get(userName=usrName)
    updateUser.firstName = new_fname
    updateUser.lastName = new_lname
    updateUser.age = new_age

    updateUser.save()

    
    return JsonResponse({'uFName':updateUser.firstName,'uLName':updateUser.lastName,'uAge':updateUser.age})



def PatientLoginPage(request):
    patientID = request.POST['PatientUserID']
    patientPswd = request.POST['PatientPassword']

    UsersList = Users.objects.all()
    existingUsers = []
    for patient in UsersList:
        existingUsers.append({patient.userName:patient.password})

    try:
        usrInfo = UsersInfo.objects.get(userName=patientID)
    except:
        return HttpResponse("User Doesnt exist. Please head back and register.Or contact Admin for assistance.")

    context = {'patientID' : patientID, 'isAuthd' : True, 'firstname' : usrInfo.firstName,
            'lastname' : usrInfo.lastName, 'age' : usrInfo.age}
    return render(request, 'AlphaHealthApp/patient_page.html', context)


def CreateAppointment(request):
    usrName = request.POST['userName']
    apptDate = request.POST['apptDate']
    apptTime = request.POST['apptTime']
    apptReason = request.POST['apptReason']

    newAppt = UsersAppointments(userName = usrName, date = apptDate, time = apptTime, reason = apptReason) 
    newAppt.save()   

    return JsonResponse({'status':'success', 'ApptDate' : apptDate, 'ApptTime':apptTime, 'ApptReason':apptReason})

def ViewAppointment(request):    
    usrName = request.POST['usrName']
    usrAppts = UsersAppointments.objects.filter(userName=usrName)
    usrApptList = []
    for appt in usrAppts:
        usrApptList.append([appt.date, appt.time, appt.reason])

    return JsonResponse({'userAppts' : usrApptList})


def ViewAllAppointment(request):    
    usrAppts = UsersAppointments.objects.all()
    usrApptList = []
    for appt in usrAppts:
        usrApptList.append([appt.userName, appt.date, appt.time, appt.reason])

    return JsonResponse({'userAppts' : usrApptList})
