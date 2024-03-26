from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from django.views import View

from .forms import CustomUserCreationForm, UserUpdateForm


class NewUserRegister(View):
    template_name: str = "users/register.html"

    def get(self, request) -> render:
        form = CustomUserCreationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account's been created for {username}!")
            return redirect("login")
        return render(request, self.template_name, {"form": form})


class LogoutUser(View):
    def get(self, request) -> redirect:
        auth_logout(request)

        message: str = "You have been successfully logged out"
        messages.success(request, message)

        return redirect("home")


class HomePage(View):
    template_name = "users/landing_page.html"

    def get(self, request) -> redirect:
        return render(request, self.template_name)


class UserProfile(View):
    template_name: str = "users/profile.html"

    def get(self, request) -> render:
        user_form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {"user_form": user_form})

    def post(self, request):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Your profile has been updated")
            return redirect("profile")
        messages.error(request, "There was an error updating your profile")
        return redirect("profile")


class Dashboard(View):
    template_name = "users/dashboard.html"

    def get(self, request) -> redirect:
        return render(request, self.template_name)
