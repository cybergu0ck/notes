
<br/>

## Templates
---
- django looks for templates in all installed apps.
- We create a `templates` directory in our `blog` app directory.
- Since we can clearly that this template is specific to blog app, we have to create a directory with the same name as the app,`blog` for this case. (django convention!)
- We can create html templates for our blog app inside this directory, here we create home.html and about.html
- Our tree should look like
	```
	D:.
	│   manage.py
	│
	├───blog
	│   │   admin.py
	│   │   apps.py
	│   │   models.py
	│   │   tests.py
	│   │   urls.py
	│   │   views.py
	│   │   __init__.py
	│   │
	│   ├───templates
	│   │   └───blog
	│   │           about.html
	│   │           home.html
	```

Now we have to route :
```python
#apps.py in blog dir
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

```
	We copy  the `BlogConfig` and use it as '\'blog.apps.BlogConfig\'' in INSTALLED_APPS list present in `settings.py` of django_project dir

```python
#settings.py in django_project dir
...

# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',  #new
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
...
```



the home.html contains the necessary html code 
```html
<!DOCTYPE html>

<html>
    <head>
        <title> </title>
    </head>

<body>
    <h1> Blog Home! using the template</h1>
</body>
</html>
```

Now we accommodate the template in our views.py module. We make use of the render function from django.shortcuts

```python
#views.py 

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """This is the Home page for our blog app."""
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html')       #New

def about(request):
    """This is the About page for our blog app."""
    #return HttpResponse('<h1>This is About me</h1>')
```

When we run our local server and head to localhost:8000/blog we must now see

![image](./_assets/template-home.png)

We can do similar thing for blog/about using about.html.

<br/>

## Using dictionary data as variables and adding control statements in html
---
```python
#views.py in blog

from django.shortcuts import render
from django.http import HttpResponse


#New
posts = [
    {
        'author': 'Some Dude',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 2022'
    },
    {
        'author': 'Some Other Dude',
        'title': 'Blog Post 2',
        'content': 'Seconf post content',
        'date_posted': 'August 2023'
        
    }
]


def home(request):
    """This is the Home page for our blog app."""

    context = {                                         #New
        'post_key': posts
    }
    return render(request, 'blog/home.html', context)   #New

def about(request):
    """This is the About page for our blog app."""
    
    return render(request, 'blog/about.html')

```
Here we have created a list of posts containing data in the form of dicts. We have used that list in the context variable dict and passed that as third parameter in render().

```html
<!DOCTYPE html>

<html>
    <head>
        <title> </title>
    </head>

<body>
    {% for post in post_key %}
        <h1> {{post.title}}</h1>
        <p> By {{post.author}} on {{post.date_posted}}</p>
        <p> {{post.content}}</p>
    {% endfor %}
</body>
</html>
```
Now the data passed as context can be used in home.html.
- {%    \<control statement> %} : syntax for for, if loops.
- {{ }} : To refer a variable
- post.title, post.author... all these are different non python way of referencing!

<br/>

## Passing titles
---
We can pass the title for the web page from the views.py. We modify the about function in views.py as follows:
```python
def about(request):
    """This is the About page for our blog app."""
    
    return render(request, 'blog/about.html', {'title': "About"})  #passing a title as a dict
```

We can use this accordingly in about.html as
```html
<!DOCTYPE html>

<html>
    <head>
        {% if title%}
            <title>Django Blog - {{title}} </title>
        {% else %}
            <title>Django Blog </title>
        {% endif %}
    </head>

<body>
    <h1> Blog About! using the template</h1>
</body>
</html>
```

Now if we head to localhost:8000/blog/about, we see this on the tab

![image](./_assets/6.png)

<br/>

Similarly we have modified the home.html as shown here

```html
<!DOCTYPE html>

<html>
    <head>
        {% if title%}
            <title>Django Blog - {{title}} </title>
        {% else %}
            <title>Django Blog </title>
        {% endif %}
    </head>

<body>
    {% for post in post_key %}
        <h1> {{post.title}}</h1>
        <p> By {{post.author}} on {{post.date_posted}}</p>
        <p> {{post.content}}</p>
    {% endfor %}
</body>
</html>
```



<br/>
<br/>



## Template Inheritance
---
There is repeated code in our html files, we need to follow DRY principle, hence we use template inheritance.
- We create a new html file in blog/templates/blog/ dir called `base.html`, This should contain all the repeated code (i.e. code that other html files are going to be inheriting) and a` {% block content%}{% endblock %}` so that unique things in the html files will be wrapped as content
```html
<!-- base.html  -->

<!DOCTYPE html>

<html>
    <head>
        {% if title%}
            <title>Django Blog - {{title}} </title>
        {% else %}
            <title>Django Blog </title>
        {% endif %}
    </head>

<body>
    {% block content%}{% endblock %}
</body>
</html>
```

Now our home.html and about.html should be modified to use the base.html, The home.html will look like
```html
<!-- home.html  -->

{%  extends "blog/base.html" %}

{% block content %}
    {% for post in post_key %}
        <h1> {{post.title}}</h1>
        <p> By {{post.author}} on {{post.date_posted}}</p>
        <p> {{post.content}}</p>
    {% endfor %}
{% endblock content %}
```
- Here the `{%  extends "blog/base.html" %}` will inherit the code from the base.html file (The repeated code) and the unique code is wrapped in this way
	```
	{% block content %}
	...
	{% endblock content %}
	```

___Concept clarity: So now the {% block content %} block of code of home.html will be wrapped in {% block content%}{% endblock %} body of base.html and everything on base.html will now be used to present the view.___

<br/>

Similarly, the about.html file is
```html
{% extends "blog/base.html" %}

{% block content %}
    <h1> Blog About! using the template</h1>
{% endblock content %}
    
```

<br/>
<br/>

## Using bootstrap for styling
---
We use the starter template from [Introduction · Bootstrap (getbootstrap.com)](https://getbootstrap.com/docs/4.3/getting-started/introduction/) directly

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
```

Now we use the above bootstrap code in our base.html,

```html
<!-- base.html -->
<!DOCTYPE html>

<html>
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


        {% if title%}
            <title>Django Blog - {{title}} </title>
        {% else %}
            <title>Django Blog </title>
        {% endif %}
    </head>

<body>
    <div class = "container">
        {% block content%}{% endblock %}
    </div>
    
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  
</body>
</html>
```

Now our home and about pages in local server would look like

![image](./_assets/7.png)

![image](./_assets/8.png)


<br/>
<br/>

Now we can view the page source of localhost:8000/blog/ (i.e. the home page of our blog)

```html
<!DOCTYPE html>

<html>
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


        
            <title>Django Blog </title>
        
    </head>

<body>
    <div class = "container">
        
    
        <h1> Blog Post 1</h1>
        <p> By Some Dude on August 2022</p>
        <p> First post content</p>
    
        <h1> Blog Post 2</h1>
        <p> By Some Other Dude on August 2023</p>
        <p> Seconf post content</p>
    

    </div>
    
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  
</body>
</html>
```

Notice the container class in the body (it's taken the input from the code we have written) it's different from the home.html view code.

<br/>

### Adding navigation bar

```html
<!-- This if from corey schafer's snippets folder (github)-->
<header class="site-header">
        <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
          <div class="container">
            <a class="navbar-brand mr-4" href="/">Django Blog</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarToggle">
              <div class="navbar-nav mr-auto">
                <a class="nav-item nav-link" href="/">Home</a>
                <a class="nav-item nav-link" href="/about">About</a>
              </div>
              <!-- Navbar Right Side -->
              <div class="navbar-nav">
                <a class="nav-item nav-link" href="#">Login</a>
                <a class="nav-item nav-link" href="#">Register</a>
              </div>
            </div>
          </div>
        </nav>
    </header>
```
We add this right after the body tag in our base.html, it must be on top as navigation must be the first thing from top.

<br/>
<br/>

### Creating a `static` folder in our app

All the static stuff must be in a directory called `static` and must be present in the root of our app. There must be directory with the same name as our app inside this `static` directory which will house all the static files.

```
├───blog
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           __init__.cpython-310.pyc
│   │
│   ├───static
│   │   └───blog
│   │           main.css
│   │
│   ├───templates
│   │   └───blog
│   │           about.html
│   │           base.html
│   │           home.html
```
We can see that we have added a main.css file in the static folder under blog. This main.css was also downloaded from corey's github.

<br/>

```css
body {
    background: #fafafa;
    color: #333333;
    margin-top: 5rem;
  }
  
  h1, h2, h3, h4, h5, h6 {
    color: #444444;
  }
  
  ul {
    margin: 0;
  }
  
  .bg-steel {
    background-color: #5f788a;
  }
  
  .site-header .navbar-nav .nav-link {
    color: #cbd5db;
  }
  
  .site-header .navbar-nav .nav-link:hover {
    color: #ffffff;
  }
  
  .site-header .navbar-nav .nav-link.active {
    font-weight: 500;
  }
  
  .content-section {
    background: #ffffff;
    padding: 10px 20px;
    border: 1px solid #dddddd;
    border-radius: 3px;
    margin-bottom: 20px;
  }
  
  .article-title {
    color: #444444;
  }
  
  a.article-title:hover {
    color: #428bca;
    text-decoration: none;
  }
  
  .article-content {
    white-space: pre-line;
  }
  
  .article-img {
    height: 65px;
    width: 65px;
    margin-right: 16px;
  }
  
  .article-metadata {
    padding-bottom: 1px;
    margin-bottom: 4px;
    border-bottom: 1px solid #e3e3e3
  }
  
  .article-metadata a:hover {
    color: #333;
    text-decoration: none;
  }
  
  .article-svg {
    width: 25px;
    height: 25px;
    vertical-align: middle;
  }
  
  .account-img {
    height: 125px;
    width: 125px;
    margin-right: 20px;
    margin-bottom: 16px;
  }
  
  .account-heading {
    font-size: 2.5rem;
  }
```

<br/>

To load the static files in our html files we have to use the following code at the top of the html file.
```
{% load static %}
```

Now, we replace the `blockcontent` in our base.html with the following code.
```css
<main role="main" class="container">
        <div class="row">
            <div class="col-md-8">
            {% block content %}{% endblock %}
            </div>
            <div class="col-md-4">
            <div class="content-section">
                <h3>Our Sidebar</h3>
                <p class='text-muted'>You can put any information here you'd like.
                <ul class="list-group">
                    <li class="list-group-item list-group-item-light">Latest Posts</li>
                    <li class="list-group-item list-group-item-light">Announcements</li>
                    <li class="list-group-item list-group-item-light">Calendars</li>
                    <li class="list-group-item list-group-item-light">etc</li>
                </ul>
                </p>
            </div>
            </div>
        </div>
    </main>
```

Finally our base.html should look like this

```html
<!-- base.html-->
{% load static %}
<!DOCTYPE html>

<html>
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

        <link rel="stylesheet" type ="text/css" href="{% static 'blog/main.css' %}">

        {% if title%}
            <title>Django Blog - {{title}} </title>
        {% else %}
            <title>Django Blog </title>
        {% endif %}
    </head>

<body>
    <header class="site-header">
        <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
          <div class="container">
            <a class="navbar-brand mr-4" href="/">Django Blog</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarToggle">
              <div class="navbar-nav mr-auto">
                <a class="nav-item nav-link" href="/">Home</a>
                <a class="nav-item nav-link" href="/about">About</a>
              </div>
              <!-- Navbar Right Side -->
              <div class="navbar-nav">
                <a class="nav-item nav-link" href="#">Login</a>
                <a class="nav-item nav-link" href="#">Register</a>
              </div>
            </div>
          </div>
        </nav>
    </header>

    <main role="main" class="container">
        <div class="row">
            <div class="col-md-8">
            {% block content %}{% endblock %}
            </div>
            <div class="col-md-4">
            <div class="content-section">
                <h3>Our Sidebar</h3>
                <p class='text-muted'>You can put any information here you'd like.
                <ul class="list-group">
                    <li class="list-group-item list-group-item-light">Latest Posts</li>
                    <li class="list-group-item list-group-item-light">Announcements</li>
                    <li class="list-group-item list-group-item-light">Calendars</li>
                    <li class="list-group-item list-group-item-light">etc</li>
                </ul>
                </p>
            </div>
            </div>
        </div>
    </main>
    
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  
</body>
</html>
```


### Adding css to our home view 

We replace the for loop in our home.html file with the following code and the home.html should look like this
```html
<!-- home.html-->
{%  extends "blog/base.html" %}

{% block content %}
    {% for post in post_key %}
        <article class="media content-section">
            <div class="media-body">
            <div class="article-metadata">
                <a class="mr-2" href="#">{{ post.author }}</a>
                <small class="text-muted">{{ post.date_posted }}</small>
            </div>
            <h2><a class="article-title" href="#">{{ post.title }}</a></h2>
            <p class="article-content">{{ post.content }}</p>
            </div>
        </article>
        {%endfor%}
{% endblock content %}
```

<br/>

>Ctrl + F5 to hard refresh our browser page!

<br/>


Our local pages will look like this,

![image](./_assets/9.png)

<br/>

![image](./_assets/10.png)


<br/>
<br/>

### Adding url name tags instead of hard coding

If we notice the navigation tag code in the body of the base.html, we can see that the href present there are all hard coded (example href = '/' and href = '/about'), We want to use the url name tags so that we can change the url once in url.py rather than changing all the href's. This can be done by making use of the name tags in the url.py

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
]

```
We make use of the name = 'blog-home' and name = 'blog-about' in the href's as follows 

```html
 href = {% url 'blog-home'%} <!-- For home -->
 href = {% url 'blog-about'%} <!-- For about -->
```