from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _





class UserManager(BaseUserManager):
    def create_user(self, email, name, district, city, state, number, password=None, **extra_fields):
        if not email:
            raise ValueError(_('User must have an email'))
        if not password:
            raise ValueError(_('User must have a password'))
        if not name:
            raise ValueError(_('User must have a full name'))

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            district=district,
            city=city,
            state=state,
            number=number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, name, number, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.CharField(_('email address'), max_length=100, primary_key=True)
    name = models.CharField(_('full name'), max_length=25)
    district = models.CharField(_('district'), max_length=50)
    city = models.CharField(_('city'), max_length=50)
    state = models.CharField(_('state'), max_length=50)
    number = models.CharField(_('phone number'), max_length=20, validators=[MinLengthValidator(10), MaxLengthValidator(10)])
    active = models.BooleanField(_('active'), default=True)
    staff = models.BooleanField(_('staff status'), default=False)
    admin = models.BooleanField(_('admin status'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'district', 'city', 'state', 'number']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.admin

    @property
    def is_active(self):
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
    ac = models.BooleanField(default=False)
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
    ac = models.BooleanField(default=False)
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
    