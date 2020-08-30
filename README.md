# To-Do List

<a href="https://imgur.com/PHR7uMs"><img src="https://i.imgur.com/PHR7uMs.png" title="source: imgur.com" /></a>

A simple To-Do list app which helps users organizing their tasks. This app is built based on TDD

## Tech Stacks

- Django 3.1

## Setup (Ubuntu)

### Environment Variables

```sh
# SMTP
export EMAIL_USER="my@gmail.com"
export EMAIL_PASSWORD="my-secret-password"

# DJANGO
export DJANGO_SECRET_KEY="my-django-secret"

```

### Installation

This project uses [pipenv](https://github.com/pypa/pipenv)

```sh
# To activate pipenv
pipenv shell

# To install all the dependencies
pipenv install --dev

```

### Database migraiton

```sh
python3 manage.py migrate

```

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change

## Steps

1. Fork this
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Tests

```sh

# Unit Tests (UT) + Functional tests (FT)
python3 manage.py test

# FT
python3 manage.py test functional_tests

# UT
python3 manage.py test lists
```
