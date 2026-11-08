from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Quản trị viên"
        MEMBER = "MEMBER", "Hội viên"
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username
class MemberProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="member_profile",
    )
    phone = models.CharField(
        max_length=15,
        blank=True
    )
    join_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Hội viên: {self.user.username}"

# Create your models here.
