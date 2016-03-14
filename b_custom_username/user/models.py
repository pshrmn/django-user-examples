from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core.validators import RegexValidator, MinLengthValidator
from django.core.mail import send_mail
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):

    """
    The username is the only Field from the AbstractUser that we
    want to override, but because Django doesn't allow for overriding
    Fields, we must instead replicate the AbstractUser class.
    """
    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            RegexValidator(
                r'^[a-zA-Z0-9_]*$',
                message='Valid characters are letters, numbers, and hyphens'
            ),
            MinLengthValidator(
                6,
                message='Username must be at least 8 characters'
            )
        ],
        error_messages={
            'unique': 'Username is taken',
        }
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
