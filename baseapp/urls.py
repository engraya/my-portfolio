from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('resume', views.resume, name="resume"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('contact', views.contact, name="contact"),
    path('certifications', views.certifications, name="certifications"),
    path('portfolio-detail/<str:pk>/', views.portfolioDetail, name="portfolio_detail"),
    path('socials', views.socials, name="socials"),
    path('portfolio_detail', views.portfolioDetail, name="detail"),

]
