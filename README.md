# cbreakpoint

c-breakpoints in python-scripts

## Dependencies:

Essentials:

 - Python 3 (tested with Python 3.7)
 - c-build chain
    

Additional dependencies for tests:

 - sh
 - virtualenv

Instalation:

To install the module using pip run:

    pip install https://github.com/realead/cbreakpoint/zipball/master

It is possible to uninstall it afterwards via

    pip uninstall cbreakpoint

You can also install using the setup.py file from the root directory of the project:

    python setup.py install

However, deinstallation might fail (only manually) if setup.py was used directly.

## Usage


Take look at the following python script `tryout.py`:

    from cbreakpoint import cbreakpoint

    cbreakpoint(1)
    print("hello")
    cbreakpoint(2)

Now, breakpoints can be set as follows in gdb:

    >>> gdb --args python tryout.py
    [gdb] break cbreakpoint
    [gdb] run

now the program runs until `cbreakpoint(0)` and hits a breakpoint -> activate other breakpoints of interest.

    [gbd] c
    
gdb stops at `cbreakpoint(1)`.

It is also possible to stop only at `cbreakpoint(1)`, for that use:

    [gdb] break src/cbreakpoint.c:12 if breakpoint_id == 1

to get the cbreakpoint-line use `condition_line()` which return `12` in the current vesion.


## Versions:

  0.1.0: Proof of concept with help of Cython
  0.2.0: As C-extension without Cython dependency

## Outlook:

  * nothing
