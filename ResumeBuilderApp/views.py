from django.shortcuts import render,redirect
from ResumeBuilderApp.models import *
# Create your views here.

def home(request):
    resumeData = ResumeModel.objects.all()
    return render(request,'home.html',{'resumes':resumeData})

def add_resume(request):
    if request.method == 'POST':
        resume =ResumeModel(
            Full_Name = request.POST.get('Full_Name'),
            Profile_Picture= request.FILES.get('Profile_Picture'),
            Email= request.POST.get('Email'),
            Phone= request.POST.get('Phone'),
            Address= request.POST.get('Address'),
            Summary= request.POST.get('Summary'),
            Degree= request.POST.get('Degree'),
            Institute_Name= request.POST.get('Institute_Name'),
            Year_of_Graduation= request.POST.get('Year_of_Graduation'),
            Company_Name= request.POST.get('Company_Name'),
            Position= request.POST.get('Position'),
            Years_of_Experience= request.POST.get('Years_of_Experience'),
            Skills= request.POST.get('Skills'),
            Hobbies= request.POST.get('Hobbies'),
            Achievements= request.POST.get('Achievements'),
        )
        resume.save()
        return redirect('home')
    return render(request,'add_resume.html')

def edit_resume(request,id):
    resumeData= ResumeModel.objects.get(id=id)
    if request.method == 'POST':
        
        Full_Name = request.POST.get('Full_Name')
        Email= request.POST.get('Email')
        Phone= request.POST.get('Phone')
        Address= request.POST.get('Address')
        Summary= request.POST.get('Summary')
        Degree= request.POST.get('Degree')
        Institute_Name= request.POST.get('Institute_Name')
        Year_of_Graduation= request.POST.get('Year_of_Graduation')
        Company_Name= request.POST.get('Company_Name')
        Position= request.POST.get('Position')
        Years_of_Experience= request.POST.get('Years_of_Experience')
        Skills= request.POST.get('Skills')
        Hobbies= request.POST.get('Hobbies')
        Achievements= request.POST.get('Achievements')
        
        picture = request.FILES.get('Profile_Picture')
        if picture is None:
            resumeData.Profile_Picture = picture
        resumeData.save()       
        return redirect('home')
    return render(request,'edit_resume.html',{'resume':resumeData})

def view_resume(request,id):
    resumeData = ResumeModel.objects.get(id=id)
    return render(request,'view_resume.html',{'resume':resumeData})

def delete_resume(request,id):
    resumeData = ResumeModel.objects.get(id=id).delete()
    return redirect('home')