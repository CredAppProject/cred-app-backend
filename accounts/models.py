from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager,PermissionsMixin
import uuid


class UserManager(BaseUserManager):
  """
  Custom Django User Manager for the Custom User Model Created.
  """
  def create_user(self, email, name, phone,password=None):
      user = self.model(
          email = self.normalize_email(email),
          name = name,
          phone = phone,
      )
      user.set_password(password)
      user.save(using = self._db)
      return user

  def create_superuser(self, email,name,phone,password=None):
      user = self.create_user(
          email=email,
          password=password,
          name = name,
          phone = phone,
      )
      user.is_admin = True
      user.is_staff = True
      user.save(using=self._db)
      return user

class User(AbstractBaseUser,PermissionsMixin):
  """
  Custom Django User Model without Username.
  """
  id = models.CharField(max_length=200, default=uuid.uuid4,unique=True,primary_key=True)
  email = models.EmailField(null=False, max_length=100,unique=True)
  name = models.CharField(null=False, max_length=100)
  phone = models.IntegerField(null=False,unique=True,upload="accounts")
  profile_picture = models.ImageField(null=True)
  date_joined = models.DateTimeField(auto_now=True)
  company = models.CharField(null=True, max_length=200)
  job = models.CharField(null=True, max_length=200)

  is_admin = models.BooleanField(default = False)
  is_active = models.BooleanField(default = True)
  is_staff = models.BooleanField(default = False)
  is_superuser = models.BooleanField(default = False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name','phone']

  objects = UserManager()

  def __str__(self):
      return self.email + ", " + self.name
  
  def has_perm(self, perm, obj = None):
      return self.is_admin

  def has_module_perms(self, app_label):
      return True