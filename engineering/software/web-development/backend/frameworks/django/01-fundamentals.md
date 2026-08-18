# Django

**_Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design._**

- It is free and opensource.

<br>

### Batteries Included philosophy

Django is known for its "batteries-included" philosophy, which means it comes with many built-in features and libraries, reducing the need to rely on external packages for common web development tasks.

<br>
<br>

## Installing django

- Create a [virtual environment](../../../../programming-languages/python/07-modules/venv.md#creating-a-new-virtual-environment) for the django project and install django using

  ```
  pip install django
  ```

- Check the django version using
  ```
  python -m django --version
  ```

<br/>
<br/>

## Starting a django project

```
django-admin startproject <name of the project>
```

- For example, we create a django project called `django-project` using
  ```
  django-admin startproject django-project
  ```

<br>
<br>

## Directory Structure

The directory structure after we create a new django project will be like:

```bash
C:.
└───learning-django   # directory on the machine (DO NOT consider as root of django project)
    ├───django-env    # directory created while creating python virtual environment
    └───django_proj   # root directory of the django project
        │   manage.py       # Command-line utility for managing the project
        │
        ├───django_proj     # Django project settings and configuration
        │       asgi.py         # ASGI application entry point (for ASGI servers); Asynchronous Server Gateway Interface
        │       settings.py     # Project settings (database, apps, middleware, etc.)
        │       urls.py         # URL routing configuration
        │       wsgi.py         # WSGI application entry point (for WSGI servers);  Web Server Gateway Interface
        │       __init__.py     # Indicates that the files in the folder are part of a Python package.
        |
        ├───app1            # Django app
        │   │   admin.py        # Admin configurations for the app
        │   │   apps.py         # App-specific configuration
        │   │   models.py       # Database models for the app
        │   │   tests.py        # Unit tests for the app
        │   │   views.py        # Views and view functions for the app
        │   │   __init__.py
        │   │
        │   └───migrations      # Database migrations
        │           __init__.py
        │
        │
        ├───media           # User-uploaded media files (e.g., user avatars)
        |
        ├───static          # Static files (CSS, JavaScript, images, etc.)
        |   └───app1
        |
        └───templates       # HTML templates
            └───app1            # App-specific templates
```

<br>
<br>

## Running a local server

```
python manage.py runserver
```

It runs a local server at http://127.0.0.1:8000 which is `localhost:8000` and we should see this page :

![image](./_assets/localhost.png)

<br/>
<br/>
