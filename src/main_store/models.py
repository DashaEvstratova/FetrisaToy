from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager as DjangoUserManager
from main_store.enums import Role
from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True


class UserManager(DjangoUserManager):
    def _create_user(self, email, password, commit=True, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, role=Role.admin, **extra_fields)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    email = models.EmailField(unique=True)
    role = models.CharField(choices=Role.choices, max_length=15, default=Role.user)
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    patronymic = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to="static/users", height_field=None, width_field=None, max_length=100)
    city = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    house = models.IntegerField(null=True, blank=True)
    corps = models.CharField(max_length=255, null=True, blank=True)
    apartment = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=12, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    @property
    def is_staff(self):
        return self.role in (Role.admin, Role.staff)

    @property
    def is_superuser(self):
        return self.role == Role.admin

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class PromoCode(models.Model):
    name = models.CharField(unique=True, max_length=255)
    discount_percentage = models.IntegerField()


class Orders(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True, blank=True, default="Active")
    promo_code = models.ForeignKey(PromoCode, null=True, blank=True, on_delete=models.DO_NOTHING, default=None)
    sum_of_order = models.FloatField()


class Items(models.Model):
    name = models.CharField(unique=True, max_length=255)
    number = models.IntegerField()
    size = models.FloatField()
    price = models.IntegerField()
    description = models.TextField(max_length=100000)
    category = models.CharField(max_length=25)


class Review(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=10000)
    stars = models.FloatField()


class OrederData(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    count = models.IntegerField()


class Color(models.Model):
    color = models.CharField(max_length=255)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)


class Pictures(models.Model):
    picture = models.ImageField(upload_to="static/toys", height_field=None, width_field=None, max_length=100)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="pictures")


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "item"], name="user_item_buket")]


class Buket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "item"], name="user_item")]
