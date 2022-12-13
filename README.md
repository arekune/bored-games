# Bored Games       <img alt="GitHub" src="https://img.shields.io/github/license/smahesh29/Django-WebApp">

This project is practice work for the Sovellusohjelmointi (Application Programming) course of the Turku University of Applied Sciences. The task was to create a web application with Django where users can add and rent board games.

## Installation

Clone repository locally and `cd` into the root (project-level) directory. 
Make sure that you have Python installed and then install requirements:

```bash
$ pip install -r requirements.txt
```

You may install Django directly instead either globally or in a local virtual environment:

```bash
$ pip install django
```

## Usage

Run migrations to set up database schema (project uses SQLite by default):

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

Create a local project environment to store your secret key:

```bash
$ pip install python-decouple
```
or
```bash
$ pip install python-dotenv
```

Create a `.env` file in your root (project-level) directory.  
Generate a new secret key (for instance on [Djecrety](https://djecrety.ir/)).  
Add your secret key file into the `.env` file:

```bash
SECRET_KEY=yoursecretkey
```

In `settings.py`, add the following if you installed python-decouple:

```bash
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

Or if you installed python-dotenv:

```bash
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SECRET_KEY = os.environ['SECRET_KEY']
```

Create an admin user for development:
```bash
$ python manage.py createsuperuser
```

Run development server:
```bash
$ python manage.py runserver
```

In your web browser, enter the address: http://localhost:8000 or http://127.0.0.1:8000/

  
## Acknowledgements

The pictures used as background images on this app were sourced from [Unsplash](https://unsplash.com/) (see [license](https://unsplash.com/license)).

We would like to acknowledge and extend our gratitude to the following photographers for their work:

* [Karthik Balakrishnan](https://unsplash.com/@karthikb351)
* [Mireille Raad](https://unsplash.com/@mireilleraad)
* [Arjan de Jong](https://unsplash.com/@aristocratie)
* [Tono Graphy](https://unsplash.com/@tonography)
* [Maarten van den Heuvel](https://unsplash.com/@mvdheuvel)
* [Hans-Peter Gauster](https://unsplash.com/@sloppyperfectionist)
