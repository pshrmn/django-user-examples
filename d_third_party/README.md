# Third Party Users

Sometimes it is useful to allow users to sign in through other websites. Doing this is made relatively easy by the `python-social-auth` module.

The majority of the work in setting up third party sign in is done in your settings. Along with registering `python-social-auth`'s app in the `INSTALLED_APPS`, you must also include its context processors, any authentication backends your site allows, and auth key/secret for the third party sites (loaded from environment variables).

[settings documentation](http://psa.matiasaguirre.net/docs/configuration/settings.html)

When a user authenticates through a third party app, two instances will be added to the database. The first is an instance of your `AUTH_USER_MODEL` which will be populated with data retrieved from the third party. The other is an auth instance of the user, which contains a foreign key to the `AUTH_USER_MODEL` table, which third party the user signed in with, a user id, and any extra data.

When the `AUTH_USER_MODEL` instance is created for a user, it attempts to set the best possible username for the user. Username generation can also be controlled through settings.
