Safe offline ext2/ext3/ext4 defragmentation
===========================================

:slug: safe-offline-ext2ext3ext4-defragmentation
:date: 2010-06-07 19:14:40+00:00
:updated: 2010-12-05 21:07:02+00:00
:tags: computers

I have a very large RAID6 array (11TB) with an ext4 partition that, due
to particular use cases, has become disgustingly fragmented (~40%
non-contiguous according to ``fsck``). Sadly, as much as ext4 is
designed to resist fragmentation issues, my partition has been having
substantial performance issues.

The ext4 defrag program ``e4defrag`` would be an ideal solution to my
problems but it is not yet stable enough for production use.

Putting some thought into the matter, I have came up with a technique
for defragmenting my partition using only stable tools. My process is
very slow and requires substantial periods of downtime but preliminary
results are good.

At present, I have 2TB of free space, which means that I can copy files
off my fragmented partition and then copy them back to decrease the
fragmentation of individual files; alternatively, the application
``shake`` can be used to accomplish a similar result. However, the
copy/recopy solution will only work if the free space on my partition is
not fragmented. Running ``e2freefrag`` I found that the free space on my
partition is monstrously fragmented.

However, clever use of ``resize2fs`` can almost completely defragment
the free space of a partition. If you unmount the partition, shrink it
to a minimum size and the expand it, the vast majority of the free space
will be moved to a contiguous region at the end of the partition.

If the partition is ``/dev/md1`` and is mounted at ``/mnt/fragmented``, your
file system can be defragmented with the following set of commands:

.. code:: sh

    $ umount /mnt/fragmented
    $ fsck -f /dev/md1
    $ resize2fs -M -p /dev/md1
    $ resize2fs -p /dev/md1
    $ mount /dev/md1 /mnt/fragmented
    $ shake -o 0 -S 0 /mnt/fragmented

This will result in some defragmentation of your partition but it is
likely that the process will need to be repeated multiple times to
achieve a substantial degree of defragmentation.
