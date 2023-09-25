from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserRegistrationForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "login__input"
            field.widget.attrs["id"] = field_name

            if field_name == "username":
                field.widget.attrs["placeholder"] = "Username"
            elif field_name == "email":
                field.widget.attrs["placeholder"] = "Email"
            elif field_name == "password1":
                field.widget.attrs["placeholder"] = "Password"
            elif field_name == "password2":
                field.widget.attrs["placeholder"] = "Confirm Password"

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')