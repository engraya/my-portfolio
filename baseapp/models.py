from django.db import models

# Create your models here.


PROJECT_STATUS = (
        ("Completed", "Completed"),
        ("Not Completed", "Not Completed")
    )

class About(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    profession = models.CharField(max_length= 200, null=True, blank=True)
    qualification = models.CharField(max_length= 200, null=True, blank=True)
    github = models.CharField(max_length= 200, null=True, blank=True)
    freelance_status = models.CharField(max_length= 200, null=True, blank=True)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    phone_Number = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    nationality = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    about_description = models.TextField()

    def __str__(self):
        return self.full_name



class Education(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    starting_date = models.CharField(max_length=200, null=True, blank=True)
    ending_date = models.CharField(max_length=200, null=True, blank=True)
    institution = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class EducationCertificate(models.Model):
    certificate = models.ForeignKey(Education, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='memberships', null=True, blank=True)

    def __str__(self):
        return self.title




class Certification(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='certificates', null=True, blank=True)
    year_acquired = models.DateField(null=True, blank=True)
    provider = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.title

class Contact(models.Model):
    location = models.CharField(max_length=200, null=True, blank=True)
    phone1 = models.CharField(max_length=200, null=True, blank=True)
    phone2 = models.CharField(max_length=200, null=True, blank=True)
    email1 = models.EmailField(max_length=200, null=True, blank=True)
    email2 = models.EmailField(max_length=200, null=True, blank=True)

class Social(models.Model):
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    showcase = models.URLField(null=True, blank=True)
    homeAdress = models.CharField(max_length=200, null=True, blank=True)
    phone1 = models.CharField(max_length=200, null=True, blank=True)
    phone2 = models.CharField(max_length=200, null=True, blank=True)
    primaryEmail = models.EmailField(max_length=200, null=True, blank=True)
    AlternativeEmail = models.EmailField(max_length=200, null=True, blank=True)
    whatsapp = models.CharField(max_length=200, null=True, blank=True)


class Portfolio(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    portfolio_description = models.TextField()
    cover_image = models.ImageField(upload_to='portfolio_cover', null=True, blank=True)
    tech_stack = models.CharField(max_length=200, null=True, blank=True)
    deployment = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True, choices=PROJECT_STATUS)
    portfolio_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Caption(models.Model):
    caption_shots = models.ForeignKey(Portfolio, on_delete=models.CASCADE ,null=True, blank=True)
    image = models.ImageField(upload_to='captions', null=True, blank=True)



class Refree(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    work_place = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class ProfessionalExperience(models.Model):
    job_title = models.CharField(max_length=200, null=True, blank=True)
    starting_date = models.DateField()
    ending_date = models.CharField(max_length=100, null=True, blank=True)
    work_place = models.CharField(max_length=200, null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
   

    def __str__(self):
        return self.work_place

class JobDescription(models.Model):
    experience = models.ForeignKey(ProfessionalExperience, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    
    def __str__(self):
        return self.description


class SoftSkills(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class TechSkills(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title



class Softwares(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class HardSkills(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)


class TechStack(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    subtitle = models.TextField()

    def __str__(self):
        return self.title


class Membership(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    issuing_body = models.CharField(max_length=200, null=True, blank=True)
    issuing_year = models.CharField(max_length=200, null=True, blank=True)
    membership_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title



class MembershipCertificate(models.Model):
    certificate = models.ForeignKey(Membership, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    issuing_body = models.CharField(max_length=200, null=True, blank=True)
    issuing_year = models.CharField(max_length=200, null=True, blank=True)
    membership_id = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='memberships', null=True, blank=True)

    def __str__(self):
        return self.issuing_body





    