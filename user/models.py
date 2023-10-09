from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db import models

# Create your models here.


# Custom User Manager
class CustomUserManager(BaseUserManager):

    # For creating Passenger and Employee Account
    def create_user(self, email, user_type, password=None, **extra_fields):
        if not email:
            raise ValueError('You must provide an email address.')
        email = self.normalize_email(email)
        user = self.model(email=email, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    # For creating Management Account
    def create_superuser(self, email, user_type, paswword=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if user_type != 'Management':
            raise ValueError('Superuser must be from Management')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=Ture')

        return self.create_user(email, user_type, paswword, **extra_fields)


# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    PASSENGER = 'Passenger'
    EMPLOYEE = 'Employee'
    MANAGEMENT = 'Management'
    MALE = 'Male'
    FEMALE = 'Female'
    OTHERS = 'Others'

    USER_TYPE_CHOICES = (
        (PASSENGER, 'Passenger'),
        (EMPLOYEE, 'Employee'),
        (MANAGEMENT, 'Management'),
    )

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    )

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=15, choices=GENDER_CHOICES, default=MALE)
    nationality = models.CharField(max_length=25)
    national_id = models.CharField(max_length=28, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    user_type = models.CharField(
        max_length=15, choices=USER_TYPE_CHOICES, default=PASSENGER)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'user_type', 'nationality', 'national_id']

    def __str__(self):
        return self.email

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return 'static/images/avatar.png'
