# Django app

<br>
<br>

## Creating App

- In a django project we can create multiple apps. This creates modularity. Django apps can be swapped from one project to another!

  ```
  python manage.py startapp <name of the app>
  ```

<br>
<br>

## Include the App

- The created app needs to be included in the django project to be used. This is done by adding the name of the app in the `<root-folder-of-django-project>\settings.py`

  ```py
  # Application definition

  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'app1'    # Like so!
  ]

  # ...
  ```

## Views
