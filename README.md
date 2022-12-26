# Initial set-up

## Start project structure
```shell
python -m venv .venv
source .venv/bin/activate
pip install django~=4.0.0
django-admin startproject django_project .
python manage.py startapp blog
python manage.py makemigrations
python manage.py migrate
```

- Add blog.apps.BlogConfig to django_projects/settings.py
- Ensure everything works as expected starting server in local: `python manage.py runserver`
- Open browser at and see the django welcome page: `http://localhost:8000`
- Create models: `...`
- Make migrations: `python manage.py makemigrations && python manage.py migrate`
- Create superuser for admin: `python manage.py createsuperuser`
- Register Post model in admin, edit blog/admin.py:
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

