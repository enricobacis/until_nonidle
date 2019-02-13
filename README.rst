until_nonidle
=============

Execute something as long as the user is idling.

Description
-----------

.. image:: https://travis-ci.com/enricobacis/until_nonidle.svg?token=3zn37kZJ8DSzJpXNU199&branch=master
    :target: https://travis-ci.com/enricobacis/until_nonidle

The tools is especially useful in combination with auto lockscreens.
The user can be notified (by a dimming action on the screen or by showing a
text message on the display) about the fact that the computer is being locked,
and can perform an action such as moving the mouse to dismiss the action.

Requirements
------------

-  xprintidle
-  psutil

Example
-------

.. code::

   ./until_nonidle.py sleep 10

The ``sleep 10`` command terminates if the user comes back from idling.
