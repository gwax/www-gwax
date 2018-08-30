Unsticking Stuck LCD Pixels: A Script
=====================================

:slug: unsticking-stuck-lcd-pixels-a-script
:date: 2009-12-08 23:41:54+00:00
:updated: 2011-03-01 00:45:39+00:00
:tags: progging

As I `just recently </2009/12/04/unsticking-stuck-lcd-pixels-redux/>`__
suggested I might do, I have made a script for automatically generating
color cycling animations of arbitrary sizes and speeds.

The script can be used at:
`http://blog.gwax.com/files/rgbanim.php </files/rgbanim.php>`__

The script accepts the parameters height, width, and delay, so it can
also be used in more interesting ways. Feel free to play around (if you
crash it, let me know).

Ex.:
`http://blog.gwax.com/files/rgbanim.php?width=100&height=100&delay=7 </files/rgbanim.php?width=100&height=100&delay=7>`__

Or, better still:

::

    - Width
    - Height
    - Delay

For the curious amongst you, the relatively simple code follows:

.. code:: php

   <?php
   if(isset($_GET['delay']) && is_numeric($_GET['delay']))
       $delay = max((int)$_GET['delay'], 1);
   else
       $delay = 10;if(isset($_GET['width']) && is_numeric($_GET['width']))
       $width = max(min((int)$_GET['width'], 1920), 1);
   else
       $width = 320;if(isset($_GET['height']) && is_numeric($_GET['height']))
       $height = max(min((int)$_GET['height'], 1080), 1);
   else
       $height = 240;$out = new Imagick();
   $out->newImage($width, $height, '#FF0000', 'gif');
   $out->setImageDelay($delay);
   $out->newImage($width, $height, '#00FF00', 'gif');
   $out->setImageDelay($delay);
   $out->newImage($width, $height, '#0000FF', 'gif');
   $out->setImageDelay($delay);header('Content-type: image/gif');
   echo $out->getImagesBlob();
   ?>
