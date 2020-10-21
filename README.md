This Package is EOL and unsupported.
====================================

DEPRECATED
==========

This package was created to support 'sendmail' functionality in `pyramid_mailer`
and `repoze.sendmail`.

That exact functionality was since integrated. 

DO NOT USE THIS LIBRARY.  IT IS OLD. IT IS NOT NEEDED.


pyramid_sendmail
================

Why?
----

I wanted/needed `sendmail` functionality in my Pyramid apps.

`pyramid_mailer` wraps `respoze.sendmail` which - despite it's name - does not
actually interface with `sendmail` at all; it supports SMTP and 'maildir'
message creation.

This package was created with 3 things in mind:

1. *speed*: It's quick and dirty because i needed this done fast.

2. *compatibility*: It tries to subclass as much as possible, to both leverage
   the infrastructure from the aftorementioned 2 projects, and be easy to migrate
   (they all use the same messages, formats, etc). The only thing you should
   need to do, is replace references to `pyramid_mailer`'s init and `get_mailer()`
   functions with calls to `pyramid_sendmail`.

3. *potential upstream push*: This functionality should really be in `repoze`
   and `pyramid_sendmail`. Functionality that extends `pyramid_mailer` is in
   `p_` prefixed files; and `repoze` specific functionality is in `r_` prefixed
   files.
