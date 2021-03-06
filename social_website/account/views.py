from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
#from django.http import HttpResponse
from common.decorators import ajax_required
from django.contrib.auth.models import User
from actions.utils import create_action
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
#from .forms import LoginForm, RegistrationForm
from account.forms import LoginForm, UserForm, UserProfileInfoForm, ProfileEditForm, UserEditForm
from account.models import UserProfileInfo,Contact
from actions.models import Action

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/dashboard")
                else:
                    return HttpResponse("Account disabled")
            else:
                return HttpResponse("Invalid Account")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})


def register_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST or None)
        profile_form = UserProfileInfoForm(request.POST, request.FILES or None)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            
            user.save()
            print(user_form)
            profile = profile_form.save(commit=False)
            profile.user = user
            
            profile.save()
            create_action(user, " has created a new account")
            print(profile_form)
            return redirect("register_done")
                #registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    con = {
        'user_form' : user_form,
        'profile_form': profile_form,
        #'registered': registered
    }

    return render(request, 'account/register.html', con)

@login_required
def editForm(request):
    #edit = get_object_or_404(UserProfileInfo, id=id)
    if request.method == 'POST':
        edit_user = UserEditForm(data=request.POST or None, instance=request.user)
        edit_profile = ProfileEditForm(data=request.POST, files=request.FILES, instance=request.user.UserProfileInfo)
        if edit_user.is_valid() and edit_profile.is_valid():
            edit_form.save()
            edit_profile.save()
            return redirect('/')

    else:
        edit_user = UserEditForm()
        edit_profile = ProfileEditForm()
    context = {
        'edit_user' : edit_user,
        'edit_profile' : edit_profile
    }
    return render(request, 'account/editform.html', context)



@login_required
def dashboard(request):
    # Display all actions by default
    actions = Action.objects.all().exclude(user=request.user)
    following_ids = request.user.following.values_list('id', flat=True)
    if following_ids:
        # If user is following others, retrieve only their actions
        actions = actions.filter(user_id__in=following_ids).select_related('user', 'user__userprofileinfo').prefetch_related('target')
    actions = actions[:10]
    print(actions)
    return render(request, 'account/dashboard.html', {'section': 'dashboard',
                                                      'actions': actions})


def registerDone(request):
    return render(request, 'account/register_done.html')

@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html', {'section': 'people',
                                                      'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people',
                                                        'user': user})


@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user,
                                              user_to=user)
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(user_from=request.user,
                                       user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'ko'})
    return JsonResponse({'status':'ko'})