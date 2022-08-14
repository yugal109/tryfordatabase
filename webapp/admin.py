from django.contrib import admin
from webapp.forms import CareerForm, ContactForm, JobApplyForm, ProductForm, ServiceForm, SubServiceForm
from cyberweb.settings import storage
from webapp.models import Application, Career, Contact, JobApplication, Product, Services, SubServices, TeamMember

# Register your models here.


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    readonly_fields = ("cv", "cv_view", "cv_tag")

    def save_model(self, request, obj, form, change):
        if change == True:
            try:
                file = request.FILES["cv_file"]
                nm = file.name.strip()
                s = storage.child(nm).put(file)
                url = storage.child(file.name).get_url(s["downloadTokens"])
                obj.cv_link = url
                return super().save_model(request, obj, form, change)
            except:
                return super().save_model(request, obj, form, change)
        else:
            file = request.FILES["cv_file"]
            nm = file.name.strip()
            s = storage.child(nm).put(file)
            url = storage.child(file.name).get_url(s["downloadTokens"])
            obj.cv_link = url
            return super().save_model(request, obj, form, change)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    # form =JobApplyForm
    list_display = ("title", "fullname")
    readonly_fields = ("view_application", "application_tag")


# @admin.register(TeamMember)
# class TeamMemberAdmin(admin.ModelAdmin):
#     list_display=("position",)

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    form = CareerForm
    list_display = ("vacancy_title", "status")


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    form = JobApplyForm
    list_display = ("fullname", "email", "address", "job_type")
    readonly_fields = ("view_cv", "photo_tag")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
    list_display = ("fullname", "description_in_short", "phonenumber", "email")


@admin.register(Services)
class SerivicesAdmin(admin.ModelAdmin):
    form = ServiceForm
    list_display = ("title",)


@admin.register(SubServices)
class SubSerivicesAdmin(admin.ModelAdmin):
    form = SubServiceForm
    list_display = ("title",)
