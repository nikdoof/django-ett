django-ett
==========

Django webapp implementation of the "Emergent Task Timer"

What is a "Emergent Task Timer"
-------------------------------

[David Seah], back in 2006, took a existing idea of using a egg timer and a todo list to track the time that tasks take and created a quick and easy way to track and monitor your time over the course of a day. He [wrote](http://davidseah.com/blog/2006/04/the-printable-ceo-iii-emergent-task-timing/) a very detail post about the subject and describes how splitting your time into 15 minute segments can make it simple to keep you control of your working time.

Out of this he developed a sheet to write down his results, and a associated [Flash prototype](http://davidseah.com/tools/ett/alpha). Unfortunatly he was unable to continue developing this app has his needs had already been met, he did release the [source code](http://davidseah.com/blog/2010/01/releasing-the-ett-online-to-creative-commons/) but little development has been done since.

Why a Django webapp?
--------------------

I needed something to keep my records centralized, so I decided to develop with the tools I know and understand. Django already had the framework and supporting application (Tastypie) that would enable me to rapidly develop an application for my own use.

License
-------

As I developed this application for personal use, i've released the code under BSD 2-clause.

Setup
-----

This is a standard Django 1.4 default application layout, it can be hosted under numerous WSGI containers without much modification. Included is requirement.txt files for virtualenv setup so it should be flexable enough for your requirements.


Testing
-------

[![Build Status](http://ci.tensixtyone.com/job/django-ett/badge/icon)](http://ci.tensixtyone.com/job/django-ett/)

This project makes use of the standard Django testing framework, along with django-jenkins to allow for easy integration into Jenkins/Hudson.
