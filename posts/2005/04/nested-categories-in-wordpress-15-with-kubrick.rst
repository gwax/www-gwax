Nested Categories in Wordpress 1.5 with Kubrick
===============================================

:slug: nested-categories-in-wordpress-15-with-kubrick
:date: 2005-04-19 17:56:24+00:00
:updated: 2005-04-19 19:12:39+00:00
:tags: blogs

After upgrading to Wordpress 1.5, I spent a rather long time hunting
through documentation trying to figure out how to display my categories
in a nested fashion. It turns out to be the case that all of the
documentation is a little out of date with regards to the wp_list_cats
and list_cats functions; to that end, here is how you can make nested
categories in Wordpress 1.5:

In wp-content/themes/{yourtheme}/sidebar.php change this:

.. code:: php

   <li><h2><?php _e('Categories'); ?></h2>
       <ul>
       <?php list_cats(0, '', 'name', 'asc', '',
   1, 0, 1, 0, 1, 1, 0,'','','','','') ?>
       </ul>
   </li>

to this

.. code:: php

   <li><h2><?php _e('Categories'); ?></h2>
       <ul>
       <?php list_cats(0, '', 'name', 'asc', '',
   1, 0, 1, 0, 1, 1, 0,'','','','','', 1) ?>
       </ul>
   </li>

Note the additional 1 in the list_cats call, this corresponds to
hierarchical=1 for wp_list_cats; the hierarchical option is not listed
in documentation as of right now but can be found by rummaging through
the code.
