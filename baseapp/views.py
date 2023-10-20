from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Contact, Social, SoftSkills, Softwares, TechSkills, TechStack, Education, ProfessionalExperience, Membership, JobDescription, Certification, Portfolio, Refree
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    socials = Social.objects.all()
    context = { 'socials' : socials}
    return render(request, 'baseapp/home.html', context)


def about(request):
    abouts = About.objects.all()
    contacts = Contact.objects.all()
    skills = SoftSkills.objects.all()
    softwares = Softwares.objects.all()
    techskills = TechSkills.objects.all()
    techstacks = TechStack.objects.all()
    context = { 'abouts' : abouts, 'contacts' : contacts, 'skills' : skills, 'softwares' : softwares, 'techskills' : techskills, 'techstacks' : techstacks}
    return render(request, 'baseapp/about.html', context)


def resume(request):
    educations = Education.objects.all()
    memberships = Membership.objects.all()
    experiences = ProfessionalExperience.objects.all().order_by('-id')
    refrees = Refree.objects.all()
    context = { 'educations' : educations, 'memberships' : memberships, 'experiences' : experiences, 'refrees' : refrees}
    return render(request, 'baseapp/resume.html', context)


def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {'portfolios' : portfolios}
    return render(request, 'baseapp/portfolio.html', context)

def portfolio_Detail(request, pk):
    portfolio = Portfolio.objects.get(id=pk)
    context = {'portfolio' : portfolio}
    return render(request, 'baseapp/portfolio-details.html', context)


def portfolioDetail(request):
    return render(request, 'baseapp/portfolio-details.html')


def contact(request):
    socials = Social.objects.all()
    context = { 'socials' : socials}
    return render(request, 'baseapp/contact.html', context)


def certifications(request):
    certificates = Certification.objects.order_by('title')
    paginator = Paginator(certificates, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'certificates' : certificates, 'page_obj' : page_obj}
    return render(request, 'baseapp/certifications.html', context)

def certificateView(request, pk):
    certificate = Certification.objects.get(id=pk)
    context = {'certificate' : certificate}
    return render(request, 'baseapp/certificateView.html', context)



def education(request):
    return render(request, 'baseapp/education.html')

def socials(request):
    socials = Social.objects.all()
    context = { 'socials' : socials}
    return render(request, 'baseapp/socials.html', context)
