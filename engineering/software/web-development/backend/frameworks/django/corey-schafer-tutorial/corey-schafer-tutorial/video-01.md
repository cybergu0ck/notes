
<br/>

## Installing django

- Create a virtual environment for the django project and install django using
	```
	pip install django
	```

- Check the django version using 
	```
	python -m django --version
	```

<br/>

## django admin

```
django-admin
```

The above command lists all the available subcommands
```
Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
```


<br/>

## Starting a django project

```
django-admin startproject <name of the project>
```

- For example, we create a django project called `django_project` using 
	```
	django-admin startproject django_project
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
- __init__.py indicates that the files in the folder are part of a Python package. Without this file, we cannot import files from another directory which we will be doing a lot of in Django!

- The manage.py file is not part of `django_project` but is used to execute various Django commands such as running the local web server or creating a new app.


<br/>

## Running a local server

```
python manage.py runserver
```

It runs a local server at http://127.0.0.1:8000 which is `localhost:8000` and we should see this page :

![image](./_assets/localhost.png)


<br/>
<br/>