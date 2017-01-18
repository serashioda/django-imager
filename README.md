[![Build Status](https://travis-ci.org/serashioda/django-imager.svg?branch=master)](https://travis-ci.org/serashioda/django-imager)

# Django Imager

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