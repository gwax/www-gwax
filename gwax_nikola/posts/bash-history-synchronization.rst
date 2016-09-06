.. title: Bash history synchronization
.. slug: bash-history-synchronization
.. date: 2016-09-06 08:05:13+00:00
.. tags: code snippets, bash
.. category: rumblings
.. link:
.. description:
.. type: text

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

.. code:: bash

    export HISTSIZE="INFINITE"
    export HISTFILESIZE="INFINITE"
    shopt -s histappend
    shopt -s cmdhist
    alias histsync='history -a && history -c && history -r && history | sort -k2 -k1nr | uniq -f1 | sort -n | tr -s " " | cut -d " " -f3- > ~/.tmp$$ && history -c && history -r ~/.tmp$$ && history -w && rm ~/.tmp$$'
    export PROMPT_COMMAND="${PROMPT_COMMAND:+$PROMPT_COMMAND$'\n'}histsync"

.. TEASER_END

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
