* **Python 2.7.x**
* **Django 1.11**
* **Bootstrap 4.0**
* **SendInBlue V3**
* **Sentry**

**1. Installation**

**Django 1.11**

`$ pip install Django==1.11`

`$ django-admin startproject mysite`

**2. Le serveur de développement**

`$ python manage.py runserver`

**Famework Bootstrap 4.0**

```html
<link rel="stylesheet"href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"/>
```


**Sendinblue v3**

La documentation complète pour l’installation et l’utilisation
https://github.com/sendinblue/APIv3-python-library/



**Sentry**

`$pip install raven`
open settings.py

include the below lines in settings.py

```python
RAVEN_CONFIG = {'dsn': '<your-dsn-here>',}
INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
```

