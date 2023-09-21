from django.shortcuts import render
from django.views import generic as views
from virtual_classroom.authentication.forms import UserRegistrationForm
from django.urls import reverse_lazy
from virtual_classroom.authentication.models import CustomUserProfile
from django.contrib import messages


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
            self.request, "User: " + user + " successfully created an account!"
        )

        return super().form_valid(form)

        

   

def login(request):
    return render(request, 'auth/login.html')