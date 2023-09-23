from django.shortcuts import redirect, render
from django.views import generic as views
from django.contrib.auth import views as auth_views
from virtual_classroom.authentication.forms import UserRegistrationForm
from django.urls import reverse_lazy
from virtual_classroom.authentication.models import CustomUserProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse

def index(request):
    return render(request, "auth/index.html")

class SignUpView(views.CreateView):
    template_name = 'auth/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()

        custom_user_profile = CustomUserProfile.objects.create(user=user)
        custom_user_profile.email = form.cleaned_data.get('email')
        custom_user_profile.save()

        messages.success(
            self.request, "User: " + user.username + " successfully created an account!"
        )

        return super().form_valid(form)

class SignInView(auth_views.LoginView):
    template_name = "auth/login.html"

    def form_invalid(self, form):
        messages.info(self.request, "Incorrect password or username!")
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse("index"))  
        else:
            messages.info(request, "Incorrect password or username!")
            return render(request, self.template_name)
        

class SignOutView(auth_views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)