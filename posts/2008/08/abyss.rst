Abyss
=====

:slug: abyss
:date: 2008-08-18 18:08:28+00:00
:tags: computers

I have finally decided, after 7 years of faithful service, that thevoid
is due for decommissioning as my primary desktop. I love thevoid, she's
a great machine but at a 1.8GHz single core, 1GB of RAM, no USB2, no
SATA, no PCI-E, no PCI-X and fans that are starting to make
squealing/grinding noises, she's fallen a little far behind the
technology curve. My general view on desktops is, and for a long time
has been, to get a core setup with the most expandability possible and
then incrementally upgrade for as long as possible; following that
principle, I am replacing thevoid with abyss.

Abyss (current specs)

-  Lian-Li PC-A77B case
-  Tyan Tempest i5400PW (S5397) motherboard
-  2x Intel Xeon E5420 2.5GHz quad core CPUs
-  4x Kingston 1GB 667MHz FB-DIMM RAM
-  2x Western Digital 500GB SATA HD
-  Lite-On SATA 20X DVD±R

Abyss (planned upgrades) (as funds are available)

-  4x Kingston 1GB 667MHz FB-DIMM RAM
-  Some medium-to-high-end nVIDIA video card
-  some medium-end multi-channel sound card
-  Highpoint RocketRAID2240 16-channel SATA controller
-  3x Icy Dock 5-bay SATA backplane
-  15x 750GB HD

The hardware in abyss has been specifically chosen to have support for
Intel `VT-x and
VT-d <http://en.wikipedia.org/wiki/X86_virtualization#Intel_Virtualization_Technology_.28Intel_VT.29>`__
virtualization technology so as to allow for as versatile a machine as
possible. Abyss is already running
`Xen <http://en.wikipedia.org/wiki/Xen>`__ with `Gentoo
Linux <http://en.wikipedia.org/wiki/Gentoo_Linux>`__ as the primary,
dom0, operating system and Windows XP as a secondary, domU, operating
system. My hope, after adding a video and sound card, is to install
another Gentoo Linux and Windows XP operating system, as well as a
Windows Vista operating system. Ultimately, the current Gentoo and
Windows operating systems will always run in the background, primarily
acting as headless servers for underlying services, and for day to day
usage I will be able to switch between Gentoo, XP and Vista domains
based on my needs. In essence, I will have a dual-booting system of
virtual hosts with direct access to my video and audio hardware.

Hopefully abyss, with some incremental upgrades, will serve my
computation needs for the next five to ten years.
