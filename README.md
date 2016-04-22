# Camera Obscura

[![Build Status](https://travis-ci.org/tesmonrd/django-imager.svg?branch=master)](https://travis-ci.org/tesmonrd/django-imager)

A django web application the allows for users to create, edit, and store photos and photo albums on the AWS cloud. Requires registration to work. Utilizes django-registration, AWS EC2 and RDS, Python, bootstrap, and HTML5.

** To account for registration error, run makemigrations and migrate normally, then run "manage.py makemigrations imager_profile" --> "migrate imager_profile" and run "manage.py makemigrations imager_images" --> "migrate imager_images"
