+++
title = "Braindumps"
author = ["John Doe"]
draft = false
+++

tags
: [Note Taking](note_taking.md) [Evergreen Notes](Evergreen/evergreen_notes.md)

keywords
:


## Braindumps {#braindumps}

Braindump$ are a means to display data about knowledge base (full [Life Management System](life_management_system.md)) in a way that is meant to be explored by the end user (person or machine) that is not (necesarily?) the means of using .

This does not need to be limited to a current snapshot to retrive information like a note explorer, it could also be visualisation like a graph or a way to show how notes are added across time and space.


### Creating A Braindump {#creating-a-braindump}

-   Inspiration
    -   <https://notes.andymatuschak.org/About%5Fthese%5Fnotes> is a great example of easy and useful exploration
        -   He seems to use <https://bear.app/> to do it
    -   [Azlen Elza](People/azlen_elza.md) made his own port or [Andy Matuschak](People/andy_matuschak.md)s notes, from what seems to be using [Roam Research](roam_research.md) as a backend
    -   [Jethro Kuan](People/jethro_kuan.md) then wrote an exporter that can take org-mode file and turn them into a webpage like [Andy Matuschak](People/andy_matuschak.md)s notes page.
-   Steps
    -   Make a folder to keep braindump generating code
        -   Code is cloned from <https://github.com/jethrokuan/braindump>
        -   I chose `~/org/braindump`
    -   In the clone codes `build.py` file modify
        -   the line that sets `files` so that it points to the directory of your notes, for me this is the same as my `org-roam-directory` since I use [org-roam](org_roam.md) to track [Backlinks](backlinks.md) and have a flat folder heirarchy.
            -   `files = glob.glob("/home/dd/org/Notes/*.org")`
        -   The line that sets the output path of the markdown files that braindump generators org2md step generates.
            -   It expects it in the /content/posts directory (?from hugos base directory | from where we generate the braindump) from the directory we created is step 1
            -   `output_file = f"/home/dd/org/braindump/content/posts/{path.with_suffix('.md').name}"}`
    -   Make sure all .org files that will be pared by the md generator have their `HUGO_BASE_DIR` set, else you will get error
        -   Put `#+HUGO_BASE_DIR: ~/org/braindump` at the top of your file, where `~/org/braindump` is the directory from step 1.
    -   Parse the orgfiles and generate the markdown files
        -   `python build.py`
    -   Generate the website
        -   `hugo`
        -   And serve the in `hugo serve`
    -   Deploy the website
        -   <https://gohugo.io/hosting-and-deployment/hugo-deploy/>
        -   Amplify is better?
            -   Just needs gitrepo, will do setup and CI
            -   <https://gohugo.io/hosting-and-deployment/hosting-on-aws-amplify/>


### Scratch Thoughts {#scratch-thoughts}

-   git is an example of a braindump that displays temporal information, although it is close to how you normally use it when reverting or rebasing (these open new avenues of interactions with knowledge based on the time scale that isnt viewing). The GUI/viz for git as a braindump is not good.
