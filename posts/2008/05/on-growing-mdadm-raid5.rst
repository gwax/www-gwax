On growing mdadm RAID5
======================

:slug: on-growing-mdadm-raid5
:date: 2008-05-29 00:03:57+00:00
:updated: 2008-05-29 00:05:07+00:00
:tags: computers

There is a right way and there are wrong ways to add drives to a RAID5
array with mdadm. Annoyingly, I chose one of the wrong ways last week
when I went to increase the hard drive space in thevoid. Thankfully, my
mistake has proven more bothersome and time consuming than harmful.

Starting out last week, thevoid had 4x 500GB drives in an mdadm RAID5
configuration: /dev/hde1, /dev/hdg1, /dev/sda1, /dev/sdb1. This had me
sitting on 1.5TB of space with one drive worth of failability, which was
proving insufficient. In order to resolve my space issues, I ordered 3x
500GB drives and proceeded to install them when the arrived: /dev/hdb,
/dev/hdc, /dev/hdd.

In my haste to have more space, I proceeded to add them to the array and
grow it:

.. code:: sh

    mdadm --manage /dev/md1 --add /dev/hdb
    mdadm --manage /dev/md1 --add /dev/hdc
    mdadm --manage /dev/md1 --add /dev/hdd
    mdadm --grow /dev/md1 --raid-devices=7

This process then got to work and took about 3-4 days to complete. I
assume the time was on account of most of the drives being IDE drives,
many sharing channels and there being an awful lot of space. Once the
growing process was complete, I merely needed to resize the ext3
partition on the array:

.. code:: sh

    resize2fs /dev/md1

This then took an hour or so and I was sitting on 3TB of total space.
The only part of the process during which my drive was inaccessible was
when I had to turn off the computer to physically install my IDE drives.

Everything is perfect now, right? Wrong. Guess who forgot that you
should partition drives before using them? That's right, me. I really
wanted to put a linux raid autodetect partition on each of the drives
before adding them to the array. Not that it really does much harm to
add the drives straight to the array but it's poor form and it might
pose problems that I am not aware of in the future so, clearly, it's a
thing that should be fixed. Thankfully, being RAID5, my array is able to
lose drives and still be fine, thus allowing the solution of failing,
removing, partitioning and adding each of the new drives back into the
array:

.. code:: sh

    mdadm --manage /dev/md1 --fail /dev/hdb
    mdadm --manage /dev/md1 --remove /dev/hdb

partition /dev/hdb and then:

.. code:: sh

    mdadm --manage /dev/md1 --add /dev/hdb1

now wait until the array has rebuilt itself:

.. code:: sh

    cat /proc/mdstat

and repeat for the other drives. Overall, it's not hard but it's
annoying and it does take about 1/2 to 2/3 of a day per drive to fix.
Thankfully, though, now the endeavor is done and my array works
correctly with no lost data and minimal down time. Hooray for software
RAID and having 3TB in a single place.

Oh, and you don't want to forget to update /etc/mdadm.conf after every
step of the process of you could have some potential problems.
