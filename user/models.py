from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.core.validators import MinLengthValidator, MaxLengthValidator



# # Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, name, location, city, state, number, password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('User must have a password')
        if not name:
            raise ValueError('User must have a full name')

        user = self.model(email=self.normalize_email(email))
        user.name = name
        user.set_password(password)
        user.location = location
        user.city = city
        user.state = state
        user.number = number
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self,email, name, number, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('User must have a password')
        if not name:
            raise ValueError('User must have a full name')

        user = self.model(email=self.normalize_email(email))
        user.name = name
        user.number = number
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    # number = models.CharField(max_length=10)
    number = models.CharField(
        max_length=20,  # Adjust max_length as needed
        validators=[MinLengthValidator(10), MaxLengthValidator(10)]
    )

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'number']
    objects = UserManager()

    def __str__(self):
        return self.email

    @staticmethod
    def has_perm(perm, obj=None):
         # "Does the user have a specific permission?"
         # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
         # "Does the user have permissions to view the app `app_label`?"
         # Simplest possible answer: Yes, always
         return True

    @property
    def is_staff(self):

        # "Is the user a member of staff?"

        return self.staff

    @property
    def is_admin(self):

        # "Is the user a admin member?"

        return self.admin

    @property
    def is_active(self):

        # "Is the user active?"

        return self.active


class Room(models.Model):

    room_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_email = models.ForeignKey(User, on_delete=models.CASCADE)
    dimention = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    cost = models.IntegerField()
    bedrooms = models.IntegerField()
    kitchen = models.BooleanField(default=False)
    hall = models.BooleanField(default=False)
    balcany = models.BooleanField(default=False, verbose_name='Balcony')
    desc = models.CharField(max_length=200)
    AC = models.BooleanField(default=False)
    booked = models.BooleanField(default=False, editable=False)
    img = models.ImageField(upload_to='room_id/', height_field=None,
                            width_field=None, max_length=100)
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.user_email)


class House(models.Model):

    house_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_email = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # onwer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='landlord')
    area = models.IntegerField()
    floor = models.IntegerField()
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    cost = models.IntegerField()
    bedrooms = models.IntegerField()
    kitchen = models.BooleanField(default=False)
    hall = models.BooleanField(default=False)
    balcany = models.BooleanField(default=False, verbose_name="Balcony")
    desc = models.CharField(max_length=200)
    AC = models.BooleanField(default=False)
    booked = models.BooleanField(default=False, editable=False)
    img = models.ImageField(upload_to='house_id/', height_field=None,
                            width_field=None, max_length=100)
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.user_email)


class Contact(models.Model):

    contact_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    body = models.CharField(max_length=500)

    def __str__(self):
        return str(self.email)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer')
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    booked = models.BooleanField(default=False)
    date = models.DateField()
    
    
# class Message(models.Model):
    