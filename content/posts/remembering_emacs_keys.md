+++
title = "Remembering Emacs Keys"
author = ["Durham Smith"]
draft = false
+++

The key bindings have a few simple and easy to remember rules:

-   C-x prefix is for default and global binding that come with Emacs.
-   C-c prefix is for users to define.
-   C-u is for altering behaviors of commands. That is, one command can behave differently depending on how many C-u you pressed first before executing a command. Mostly you just have to hit C-u once.
-   C-<number> like C-1, C-2… is similar to C-u, but passing a number to a command. Usually, the number specifies how many times you want to repeat a command.

You will learn about C-u and C-<number> in Prefix Arguments section.

Most commands can be organized in an easy to remember way. For example, command like helm-do-grep (the command belongs to Helm, a 3rd party extension to Emacs) can have a key binding like C-c h g. The h stands for Helm and g stands for grep. So, key bindings are not difficult to remember.


## Refs: {#refs}

[Emacs keys are easy to remember](https://tuhdo.github.io/emacs-tutor.html#orgheadline18)
