#Email as username

Sometimes you may want to use a different field than a username to uniquely identify a user. For example, an email address can be used for user authentication. Like the `AbstractUser`, the `User` model created in this example inherits from the `AbstractBaseUser` and `PermissionsMixin` classes.

For the `AbstractBaseUser`, our model needs to set a `USERNAME_FIELD` attribute as well as provide `get_full_name` and `get_short_name` methods. For the `PermissionsMixin`, our model needs an `is_active` Field.

The custom `User` model will also need its own `Manager` that provides `create_user` and `create_superuser` methods.

###Modified files:
`settings.py` - set `AUTH_USER_MODEL` to the custom user
`user/models.py` - define the `User` and `UserManager` models
`user/forms.py` - extend the `UserCreationForm` form and create a `UserChangeForm`
`users/admin.py` - define the `UserAdmin` class and register the `User` model with the admin site

###Setup

```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata ../fixture_data.json
```
