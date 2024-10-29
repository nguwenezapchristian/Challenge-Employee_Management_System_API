from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from base.models import BaseModel


class User(AbstractUser, BaseModel):
    """Custom User model extending Django's AbstractUser with additional fields"""
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    role = models.CharField(
        max_length=20,
        choices=[('admin', 'Admin'), ('employee', 'Employee')],
        default='employee'
    )
    
    # Adding custom related names to avoid clashes with Django's default user model
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Unique related name for groups
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Unique related name for permissions
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )

    class Meta:
        db_table = 'users'


class PasswordReset(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)

    class Meta:
        db_table = 'password_resets'

