Ultimate Xbox 360 Transcoding solution
======================================

:slug: ultimate-xbox-360-transcoding-solution
:date: 2007-01-29 02:31:15+00:00
:tags: video games

About a week ago, I finally caved and bought myself an Xbox 360. Along
with some really great games (ex. Gears of War) the 360 is also a
powerhouse of media playing capabilities. Using Microsoft `provided
software <http://www.xbox.com/pcsetup>`__ you can set up your PC to
serve media over the network to your 360. This means that you can listen
to your entire music collection while you play you games (solves the
only problem with Geometry Wars, the mediocre soundtrack); the 360
natively plays mp3s so you don't need to do much of anything to make
music work. Unfortunately, the 360 will only natively play wmv video
files, and only ones that are properly formatted, which means that
you'll have to do a bit of work to watch and DivX, Xvid or, for that
matter, just about anything else that you didn't get from Microsoft to
begin with. Playing my video files on my TV through my 360 is an
important thing for me, so set about scouring the internet to figure out
how to do this and, having done so, I now report to you on what I have
found.

If you're running Vista or XP MCE, it's supposedly a lot easier but,
since I have neither, you're on your own and I cannot help. Supposedly,
it's possible to use `TVersity <http://www.tversity.com>`__ on a regular
XP machine to do real-time on-the-fly transcoding of your files into wmv
but I was not able to make it work. It may be the case that my computer
is not powerful enough for on-the-fly transcoding or it might be that I
had it set up wrong but the simple fact of the matter is that, in my
opinion, TVersity is pretty flaky and doesn't provide a very good
network interface when you access it through the 360. Using Microsoft's
software and manually transcoding files before I watch them is thus my
option of choice for watching movies and listening to music on my 360.
This brings us to the real meat of this post, how to best transcode
files for playing on the 360.

I tried a whole bunch of transcoding options, none of which worked,
before I came across `Encode360 <http://dcunningham.net/encode360/>`__.
Encode360 encodes things perfectly and allows for the vital rescaling
(more on this later) but suffers from two problems: it's slow and it
crashes a lot. A little more digging turned up that some had `figured
out <http://happybeggar.com/index.php?option=com_content&task=view&id=63&Itemid=2>`__
how to use `VLC media player <http://www.videolan.org>`__ to perform the
transcodes. I tried the VLC transcoding method and discovered that it
was both very fast and encoded perfectly. Unfortunately, the batch files
provided for this purpose don't do rescaling and have a number of other
problems. The rescaling is vital because if you don't scale your file
properly, the 360 will auto-scale to fit the TV and the 360's
auto-scaling is terrible, leaving blocky artifacts all over the screen.
In order to deal with the 360's scaling issues and some of the other
problems of the provided batch files, I read through VLC's documentation
and fiddled around a bunch and am proud to say that I have come up with
a few new batch files for VLC that will process video files and make
them work properly on your 360.

Go get your hands on a copy of `VLC media
player <http://www.videolan.org/vlc>`__ and then grab the batch files I
have made
(`vlc2xbox480h.bat <http://www.gwax.com/content/xbox-transcode/vlc2xbox480h.bat>`__
and
`vlc2xbox720w.bat <http://www.gwax.com/content/xbox-transcode/vlc2xbox720w.bat>`__).
You will need to modify the batch files slightly for your system; open
the file in a text editor and change the very beginning to point to
where you have installed VLC ("C:\program files\vlc\vlc.exe" is where
mine is, change this if you need to). In order to transcode a file, you
will drag-and-drop the file that you want to transcode onto one of these
batch files, depending on the files aspect ratio. If the files aspect
ratio is less than 16:9, drop it on the 480h file; if the aspect ratio
is greater than 16:9, drop it on the 720w files; if the aspect ratio is
16:9, drop it on either one. It is important to note that your file's
filename cannot have any single quotes (') or it will cause problems. So
there you have it, the best way that I've found to transcode files into
a 360 ready format. I might improve the batch files later or I might try
writing a wrapper application at some point and, if I do, I'll post
those updates here.
