import imp
from django import forms
from matplotlib import widgets
from matplotlib.widgets import Widget
from .models import money,UserProfile
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm,UsernameField,UserCreationForm

class moneyForm(forms.ModelForm):
    
    class Meta:
        model = money
        fields = ('Date',"money_type",'amount','Category',)
        labels = {'money_type': 'Type',
                  'amount': 'Amount',
                  'Category': 'Category',
                  'Date':'Expence Date'}
        widgets = {
            'Date': forms.DateInput(attrs={'type':'date','class': 'form-control form-control-user','placeholder':'Password'}),
            'money_type': forms.Select(attrs={'class': 'form-control form-control-user','placeholder':'Password'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control form-control-user','placeholder':'Amount'}),
            'Category': forms.Select(attrs={'class': 'form-control form-control-user','placeholder':'Password'}),
        }

class loginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'form-control form-control-user',
        # 'class': 'form-control',
        'placeholder':'Enter Username...'

    }))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id':'exampleInputEmail',
        'placeholder':'Enter Password'

    }))

class signUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user',
              # 'placeholder':'Password'
              }))
    password2 = forms.CharField(label='Confirm Password(Again)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 
                                # 'placeholder':'Re-Enter Password'
                                }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'email': 'Email ID'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control form-control-user', 
                    # 'placeholder':'Username'
                    }),
                   'first_name': forms.TextInput(attrs={'class': 'form-control form-control-user',
                   # 'placeholder':'First Name'
                   }),
                   'last_name': forms.TextInput(attrs={'class': 'form-control form-control-user', 
                    # 'placeholder':'Last Name'
                    }),
                   'email': forms.EmailInput(attrs={'class': 'form-control form-control-user required', 
                    # 'placeholder':'Email - Address'
                    'required':True
                    })}

class signUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user',
              'placeholder':'Password'
              }))
    password2 = forms.CharField(label='Confirm Password(Again)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 
                                'placeholder':'Re-Enter Password'
                                }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'email': 'Email ID'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control form-control-user', 
                    'placeholder':'Username'
                    }),
                   'first_name': forms.TextInput(attrs={'class': 'form-control form-control-user',
                   'placeholder':'First Name'
                   }),
                   'last_name': forms.TextInput(attrs={'class': 'form-control form-control-user', 
                    'placeholder':'Last Name'
                    }),
                   'email': forms.EmailInput(attrs={'class': 'form-control form-control-user required', 
                    'placeholder':'Email - Address',
                    'required':True
                    })}
# Receord Search

CHART_CHOICES=(
    ('#1','Bar Chart'),
    ('#2','Pie Chart'),
    ('#3','Line Chart'),
)
INCOME_CHOICES=(
    ('Income','Income'),
    ('Expense','Expense'),
)

class ExpenceSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'form-control form-control-user'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'form-control form-control-user'}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
    income_type = forms.ChoiceField(choices=INCOME_CHOICES)
    chart_type.widget.attrs.update({'class': 'form-control form-control-user'})
    income_type.widget.attrs.update({'class': 'form-control form-control-user'})


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

class addMulForm(forms.Form):
    type = forms.CharField(max_length=100, required=False)
    date = forms.DateTimeField(required=False)
    amount = forms.IntegerField()
