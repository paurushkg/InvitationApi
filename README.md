# InvitationApi
Backend Project

## Steps to setup this project locally

-  Make sure Python 3.x is already installed. [See here for help](https://www.python.org/downloads/).
-  Clone the repo and configure the virtual environment:
-  To know about virtualenv use this link [VirtualEnv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
```
$ git clone https://github.com/sumit4613/NidhiSanchar-BE.git
$ cd NidhiSanchar-BE
$ source .venv/bin/activate # activate virtual environment (.venv is the name, use any name as you like)
$ pip install -r requirements.txt
```

-  Set up the initial migration for our custom user models in users and build the database.

```
(.venv) $ python manage.py makemigrations
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
```

- To view API endpoints, go to [Swagger](http://127.0.0.1:8000/swagger/)

### To follow PEP8 code conventions, integrated [Pre-Commit](https://pre-commit.com) which formats code using [Black](https://github.com/psf/black) code formatter.

- To use this run `pre-commit install`, now whenever you commit changes, pre-commit will check the files which you have updated and run some checks.
