Bash history synchronization
============================

:slug: bash-history-synchronization
:date: 2016-09-06 08:05:13+00:00
:updated: 2018-04-20T07:55:00.339805+00:00
:guid: 42d5ffed-0b3a-49c9-b234-f55b711ea91d
:tags: code snippets, bash
:category: rumblings

Bash is my go to shell. I've tried fish; I've heard about zsh; but Bash is my
go to.

I really like command history (pressing up arrow or Ctrl+R) and there are a
few specific behaviors that I want in my history:

1. If I have multiple terminals open, I want history shared across them.
2. If I run the same command multiple times, it should be in my history once.
3. My history should stick around forever.
4. The last command, I entered should be the first thing I see when I press
   up arrow.
5. Race conditions of long-running commands shouldn't erase history entries.

Turns out all of this is a little tricky with bash, but I've mostly managed it:

.. TEASER_END

Updated: 2018-04-20
-------------------

I've been finding cases where my original solution lost commands, which is
very not good in my book. As such, I've reverted back to a simpler, safer,
synchronization scheme that doesn't always get the order right but seems to
lose stuff less often:

.. code:: bash

    export HISTCONTROL=ignoredups:erasedups
    export HISTSIZE=100000
    export HISTFILESIZE=100000
    shopt -s extglob
    shopt -s histappend
    export PROMPT_COMMAND="history -n; history -w; history -c; history -r; $PROMPT_COMMAND"

Original
--------

.. code:: bash

    export HISTSIZE="INFINITE"
    export HISTFILESIZE="INFINITE"
    shopt -s histappend
    shopt -s cmdhist
    alias histsync='history -a && history -c && history -r && history | sort -k2 -k1nr | uniq -f1 | sort -n | tr -s " " | cut -d " " -f3- > ~/.tmp$$ && history -c && history -r ~/.tmp$$ && history -w && rm ~/.tmp$$'
    export PROMPT_COMMAND="${PROMPT_COMMAND:+$PROMPT_COMMAND$'\n'}histsync"

Here's how it (mostly) works:

First we just set up some basic configuration:

1. Keep all of history forever

    .. code:: bash

        export HISTSIZE="INFINITE"
        export HISTFILESIZE="INFINITE"

2. Append history instead of overwriting

    .. code:: bash

        shopt -s histappend

3. Store multi-line commands as a single history entry

    .. code:: bash

        shopt -s cmdhist

4. Create a command that synchronizes history:

   a. Append anything new to the history file, clear and reread

        .. code:: bash

            history -a && history -c && history -r

   b. Get the history, sorted by when things were added with duplicates removed

        .. code:: bash

            history | sort -k2 -k1nr | uniq -f1 | sort -n | tr -s " " | cut -d " " -f3-

   c. Write to temp file, clear history, read from temp file, write to
      ~/.bash_history, remove temp file

        .. code:: bash

            > ~/.tmp$$ && history -c && history -r ~/.tmp$$ && history -w && rm ~/.tmp$$

5. Use the sync command as a part of the PROMPT_COMMAND

    .. code:: bash

        export PROMPT_COMMAND="${PROMPT_COMMAND:+$PROMPT_COMMAND$'\n'}histsync"

There might be better ways, but it works.

P.S. I keep my `.bashrc on GitHub <https://github.com/gwax/dotfiles/blob/master/bashrc>`__
(along with the rest of my core dotfiles).
