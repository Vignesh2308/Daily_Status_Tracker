from django.shortcuts import render
from Tracker.forms import Info
from Tracker.forms import UserForm, UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        emp_name = request.POST.get('emp_name')
        training_name = request.POST.get('training_name')
        source = request.POST.get('source')
        source_other = request.POST.get('source_other')
        cur_date = request.POST.get('cur_date')
        completion_date = request.POST.get('completion_date')
        tot_hours = request.POST.get('tot_hours')
        hours_spent = request.POST.get('hours_spent')
        training_type = request.POST.get('training_type')
        skill = request.POST.get('skill')
        certification = request.POST.get('certification')
        certified = request.POST.get('certified')
        lex_link = request.POST.get('lex_link')
        task = request.POST.get('task')
        description = request.POST.get('description')
        ttl_hours = request.POST.get('ttl_hours')
        assessment = request.POST.get('assessment')
        assess_status = request.POST.get('assess_status')
        print(emp_id, emp_name, training_name, source, source_other, cur_date, completion_date, tot_hours, hours_spent, training_type, skill, certification, certified,
              lex_link, task, description, ttl_hours, assessment, assess_status)
        status = Info(emp_id, emp_name, training_name, source, source_other, cur_date, completion_date, tot_hours, hours_spent, training_type, skill, certification, certified,
              lex_link, task, description, ttl_hours, assessment, assess_status)
        status.save()
        return render(request,'Tracker/Result.html')
    return render(request, 'Tracker/Home.html')
#
#
# def result(request):
#     return render(request, 'Tracker/Result.html')

def index(request):
    return render(request, 'Tracker/index.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save()
            profile.user = user
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'Tracker/register.html', context)





def user_login(request):
    if request.method == 'POST':
        # getting username and password from form(name)
        username = request.POST.get('username')
        password = request.POST.get('password')

        # username and password checking
        user = authenticate(username=username, password=password)

        # checking authentication is success
        if user:
            # checking user is active or not
            if user.is_active:
                # in built function to login ->send req and authenticated checking
                login(request, user)
                return HttpResponseRedirect(reverse('Tracker:home'))
            else:
                return HttpResponse("Account is not active")
        else:
            print("Invalid Username and Password")
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse("Invalid Username and Password")
    else:
        return render(request, 'Tracker/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))