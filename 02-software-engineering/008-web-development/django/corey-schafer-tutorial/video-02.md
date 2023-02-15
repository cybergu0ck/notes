
<br/>

# Creating App

In a django project we can create multiple apps. This creates modularity.

```
python manage.py startapp <name of the app>
```

Here we are creating a "blog" app in django_project, `python manage.py startapp blog`
Now our tree structure would look like this,

```
Volume serial number is 4297-79C6
D:.
│   db.sqlite3
│   manage.py
│
├───blog
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   views.py
│   │   __init__.py
│   │
│   └───migrations
│           __init__.py
│
└───django_project
    │   asgi.py
    │   settings.py
    │   urls.py
    │   wsgi.py
    │   __init__.py
```

<br/>


## Creating Views

views.py file present in our app handles the views.

```python
#views.py

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """This is the Home page for our blog app."""
    return HttpResponse('<h1>Blog Home</h1>')

```

Create a `urls.py` in blog directory (not to be confused with urls.py present in the django_project \[project level\] ) and add the code :
```python
#urls.py present in blog
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
]
```
This module routing inside the `blog` app. Here, we are importing the views module to get the `home` function. Therefore whenever we access the blog app, a home view can be seen. The empty string in path function is explained down.


Now we have to make changes in the `urls.py` present in project level i.e. `django_project` as follows:
```python
#urls.py present in django_project
from django.contrib import admin
from django.urls import path, include  #New


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls'))   #New
]
```
the  `path('blog/',include('blog.urls'))` routes the `blog/` to the `urls.py` present in `blog` app, we use `include` function for this.


> the `include` function in path() in urls.py present in django_project processes everything until blog/ and returns the remaining string to the path() present in blog. Since there is nothing after blog/ in n urls.py present in django_project, we have empty string '' in path() present in blog!


When we run the local server and hit localhost:8000/blog we must see,

![image](./_assets/blog-home.png)

Creating another view to understand this concretely, 

```python
#views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """This is the Home page for our blog app."""
    return HttpResponse('<h1>Blog Home</h1>')


def about(request):                                      #New
    """This is the About page for our blog app."""
    return HttpResponse('<h1>This is About me</h1>')
```

```python
#urls.py in blog app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),  #New
]

```
We do not need to edit the urls.py in django_project. Now the include fucntion in path() of urls.py in django_project process everything till blog/ and the remaning string i.e. 'about/' is fed. This string is found in path() of urls.py in blog app, and hence it redirects it to the views.about.  If we run a local server and head to localhost:8000/blog/about, we see the following:

![image](./_assets/blog-about.png)

if we want our blog app (the home view to be specific) to be shown in the localhost itself (i.e. show home view when we head to localhost:8000 instead of localhost:8000/blog), we have to modify the urls.py present in django_project :

```python
#urls.py in django_project
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls') )     #New, make it as empty string!
]

```


<br/>
<br/>
