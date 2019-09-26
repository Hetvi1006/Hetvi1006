from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from . models import Profile

class UserRegisterForm(UserCreationForm):
    gen = (('Male','Male'), ('Female','Female'))
    name = forms.CharField()
    email = forms.EmailField()
    gender = forms.ChoiceField(widget=forms.Select, choices=gen)
    contact_no = forms.CharField()


    class Meta:
        model = User
        fields = ['username', 'name','email', 'contact_no', 'gender', 'password1', 'password2']

from users.models import Feedback
class FeedbackForm(UserCreationForm):
    name = forms.CharField()
    email = forms.EmailField()
    feedback = forms.CharField()


    class Meta:
        model = Feedback
        fields='__all__'
        

# class UserUpdateForm(forms.ModelForm):
#     gen = (('Male','Male'), ('Female','Female'))
#     name = forms.CharField()
#     email = forms.EmailField()
#     gender = forms.ChoiceField(widget=forms.Select, choices=gen)
#     con_no = forms.CharField()


#     class Meta:
#         model = User
#         fields = ['username', 'name', 'email', 'con_no', 'gender',]

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image',]
from django import forms   
from users.models import product  
class ProductForm(forms.ModelForm):  
    class Meta:  
        model = product  
        fields = "__all__"
from users.models import subcat  
class SubcatForm(forms.ModelForm):  
    class Meta:  
        model = subcat  
        fields = ('product','cimage','cname','cprice','cdes','disc','dprice',)
from django import forms
from users.models import Profile

class profilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ( 'user','image', )