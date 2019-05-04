from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
<<<<<<< HEAD
from .forms import UserCreateForm ,UserUpdateForm ,ProfileUpdateForm 
=======
from .forms import UserCreateForm
>>>>>>> c1e30cfb0050b6ff6eb3be8c26ba002274d586c9
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required




@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('/accounts/profile/')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)
=======
from project.models import Project

def list_user_projects(request):
    projects = Project.objects.all().filter(user = 1)
    for project in projects:
        print(project.title)
        print("projectssss")
    return render(request, 'accounts/projects.html', {"projects": projects})
# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic
# from .forms import  UserCreateForm
# from django.shortcuts import render

# class SignUp(generic.CreateView):
#     form_class = UserCreateForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


def profile(request):
 return render(request, 'profile.html')
>>>>>>> c1e30cfb0050b6ff6eb3be8c26ba002274d586c9

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
<<<<<<< HEAD
            mail_subject = 'Activate your account.'
=======
            mail_subject = 'Activate your blog account.'
>>>>>>> c1e30cfb0050b6ff6eb3be8c26ba002274d586c9
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = UserCreateForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')