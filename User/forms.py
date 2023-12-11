from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)
    first_name = forms.CharField(label='First Name',max_length=150) 
    last_name = forms.CharField(label='Last Name', max_length=150) 
    email = forms.EmailField(label='email')  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
    # _email = forms.EmailField(required = False)
    # _firstName = forms.EmailField()
    # _lastName = forms.EmailField()

    # class Meta:
    #     model = User
    #     fields = ['username', 'first_name','last_name','email', 'password1','password2']

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  

    def first_name_clean(self):  
        first_name = self.cleaned_data['first_name'].lower()  
        new = User.objects.filter(first_name = first_name)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return first_name 
    
    def last_name_clean(self):  
        last_name = self.cleaned_data['last_name'].lower()  
        new = User.objects.filter(last_name = last_name)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return last_name 

    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  

    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  

        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  

    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            email = self.cleaned_data['email'],  
            password=self.cleaned_data['password1'],  
            first_name= self.cleaned_data['first_name'], 
            last_name= self.cleaned_data['last_name'] 
        )  
        return user  
