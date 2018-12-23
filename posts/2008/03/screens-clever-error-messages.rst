Screen's Clever Error Messages
==============================

:slug: screens-clever-error-messages
:date: 2008-03-27 00:57:53+00:00
:updated: 2008-03-27 01:00:17+00:00
:tags: computers

I am--and have for quite a while been--a huge proponent of `GNU
Screen <http://www.gnu.org/software/screen/>`__ for the many-fold
improvements that it provides to terminal and SSH sessions. One of the
things about screen is that it runs in two processes, one is a headless
process that redirects terminal output of applications to it (server
process) and the other is a process which connects to the server process
allowing interaction with and the viewing of output from applications in
the server process (client process). The advantage to this two process
approach is that you can run screen from an SSH connection, disconnect
the client process, leave and then later reconnect a new client process
to the same server process you started earlier, thus allowing session
persistence. It's a wonderful application with many other features that
make my life easier.

In addition to being fantastically useful, screen appears to have been
written by someone with a sense of humor as it seems to contain rather a
few Easter Eggs. One particular Easter Egg that I recently came across
is that if the server process dies while the client process is still
connected, you meet the error message:

    Suddenly the Dungeon collapses!! - You die...

It's a cryptic and ominous error message that might put you off a little
if you don't know what's going on. A quick
`googling <http://www.google.com/search?q=Suddenly+the+Dungeon+collapses%21%21+-+You+die...>`__
will show that some have accidentally misinterpreted the meaning;
thankfully I could guess what it was and check google for confirmation.
