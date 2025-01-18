from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from .forms import *
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Case, When, IntegerField


# Create your views here.
@login_required
def profil(request):
    if request.method == 'POST':
        form = Userprofilform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, "Malumotlar Saqlandi.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
        else:
            messages.info(request, "Yaroqsiz maʼlumot!.")
    else:
        form = Userprofilform(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'main/profil.html',context)


@login_required
def index(request):
    if request.method == 'POST':
        form = Employeeform(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.author = request.user
            employee.save()
            messages.info(request, "Istemolchi qo'shildi.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
        else:
            messages.info(request, "Yaroqsiz maʼlumot!.")
    else:
        form = Employeeform()
    
    employees = Employee.objects.filter(author=request.user).annotate(
        summa=Sum(
            Case(
                When(qarz__status=True, then='qarz__summa'),
                default=0,
                output_field=IntegerField()
            )
        )
    ).order_by('-id')
    
    jami_sum = employees.aggregate(Sum('summa'))['summa__sum']
    
    context = {
        'jami_sum': jami_sum,
        'form': form,
        'employee': employees,
    }
    return render(request, 'main/index.html', context)


@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST' and employee.author == request.user:
        
        full_name = request.POST.get('full_name')
        tel = request.POST.get('tel')
        pazivnoy = request.POST.get('pazivnoy')
        
        employee.full_name = full_name
        employee.tel = tel
        employee.pazivnoy = pazivnoy
        employee.save()
        
        messages.info(request, "Saqlandi")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
    else:
        return redirect(reverse('login'))


@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if employee.author == request.user:
        employee.delete()
        messages.info(request, "Istemolchi o'chirildi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
    else:
        return redirect(reverse('login'))
    
    
@login_required
def debt(request,pk):
    employee = get_object_or_404(Employee, id=pk)
    if request.method == 'POST':
        form = Qarzform(request.POST)
        if form.is_valid():
            qarz = form.save(commit=False)
            qarz.employee = employee
            qarz.save()
            messages.info(request, "Qarz qo'shildi.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
        else:
            messages.success(request, "Yaroqsiz maʼlumot!.")
    else:
        form = Qarzform()
    
    context = {
        'form': form,
        'qarz': Qarz.objects.filter(employee=employee,status=True)[::-1],
    }
    return render(request, 'main/debt.html', context)


@login_required
def debt_edit(request, pk):
    qarz = get_object_or_404(Qarz, pk=pk)
    if request.method == 'POST' and qarz.employee.author == request.user:
        
        summa = request.POST.get('summa')
        qarz.summa = summa
        qarz.save()
        
        messages.info(request, "Saqlandi")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
    else:
        return redirect(reverse('login'))


@login_required
def debt_delete(request, pk):
    qarz = get_object_or_404(Qarz, pk=pk)
    if qarz.employee.author == request.user:
        qarz.status = False
        qarz.save()
        messages.info(request, "Qarz o'chirildi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
    else:
        return redirect(reverse('login'))
    
    