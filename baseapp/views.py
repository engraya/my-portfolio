from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Contact, Social, SoftSkills

# Create your views here.


def home(request):
    return render(request, 'baseapp/home.html')


def about(request):
    abouts = About.objects.all()
    contacts = Contact.objects.all()
    skills = SoftSkills.objects.all()
    context = { 'abouts' : abouts, 'contacts' : contacts, 'skills' : skills}
    return render(request, 'baseapp/about.html', context)


def resume(request):
    return render(request, 'baseapp/resume.html')


def portfolio(request):
    return render(request, 'baseapp/portfolio.html')


def portfolioDetail(request):
    return render(request, 'baseapp/portfolio-details.html')


def contact(request):
    return render(request, 'baseapp/contact.html')


def certifications(request):
    return render(request, 'baseapp/certifications.html')


def education(request):
    return render(request, 'baseapp/education.html')

def socials(request):
    socials = Social.objects.all()
    context = { 'socials' : socials}
    return render(request, 'baseapp/socials.html', context)
