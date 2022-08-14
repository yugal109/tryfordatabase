from django.utils import timezone
import uuid
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.db import models


class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50,blank=False,null=False,unique=True)
    subject=models.CharField(max_length=10000,default="")
    created_at = models.DateTimeField(default=timezone.now)
    application_link=models.CharField(max_length=10000,blank=False,null=False,default="",editable=False)

    def __str__(self):
        return self.title
    
    def fullname(self):
        return self.user.first_name + " "+self.user.last_name

    def view_application(self):
        return format_html(f"<a href={self.application_link} target='_blank'>VIEW</a>")


    
    def application_tag(self):
        return format_html(f"<iframe src={self.application_link} width='100%' height='1500px'></iframe>")





class Career(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vacancy_title=models.CharField(max_length=50,blank=False,null=False,unique=True)
    total_positions=models.IntegerField(default=1)
    description=models.CharField(max_length=10000,default="")
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.vacancy_title




class Services(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=50,blank=False,null=False,unique=True)
    sub_title=models.CharField(max_length=50,blank=False,null=False,unique=True)
    description=models.CharField(max_length=10001,default="")
    created_at = models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to="images/",blank=False)
    
    def __str__(self):
        return self.title


    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


class SubServices(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service=models.ForeignKey(Services,on_delete=models.CASCADE)
    title=models.CharField(max_length=50,blank=False,null=False,unique=True)
    description=models.CharField(max_length=10000,default="")
    created_at = models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to="images/",blank=False)
    
    def __str__(self):
        return self.title

    # def get_absolute_ul(self):
        # return reverse("_detail", kwargs={"pk": self.pk})

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=50,blank=False,null=False,unique=True)
    link=models.CharField(max_length=50,blank=False,null=False)
    description=models.CharField(max_length=10000,default="")
    created_at = models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to="images/",blank=False)
    
    def __str__(self):
        return self.title


class TeamMember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    position=models.CharField(max_length=1000,default="")
    description=models.CharField(max_length=10000,default="")
    github_link=models.CharField(max_length=10000,blank=False,null=False)
    linkedin_link=models.CharField(max_length=10000,blank=False,null=False)
    created_at = models.DateTimeField(default=timezone.now)
    profile_image=models.ImageField(upload_to="images/",blank=False)
    cv_link=models.CharField(max_length=10000,blank=False,null=False,default="",editable=False)
    
    def __str__(self):
        if self.user.first_name=="" or self.user.last_name=="":
            return  self.user.username
        return self.user.first_name+" "+self.user.last_name
    
    def cv_view(self):
        return format_html(f"<a href={self.cv_link} target='_blank'>VIEW</a>")

    def cv_tag(self):
        return format_html(f"<iframe src={self.cv_link} width='100%' height='1500px'></iframe>")

    def cv(self):
        return format_html("<form method='post'><input required name='cv_file' type='file'/></form>")
    


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=50,blank=False,null=False)
    link=models.CharField(max_length=50,blank=False,null=False)
    description=models.CharField(max_length=10000,default="")
    created_at = models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to="images/",blank=False)
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname=models.CharField(max_length=250,blank=False,null=False)
    email=models.EmailField(max_length=350,blank=False,null=False)
    phonenumber=models.CharField(max_length=10,blank=False,null=False)
    created_at = models.DateTimeField(default=timezone.now)
    description=models.CharField(max_length=10000,default="")

    def __str__(self):
        return self.fullname
    
    def description_in_short(self):
        return self.description[:40]


EDUCATION_CHOICES = (
    ("SEE", "SEE"),
    ("+2","+2"),
    ("Bachelors","Bachelors"),
    ("Masters","Masters"),
    ("Phd","Phd"),
)

JOB_CHOICES = (
    ("Full-Time", "Full-Time"),
    ("Part-Time","Part-Time")
)

class JobApplication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname=models.CharField(max_length=250,blank=False,null=False)
    lastname=models.CharField(max_length=250,blank=False,null=False)
    address=models.CharField(max_length=250,blank=False,null=False)
    email=models.EmailField(max_length=350,blank=False,null=False)
    position=models.ForeignKey(Career,on_delete=models.CASCADE)
    phonenumber=models.CharField(max_length=10,blank=False,null=False)
    education_status=models.CharField(max_length=20,choices=EDUCATION_CHOICES,default="SEE")
    job_type=models.CharField(max_length=20,choices=JOB_CHOICES,default="Full-Time")
    created_at = models.DateTimeField(default=timezone.now)
    description=models.CharField(max_length=10000,default="")
    cv_link=models.CharField(max_length=10000,blank=False,null=False,default="",editable=False)

    def __str__(self):
        return self.firstname+" "+self.lastname
    
    def fullname(self):
        return self.firstname+" "+self.lastname
    
    def view_cv(self):
        return format_html(f"<a href={self.cv_link} target='_blank'>VIEW</a>")

    def photo_tag(self):
        return format_html(f"<iframe src={self.cv_link} width='100%' height='1500px'></iframe>")

    






