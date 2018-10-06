author: rameez
date: 01 september 2018

This code has been developed on Debian Stretch and assumes that system uses LXterminal as shell terminal.
If your system  doesn't have LXterminal please install it with 'aptitude' tool.
instead you can use other terminal also by making change in c program's command.

This code makes use of standard C library i.e. unistd.h,string.h and stdlib.h hence no need to install or include any user defined library.

test.c file contains the code and a.out contains compiled output.
just run a.out and it will open a separate window to display the data coming form USB port.
to send data to USB the existing terminal can be used.

to terminate the program, terminate the parent process carefully along with its forked process by yourself.
because no extra preventive measure is taken to kill forked processes.
