# Setup
## prerequisites
* python ( for installation refer to https://www.python.org/downloads/ )
* git ( for installation refer to https://git-scm.com/downloads )
## clone 
```
$ git clone https://github.com/FliprClassroom/Backend.git
$ cd backend
```
## virtual env
```
$ pip install virtualenv
$ virtualenv env
$ source env/Scripts/activate
(env)$ pip install -r requirements.txt
```
## run locally
```
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```

