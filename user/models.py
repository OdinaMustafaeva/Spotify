from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from playlist.models import TimestampModel
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    class UserType(models.TextChoices):
        ARTIST = "Artist"
        LISTENER = "listener"

    username = models.CharField(_("username"), max_length=150, unique=True, null=True, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    country = models.CharField(max_length=15, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    description = models.CharField(_("description"), max_length=300, null=True)
    usertype = models.CharField(max_length=50, choices=UserType.choices, default="listener")
    avatar = models.ImageField(null=True, upload_to="users/")

    objects = CustomUserManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    def __str__(self):
        return f"{self.email}"

    def full_name(self):
        return self.get_full_name()


class VerificationCode(models.Model):
    code = models.CharField(max_length=6)
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="verification_codes", null=True, blank=True
    )
    email = models.EmailField(unique=True, null=True)
    last_sent_time = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    expired_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.email

    @property
    def is_expire(self):
        return self.expired_at < self.last_sent_time + timedelta(seconds=30)

