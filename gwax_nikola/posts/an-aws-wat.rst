.. title: An AWS wat?!
.. slug: an-aws-wat
.. date: 2016-04-05 23:59:01+00:00
.. tags: code snippets, wat
.. category: rumblings
.. link: 
.. description: 
.. type: text

tl;dr different AWS regions have different APIs.

I've been using AWS via `boto3 <http://boto3.readthedocs.org/en/latest/>`_ a
bunch lately and testing can be a bit of a pain. To my great joy, there turns
out to be a mock aws implementation: `moto <https://github.com/spulec/moto>`_.

Moto support for boto is pretty good but support for boto3 is still a bit of a
work in progress. In testing, I was finding a lot of functionality to be
broken, in spite of it working for other people. Through some poking and
digging, I discovered that the failures depended on the region.

Here's a chunk of test code that illustrates the issue:

.. listing:: test_moto_boto3_regions.py python

Punchline: A call to "py.test test_moto_boto3_regions.py" gives:

::

    test_moto_boto3_regions.py .FFF.F.FFF

    ====================== 7 failed, 3 passed in 0.97 seconds ======================

Why the heck are the api calls of boto3 dependent on the region being called?
