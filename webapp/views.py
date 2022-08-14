from importlib.metadata import requires
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cyberweb.settings import storage 

from webapp.models import Application, Career, Contact, JobApplication, Product, Services, SubServices, TeamMember

# Create your views here.


def home(request):

    return render(request, "webapp/home.html", {})


def about(request):
    return render(request, "webapp/about.html", {})


def applyjobs(request):
    careers=Career.objects.filter(status=True)

    if request.method == 'POST' and request.FILES["cv_file"]:
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        email = request.POST["email"]
        address = request.POST["address"]
        phonenumber = request.POST["phonenumber"]
        education_status = request.POST["ed_status"]
        job_type = request.POST["job_type"]
        position = request.POST["position"]
        description = request.POST["description"]
        cv_pdf = request.FILES["cv_file"]
        nm=cv_pdf.name.strip()
        s=storage.child(nm).put(cv_pdf)
        url=storage.child(cv_pdf.name).get_url(s["downloadTokens"]);

        JobApplication.objects.create(
            firstname=firstname.strip(), lastname=lastname.strip(), email=email.strip(),
             address=address.strip(), phonenumber=phonenumber.strip(),
             position=position,
                education_status=education_status.strip(),job_type=job_type.strip(),
                description=description.strip(),
                cv_link=url
             )

        messages.add_message(request, messages.INFO,
                             'your application has been successfully uploaded.')
                        

    return render(request, "webapp/applyjob.html", {"careers":careers})


def career(request):
    careers = Career.objects.all()
    form = {"careers": careers}
    return render(request, "webapp/career.html", form)

@login_required(login_url="/login")
def application(request):
    if request.method == 'POST' and request.FILES["application_file"]:
        title = request.POST["title"]
        subject = request.POST["subject"]
        application_file = request.FILES["application_file"]
        nm=application_file.name.strip()
        s=storage.child(nm).put(application_file)
        url=storage.child(application_file.name).get_url(s["downloadTokens"]);

        Application.objects.create(title=title.strip(),user=request.user,subject=subject.strip(),application_link=url)



    return render(request, "webapp/application.html", {})

def loginTeamMember(request):
    if request.user.is_authenticated:
        return redirect("main_web:home")
    if request.method=="POST":
            username=request.POST["username"]
            password=request.POST["password"]
            user = authenticate(username=username.strip(), password=password.strip())
            if user is not None:
                login(request,user);
                return redirect("main_web:application")
            else:
                print('either wrong username or password.')
                messages.add_message(request, messages.INFO,
                             'either wrong username or password.'
                             )
    return render(request, "webapp/login.html", {})


def team(request):
    team_members = TeamMember.objects.all()
    form = {"team_members": team_members}
    return render(request, "webapp/team.html", form)


def products(request):
    products = Product.objects.all()
    form = {"products": products}
    return render(request, "webapp/products.html", form)


def contactus(request):

    if request.method == 'POST':
        fullname=request.POST["fullname"]
        phonenumber=request.POST["phonenumber"]
        email=request.POST["email"]
        description=request.POST["description"]
        if len(fullname)==0 or len(phonenumber)==0 or len(email)==0 or len(description)==0:
             messages.add_message(request, messages.INFO,
                             'please fill the form correctly.')
        else:
            Contact.objects.create(fullname=fullname,phonenumber=phonenumber,email=email,description=description)
            messages.add_message(request, messages.INFO,
                             'your contact form has been submitted.')
             

                  
    return render(request, "webapp/contactus.html", {})


def blogs(request):
    return render(request, "webapp/blogs.html", {})


def blog_indi(request, blog_id):
    return render(request, "webapp/blog_indi.html", {})


def what_we_do(request):
    services = Services.objects.all()
    form = {"services": services}
    return render(request, "webapp/what_we_do.html", form)


def what_we_do_specific(request, typedev, typedevid):
    service = Services.objects.get(id=typedevid)
    subservices = SubServices.objects.filter(service=typedevid)
    form = {"service": service, "sub_services": subservices}
    return render(request, "webapp/individual_service.html", form)

def logoutUser(request):
    print("logout user")
    logout(request)
    return redirect("main_web:home")