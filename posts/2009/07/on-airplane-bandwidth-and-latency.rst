On airplane bandwidth and latency
=================================

:slug: on-airplane-bandwidth-and-latency
:date: 2009-07-03 00:21:27+00:00
:tags: computers, intzorweb

Having recently used Virgin America to transport myself across the
country, I was very pleased to have Internet access while I was in the
air. This, however, is not the sort of airplane bandwidth and latency
that I am going to talk about. Instead, I would like to discuss a
comparison between the bandwidth and latency of typical Internet
connections with those associated with taking a hard drive on an
airplane.

Let's say we compare a high speed (15Mbit) DSL connection to taking a
moderately large hard drive (500GB) on a plane for data rates between
San Francisco and Boston (~7 hours):

Bandwidth: DSL: 15 Mbit/s Airplane: [pmath] {{500 GB} / {7 hr}} \* {{1
hr} / {60 min}} \* {{1 min} / {60 s}} \*{{8000 Mb} / {1 GB}} approx
[/pmath] 150 Mbit/s

Latency: DSL: ~100ms Airplane: >7 hours

For fun, let's try something a little bigger on both sides: OC-768 vs
Boeing 747-400F plane filled with 2TB hard drives.

Bandwidth: OC-768: 38 Gbit/s 747-400F: [pmath] {{250,000 lbs} / {7 hr}}
\* {{2 TB} / {1.7 lbs}} \* {{1 hr} / {60 min}} \* {{1 min} / {60 s}}
\*{{8 Tb} / {1 TB}} approx [/pmath] 93 Tbit/s

Latency: OC-768: <100ms 747-400F: >7 hours

Clearly, hard drives on an airplane will win in a purely bandwidth
driven application but airplanes suffer from incredibly high latency.
You will have to decide which is best choice based on your particular
use scenario.
