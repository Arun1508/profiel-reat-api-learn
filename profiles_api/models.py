from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """manager for user profiles """

    def create_user(self, email, name, password=None):
        """Create a new user profile """
        if not email:
            raise ValueError('User must have email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        print("User created....!")
        print('user ',user)
        return user

    def create_superuser(self, email, name, password):
        """Create new super user """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractUser, PermissionsMixin):
    """db model for user system"""

    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    address = models.TextField(max_length=500)
    pincode = models.IntegerField(default=0)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrive full name of user"""
        return self.name

    def get_short_name(self):
        """return short name of the user """
        return self.name

    def __str__(self):
        """return user """
        return self.email
