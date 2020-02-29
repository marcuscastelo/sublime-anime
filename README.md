# Sublime Anime

A package that contains a syntax and a plugin to help me write my anime watch list.
Probably this project will not be useful to anyone besides me, but i'll make a readme just in case there's another freak like me searching for this.

## Problem

I've been writing my episode watchtimes for a long time, and as almost all mechanical processess, it would eventually be automated. So that's what I did. \
List record example:

![list example](https://i.imgur.com/NNfN6ui.png)

## Solution

### Syntax Highlight

You may have noticed in the image above i'm already showing the syntax highliting in usage. Also, I'm too lazy to fix this presentation order issue. So, that's it, Syntax Highlighting,

### Dynamic Autocompletions and Shortcuts (Plugin)

![plugin demonstration](https://im2.ezgif.com/tmp/ezgif-2-911c15c266a3.gif)

The gifs demonstrates autocompletion for anime titles and friend names, but also some shortcuts, as below:

* Alt + D -> "{dd/mm/yyyy}\n\n"
* Alt + T -> "{hh:MM}" and a aditional " - " if it's the starting time
* Alt + L -> Writes "{last episode+1}" Filling left zeros for 1-digit (eg. 9 -> 09, but 15 -> 15)

## Other

Alt + S copies the last anime title... not so useful. \
There is also a syntax highlight for "[SOME-TEXT]" representing tags, a not well defined concept. \
I plan on using tags like [REWATCH], [NOT-IN-MAL] for another project later.
