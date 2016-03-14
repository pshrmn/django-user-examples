from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.mail import send_mail


class UserManager(BaseUserManager):

    user_in_migrations = True

    def create_user(self, email, password, **extras):
        if not email:
            raise ValueError('email is required')
        # BaseUserManager.normalize_email converts domain to lowercase
        user = self.model(
            email=self.normalize_email(email),
            **extras
        )
        # set_password will take take of the hashing
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extras):
        if not email:
            raise ValueError('email is required')
        user = self.model(
            email=self.normalize_email(email),
            **extras
        )
        user.set_password(password)
        # make sure the user is staff and a superuser
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', ]

    objects = UserManager()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
