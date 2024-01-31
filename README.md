Library Management System API using Django and django-rest-framework

#Initial Setup:

Install  virtual environment: python -m venv env 

Install django : pip install django 

Start a new django Project: django-admin startproject elibrary 

Set Up a postgres Database : pip install psycopg2-binary 

Change settings.py files to include postgres database : 

DATABASES = {

    'default': {
		
        'ENGINE': 'django.db.backends.postgresql',
				
        'NAME': 'yourdbname',
				
        'USER': 'yourdbuser',
				
        'PASSWORD': 'yourpassword',
				
        'HOST': 'localhost',
				
        'PORT': '',
				
    }
		
} 

Start a new app named api: python manage.py startapp api 

Install django-rest-framework: pip install django-rest-framework 

The initial setup is now complete 
