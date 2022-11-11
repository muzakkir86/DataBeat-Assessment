from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from rest_framework.serializers import ModelSerializer


# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, confirm_password=None):
        # Creates and saves a User with the given email, name and password.
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


# Custom user model
class User(AbstractBaseUser):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin


# Creating Movie model
class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=300)
    created_at = models.DateField()
    updated_at = models.DateField()
    runtime = models.IntegerField()
    language = models.CharField(max_length=20)
    tagline = models.CharField(max_length=100)


# Creating MovieSerializer
class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


# Creating Cast Model
class Cast(models.Model):
    cast_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    dob = models.DateField()


# Creating CastSerializer
class CastSerializer(ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'
