from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserCreateForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
<<<<<<< HEAD

=======
from project.models import Project

def list_user_projects(request):
    projects = Project.objects.all().filter(user = 1)
    for project in projects:
        print(project.title)
        print("projectssss")
    return render(request, 'accounts/projects.html', {"projects": projects})
>>>>>>> d36c4b517eab3c21da3097626b93ef170b2a126d
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

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
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
<<<<<<< HEAD
        return HttpResponse('Activation link is invalid!')
=======
        return HttpResponse('Activation link is invalid!')
>>>>>>> d36c4b517eab3c21da3097626b93ef170b2a126d
