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

Now, it'll have a directory created with the name "django_project" with the files as follows:

```
D:.
│   manage.py
│
└───django_project
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
```

- asgi.py allows for an optional Asynchronous Server Gateway Interface to be run.
- settings.py controls our Django project’s overall settings.
- urls.py tells Django which pages to build in response to a browser or URL request.
- wsgi.py stands for Web Server Gateway Interface which helps Django serve our eventual web pages.
- **init**.py indicates that the files in the folder are part of a Python package. Without this file, we cannot import files from another directory which we will be doing a lot of in Django!

- The manage.py file is not part of `django_project` but is used to execute various Django commands such as running the local web server or creating a new app.

<br/>
