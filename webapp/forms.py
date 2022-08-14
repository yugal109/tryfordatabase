from django import forms
from .models import Career, Contact, JobApplication, Product,Services,SubServices

class CareerForm(forms.ModelForm):
  vacancy_title = forms.CharField( widget=forms.Textarea(attrs={'rows': 3, 'cols': 100}))
  description = forms.CharField( widget=forms.Textarea(attrs={'rows': 10, 'cols': 100}))
  class Meta:
    model = Career 
    fields = ('__all__')

class ProductForm(forms.ModelForm):
  description = forms.CharField( widget=forms.Textarea(attrs={'rows': 10, 'cols': 100}))
  class Meta:
    model = Product 
    fields = ('__all__')

class ContactForm(forms.ModelForm):
  description = forms.CharField( widget=forms.Textarea(attrs={'rows': 10, 'cols': 100}))
  class Meta:
    model = Contact 
    fields = ('__all__')

class JobApplyForm(forms.ModelForm):
  description = forms.CharField( widget=forms.Textarea(attrs={'rows': 10, 'cols': 100}))
  class Meta:
    model = JobApplication 
    fields = ('__all__')




class ServiceForm(forms.ModelForm):
  description = forms.CharField( widget=forms.Textarea(attrs={'rows': 10, 'cols': 100}))
  class Meta:
    model = Services 
    fields = ('__all__')

class SubServiceForm(forms.ModelForm):
  description = forms.CharField( widget=forms.Textarea(attrs={'rows': 10, 'cols': 100}))
  class Meta:
    model = SubServices 
    fields = ('__all__')




