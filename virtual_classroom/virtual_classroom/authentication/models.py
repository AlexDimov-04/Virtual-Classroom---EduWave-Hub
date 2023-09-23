from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

class CustomUserProfile(models.Model):
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    email = models.EmailField(null=True, blank=True)

    birth_date = models.DateField(null=True, blank=True)

    phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        null=True,
        blank=True,
        help_text="Contact Phone Number",
    )

    profile_image = models.ImageField(
        upload_to="profile_images/", null=True, blank=True
    )

    def __str__(self):
        return self.email
