pyramid_sendmail

i wanted / needed sendmail functionality in my pyramid apps

pyramid_mailer wraps respoze.sendmail which, despite it's name, does not interface with sendmail at all -- it supports SMTP and 'maildir' message creation 

this package was created with 3 things in mind:

1 speed.  it's quick and dirty because i needed this done fast.
2 compatibility.  it tries to subclass as much as possible, to both leverage the infrastructure from the aftorementioned 2 projects and be easy to migrate ( they all use the same messages, formats, etc).  the only thing you should need to do, is replace references to pyramid_mailer's init and get_mailer() functions with calls to pyramid_sendmail
3 potential upstream push. this functionality should really be in repoze and pyramid_sendmail.  functionality that extends pyramid_mailer are in p_ files, and repoze specific functionality is in r_ files





