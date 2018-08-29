Unsticking Stuck LCD Pixels
===========================

:slug: unsticking-stuck-lcd-pixels
:date: 2006-01-03 16:17:35+00:00
:updated: 2009-12-27 06:43:36+00:00
:tags: computers

Sometimes the pixels on an LCD can become stuck, displaying only some
colors or appearing completely dead. These black or oddly colored spots
are a pain in the neck but they're not always permanent. At some point
last summer the Mac laptop I was working on got a stuck pixel and after
scouring the internet for information on how to fix such things I came
across instructions for fixing stuck pixels on the PSP that involved
playing a particular video file, containing RGB pulses, and massaging
the screen around the stuck pixel. The PSP technique worked
fantastically and in a few moments my screen was free of stuck pixels. I
have a similar problem on the machine I'm using right now but this
machine has no means of playing .mp4 files (which the PSP pixel fixing
video is) and rather than trying to figure out how to make it play .mp4
files, I thought I'd `ImageMagick <http://www.imagemagick.org/>`__
myself up a quick solution. To that end, I created three animated gifs
that pulse at different frequencies (`rgb3.gif </pics/rgb3.gif>`__,
`rgb5.gif </pics/rgb5.gif>`__ and `rgb7.gif </pics/rgb7.gif>`__), which
serve the same purpose as the video and are substantially smaller in
size (1.2KB vs 1.5MB). The great thing about these is they're
essentially platform independant and require no video codecs at all. To
fix your dead pixels, just fire up a graphical web browser, point
yourself at one of the images, move the browser window so that the image
is under your dead pixel, massage the screen a little and with luck the
pixel may start working again. If you don't have any luck try one of the
other frequencies and if that doesn't work, I'm sorry.

**UPDATE:** If you're here, you might be interested in `Unsticking Stuck
LCD Pixels: A
Script <http://blog.gwax.com/2009/12/08/unsticking-stuck-lcd-pixels-a-script/>`__
