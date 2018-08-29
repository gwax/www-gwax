Unsticking Stuck LCD Pixels (Redux)
===================================

:slug: unsticking-stuck-lcd-pixels-redux
:date: 2009-12-05 01:20:51+00:00
:updated: 2009-12-08 23:43:54+00:00
:tags: waksman

My previous article on `Unsticking Stuck LCD
Pixels </2006/01/03/unsticking-stuck-lcd-pixels/>`__ having been rather
a hit and having been asked for an alternate gif image, I figured I
should revisit the topic briefly.

The animated gif images were created with ImageMagick. Having long since
forgotten how I did it last time, I reacquainted myself with ImageMagick
and have developed this little one liner:

``convert -delay 20 -loop 0 -size 100x100 xc:#FF0000 xc:#00FF00 xc:#0000FF rgbanim.gif``

This command will generate an animated gif to use in attempting to fix
stuck pixels. Key parameters are:

Image size can be changed by changing the size parameter. ex.:
``-size 640x480``

Cycling speed can be varied by changing the delay parameter. ex.:
``-delay 7``

So, if my original images don't serve your purposes, go grab a copy of
`ImageMagick <http://www.imagemagick.org/>`__ and make one of your own.
(If I feel ambitious, I might hack together a script to auto-generate
these gif images)

**UPDATE:** Apparently, `I was sufficiently
ambitious </2009/12/08/unsticking-stuck-lcd-pixels-a-script/>`__.
