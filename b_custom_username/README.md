#Custom Username

The custom user has a username that can only contain letters, numbers, and hyphens. The username also must be at least 8 characters long. This is a more restrictive version of the AbstractUser, but otherwise, this class has the same fields as the AbstractUser class. Django does not allow model Fields from inherited classes to be overridden, so while we only want to change one Field of the Abstractuser class, we need to replicate all of its classes in our own class (which inherits from the same classes as AbstractUser, AbstractBaseUser and PermissionsMixin).

###Modified files:
`settings.py` - set `AUTH_USER_MODEL` to the custom user
`user/models.py` - define the `User` model
`user/forms.py` - extend the `UserCreationForm` form
`users/admin.py` - register the `User` model with the admin site

###Setup

```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata ../fixture_data.json
```
