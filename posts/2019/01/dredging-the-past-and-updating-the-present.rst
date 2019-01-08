Dredging the past and updating the present
==========================================

:slug: dredging-the-past-and-updating-the-present
:date: 2019-01-08 07:54:13+00:00
:tags: nikola, meta
:category: meta

A few months ago, while digging around my gargage, I found an old server of
mine. I was looking for a particular bit of old data that I couldn't find on
my current computer and thought it might be on this one. It didn't have what
I was looking for but it did have a bunch of content from my old blog, going
back to 2004.

It was a really old computer that wasn't cared for after I moved stuff to the
cloud and the hard drives started failing reads almost as soon as I looked at
the thing. However, with some running `dd`_ and a lot of finger-crossing, I
was able to pull out a backup of the old blog. The backup, annoyingly, was
a MySQL dump of a Wordpress page. After trying a handful of text based
approaches and a couple of automated approaches, I figured I might as well
install MySQL, load the dump into the database and hack together some one-off
code to rip things out in a format that I liked.

.. _dd: http://man7.org/linux/man-pages/man1/dd.1.html

The data extraction code isn't pretty but it gets the job done:

.. TEASER_END

.. listing:: gen_olddata.py python

From there, I had a lot of cleanup work to do and some images to track down
and copy over. Then there was some early-20s angst to remove.

Of course, that got me updating things and finding little problems with the
display and layout of things. One thing led to another and I've ended up
sinking a bunch of time into tiny content and style guide tweaks.
