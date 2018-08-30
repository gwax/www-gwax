Fast, recursion depth safe, list flattening for Python
======================================================

:slug: fast-recursion-depth-safe-list-flattening-for-python
:date: 2011-03-01 02:10:01+00:00
:updated: 2011-03-02 00:48:38+00:00
:tags: progging

I've been using
`Python <http://en.wikipedia.org/wiki/Python_(programming_language)>`__
at work a lot recently (yeah, I know, took me long enough) and finding
it to be fantastically useful for all sorts of things.

Anyway, I found myself needing a mechanism for flattening nested
container objects and a quick google search led me to a `Right Foot In
article <http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html>`__
on various flatten algorithms. Seeing as I needed something to work on
containers that aren't tuples or lists and I'm not very good at leaving
well enough alone, I went about trying to come up with my own method.

Here's what I've got so far:

.. code:: python

   def flatten_to_list(something):
       if not hasattr(something, '__iter__'):
           return [something]
       retlist = list(something)
       i = 0
       while i < len(retlist):
           while hasattr(retlist[i], '__iter__'):
               if not retlist[i]:
                   retlist.pop(i)
                   i -= 1
               else:
                   retlist.insert(i, retlist[i].pop(0))
           i += 1
       return retlist

In at least one test case, my method appears to be faster than the best
method in the *Right Foot In* article. I'm still wrestling with
namespace issues relating to the use of **timeit** but I'll try to get
some actual speed numbers and test cases up later.

**UPDATE:** I am an idiot. My code was faster because my test case
exploited a degenerate case for the algorithm; the code below, which is
much closer to the original at *Right Foot In*, is faster.

.. code:: python

   def flatten_to_list(something):
       if not hasattr(something, '__iter__'):
           return [something]
       retlist = list(something)
       i = 0
       while i < len(retlist):
           while hasattr(retlist[i], '__iter__'):
               if not retlist[i]:
                   retlist.pop(i)
                   i -= 1
               else:
                   retlist[i:i + 1] = retlist[i]
           i += 1
       return retlist
