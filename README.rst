Pymorning
=========

Having spotify in one window change to a terminal with Alt + Tab and run.

  $ python alarm.py

The macro runs "Alt + Tab" then "Space".

You can specify hours and minutes for the time you want to sleep like.

  $ python alarm.py 5 30

This is 5 hours and 30 minutes.

A random delta is added to the sleep time. It can be set as a third argument.

  $ python alarm.py 5 30 5

This is 5 hours and 30 minutes +/- a random number of minutes between 0 and 5.

Use 0 to disable it.

  $ python alarm.py 5 30 0

This is 5 hours and 30 minutes with no delta.

Tested in spotify web client in Chrome and should work on any browser or the native client.
