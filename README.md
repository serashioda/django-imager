
[![Build Status](https://travis-ci.org/serashioda/django-imager.svg?branch=front-end-4)](https://travis-ci.org/serashioda/django-imager) [![Coverage Status](https://coveralls.io/repos/github/serashioda/django-imager/badge.svg?branch=front-end-4)](https://coveralls.io/github/serashioda/django-imager?branch=front-end-4)

# Django Imager

A simple image management app built on Django.

by [Sera Smith](https://github.com/serashioda) and [Ben Petty](https://github.com/benpetty)

## Tools

- Python
- Django
- PostgreSQL
- Psycopg2

## Models

The `ImagerProfile` class contains a standard Django user model with additional properties:

- `camera_type` (CharField stores details about user's photo equipment)
- `address` (CharField stores user's physical or/ mailing address)
- `bio` (TextField stores a text bio about user)
- `personal_website` (URLField stores user's personal or professional website)
- `hireable` (Boolean indicating if user is available for hire)
- `travel_radius` (DecimalField indicating how far user is willing to travel from there saved address for work)
- `phone` (CharField storing user's preferred phone contact number)
- `photo_type` (CharField storing the type of photo)
- `is_active` (Boolean indicating if user account is active)
- `imager_id` (UUIDField storing user's unique ID#)

## Tests

### Required testing packages:

- factory-boy
- Faker
- Coverage


To test with coverage:
```bash
$ coverage run --source='.' manage.py test
$ coverage report
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
imager_profile/__init__.py       0      0   100%
imager_profile/admin.py          3      0   100%
imager_profile/models.py        35      2    94%   64, 68
imager_profile/urls.py           3      3     0%   3-6
imager_profile/views.py          6      6     0%   2-12
imagersite/__init__.py           0      0   100%
imagersite/settings.py          28      0   100%
imagersite/urls.py               8      8     0%   16-34
imagersite/views.py              3      3     0%   3-8
----------------------------------------------------------
TOTAL                           86     22    74%
```

