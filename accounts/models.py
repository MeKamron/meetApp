from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from blog.models import Category, SubCategory

class Region(models.Model):
    name = models.CharField(max_length=64, verbose_name="Viloyat nomi")

    def __str__(self) -> str:
        return self.name



class Status(models.Model):
    title = models.CharField(max_length=64)
    keyword = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.title

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phone, username, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not phone:
            raise ValueError('The given email must be set')
        user = self.model(phone=phone, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, username, password, **extra_fields)

    def create_superuser(self, phone, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, username, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(_('Username'), max_length=200, unique=True, blank=True)
    phone = models.CharField(_('Telefon raqam'), max_length=13 ,unique=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/photos/', blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="users")
    category = models.ManyToManyField(Category, related_name="users")
    sub_category = models.ManyToManyField(SubCategory, related_name="users")
    bio = models.CharField(max_length=300)