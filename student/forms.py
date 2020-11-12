from .models import Student
from users.models import Users
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm



# class StudentForm(UserCreationForm):
#     username = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=200)

#     class Meta:
#         model = Student
#         fields = ('username', 'email', 'password1', 'password2', )


class StudentForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=150)
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=50)
    confirm_password = forms.CharField(label='confirm Password', widget=forms.PasswordInput, max_length=50)
    # batch = forms.IntegerField(label="batch year")
    # uid = forms.CharField(label="Student ID", max_length=8)

    class Meta:
        model = Student
        fields = ('first_name','username', 'last_name', 'email', 'password')

    def clean(self):
        cleaned_data = super(StudentForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords Do Not Match', code=400)

    def save(self):
        created_user = Users(first_name=self.cleaned_data.get('first_name'),last_name=self.cleaned_data.get('last_name'),email=self.cleaned_data.get('email'), username=self.cleaned_data.get('username'))
        created_user.set_password(self.cleaned_data.get('password'))
        created_user.save()
        # created_student = Student(u=created_user, username=self.cleaned_data.get('username'))
                                  
      
        # # created_student = Student(user=created_user,uid=created_user.username,arn=1700006,batch=2017)
        # created_student.save()
        # return created_student

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['user']