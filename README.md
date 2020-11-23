# Sublime Anime

A package for **Sublime Text 3** that contains a syntax and a plugin to help me write my anime watch list.
Probably this project will not be useful to anyone besides me, but i'll make a readme just in case there's another freak like me searching for this.

## Installation

Go to Sublime Text 3 `Packages` folder and clone this repo as a folder with any name. Inside this new folder there will be another folder named *"PUT IN USER PACKAGE"*. Copy its content to `Packages/User` \
**WARNING: this will override all your previous custom settings, if you wish to keep them, edit the files and merge manually**

Depending on your installation and operating system, the *Package* folder might be in a different path, usually on linux it's located at `~/.config/sublime-text-3/Packages/`

## Problem

I've been writing my episode watchtimes for a long time, and as almost all mechanical processes, it would eventually be automated. So that's what I did. \
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
