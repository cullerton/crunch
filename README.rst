======
crunch
======

crunch is a simple package for an interview programming test.

-------------
iter_commands
-------------

crunch contains a single function `iter_commands`.
`iter_commands` is a generator.
`iter_commands` takes a list (str) of sql commands as an argument. These sql commands can contain comments.

`iter_commands` loops through the commands and separates them into tuples.
The tuples include the start and end location of the command and a counter, along with the command.

The tuples are then yielded back to the caller.

-----
Tests
-----

Crunch uses the built-in unittest testing framework.

To run the tests, issue the following command from the top-level crunch directory.
This should be the same directory that contains this README file.

::

    $ python test.py
