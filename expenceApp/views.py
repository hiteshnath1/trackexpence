from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views.generic import ListView,DetailView
from matplotlib.style import context
from .models import moneyType, money,expType,UserProfile
from django.db.models import Avg, Max, Min, Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
import datetime
from .forms import ExpenceSearchForm,moneyForm,UserProfileForm,addMulForm
from django.db.models.functions import ExtractMonth


# Create your views here.
@login_required
def moneyView(request):
    if request.user.is_authenticated:
        incmoney = money.objects.filter(user=request.user).order_by('-amount')
        money_type = moneyType.objects.all()
        choice = request.GET.get('choice')
        request.session['choice'] = choice
        lab = request.session['choice']
        today = datetime.datetime.now()
        
        
        print(today.strftime('%B'))
        if choice:
            incmoney = money.objects.filter(user=request.user).filter(money_type__id = choice).order_by('-amount')
            qs = money.objects.filter(user=request.user).filter(money_type__id = choice).values('Category__name').order_by('Category').annotate(total_price=Sum('amount'))
        else:
            incmoney = money.objects.filter(user=request.user).order_by('-amount')
            qs = money.objects.filter(user=request.user).values('Category__name').order_by('Category').annotate(total_price=Sum('amount'))
    context={
        'money_type':money_type,
        'incmoney':incmoney,
        'qs':qs,
        'lab':lab,
    }
    return render(request,'expenceApp/dashboard.html',context)
@login_required
def charts(request):
    form = ExpenceSearchForm(request.POST or None)
    chart = 'doughnut'
    qs = money.objects.filter(user=request.user).filter(money_type__name = 'Income').values('Category__name').order_by('Category').annotate(total_price=Sum('amount'))
    start = money.objects.all()[:1]
        
    print(start)
    if request.method ==  'POST':
        
        income_type = request.POST.get('income_type')
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        result_by = request.POST.get('result_by')

        print(date_from,date_to,chart_type)
        qs = money.objects.filter(user=request.user).filter(Date__lte = date_to, Date__gte = date_from).filter(money_type__name = income_type).values('Category__name').order_by('Category').annotate(total_price=Sum('amount'))            
        if chart_type == '#1':
            chart = 'bar'
        elif chart_type == '#2':
            chart = 'pie'
        elif chart_type == '#3':
            chart = 'line'
        else:
            no_data = 'No data in select date range'

    
    context={
        'form':form,
        'qs':qs,
        'chart':chart,
    }
    return render(request,'expenceApp/chart.html',context)

@login_required
def addmoney(request):
    if request.user.is_authenticated:
        total_income = money.objects.filter(user=request.user).filter(money_type__name= 'Income').aggregate(Sum('amount')).get('amount__sum')
        total_expense = money.objects.filter(user=request.user).filter(money_type__name= 'Expense').aggregate(Sum('amount')).get('amount__sum')
        if total_expense is None:
            total_expense='0'
        if total_income is None:
            total_income = '0'
        
        # amount = int(total_income) - int(total_expense)
        if request.method == "POST":
            form = moneyForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.user = request.user
                user.save()

                return redirect('/add')
        else:
            form = moneyForm()
            
        context = {
            'form':form,
            'total_income':total_income,
            'total_expense':total_expense,
        }
        return render(request,'expenceApp/addRecord.html',context)

@login_required
def my_profile_view(request):
    profile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if form.is_valid():
        form.save()
        confirm = True
        return redirect('/')
    context = {
        'profile': profile,
        'form':form,
        'confirm':confirm,
    }
    return render(request,'expenceApp/UserProfile.html',context)

def datatable(request):
    return render(request,'expenceApp/dashboard.html')


def multiadd(request):
    choice = request.session['choice']
    if request.user.is_authenticated:
        total_income = money.objects.filter(user=request.user).filter(money_type__name= 'Income').aggregate(Sum('amount')).get('amount__sum')
        total_expense = money.objects.filter(user=request.user).filter(money_type__name= 'Expense').aggregate(Sum('amount')).get('amount__sum')
        if total_expense is None:
            total_expense='0'
        if total_income is None:
            total_income = '0'
        incmoney = expType.objects.filter(c_Type=choice)
        money_type = moneyType.objects.all()
        choice = request.GET.get('choice')
        request.session['choice'] = choice
        if choice:
            incmoney = expType.objects.filter(c_Type=choice)
        else:
            incmoney = expType.objects.filter(c_Type=2)

        

    context={
        'money_type':money_type,
        'incmoney':incmoney,
        'total_income':total_income,
        'total_expense':total_expense,
    }
    return render(request,'expenceApp/addmultiple-1.html',context)

def multiaddsave(request,pk):
    data = expType.objects.get(pk=pk)
    money_type = moneyType.objects.get(id=request.session['choice'])
    date = request.POST['date']
    value = request.POST['amount']
    print(date)
    if date == "":
        date =  datetime.datetime.now()
    print(data)
    print(date)
    print(value)
    moneyobj = money.objects.create(user=request.user,money_type=money_type,amount=value,Date=date,Category=data)
    return redirect('/addmul/?choice='+request.session['choice'])


def reportView(request):
    start = money.objects.first()
    print(start.date)
    pass