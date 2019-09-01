# To-Do List

A simple To-Do list app which helps users organizing their tasks. This app is built based on TDD.

This app is developed and tested on Ubuntu/Windows, deployed using AWS EC2.

## Installation

Required software:
- Google Chrome web browser
- Chrome Driver
- Python 3, Django 1.11 and Selenium 3

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the requirements.

## Development (Linux/Windows)

Setting up and activating your Virtualenv:
```
cd to-do-list
python -m venv virtualenv

# Activate venv on Linux
source virtualenv/bin/activate 

# Activate venv on Windows
virtualenv/Scripts/activate
```

Installing all the app requirements:
```
pip install -r requirements.txt
```

Database migration:
```
python manage.py makemigrations
python manage.py migrate
```

Running all functional test + unit tests:
```
python manage.py test
```

Run on local server:
```
python manage.py runserver
```

## Deployment

The deployment of this app is automated using [Fabric](https://docs.fabfile.org/en/1.4.1/index.html).
```
$ pip install fabric
```

How to use fabric here:
```
# fab deploy:host=users@hostname
# Example:
fab deploy:host=ubuntu@ip-123-456-host-name
```

Fabric help:
```
fab --help
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
