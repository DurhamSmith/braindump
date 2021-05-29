+++
title = "ENSnano2021: Ensnano: a 3d modeling software for dna nanostructures"
author = ["John Doe"]
draft = false
+++

tags
:


keywords
:


## Ensnano: a 3d modeling software for dna nanostructures {#ENSnano2021}


#### Notes {#notes}


#### The 4 feature they say DNA Design tools should have {#the-4-feature-they-say-dna-design-tools-should-have}

Various softwares have been developed to help the designer. These softwares provide essentially four kind of tools:

-   an abstract representation of DNA helices (e.g. cadnano, scadnano, DNApen, 3DNA, Hex-tiles)
-   a 3D view of the design (e.g.,vHelix, Adenita, oxDNAviewer);
-   fully automated design generally dedicated to a specific kind of design, such as wireframe origami (e.g., BScOR, Daedalus, Perdix, Talos, Athena),
-   coarse grain or thermodynamical physics simulations (e.g., oxDNA, MrDNA, SNUPI, Nupack, ViennaRNA,...).

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  I don't think these capture the essential of what's needed for a CAD tool.


#### Their Aim: {#their-aim}

We present our first step in the direction of conciliating all these different approaches  and   purposes into one single reliable GUI solution


#### Novel Contributions {#novel-contributions}

Our software extends the concept ofgrids introduced in cadnano. Grids allow to abstract and articulated the different parts of a design.

    ENSnano also provides new design tools which speeds up considerably the design of complex large 3D
structures, most notably:

-   a 2D split view, which allows to edit intricate 3D structures which cannot easily be mapped in a 2D view
-   and a copy, paste & repeat functionality, which takes advantage of the grids to design swiftly large repetitive chunks of a structure.

    "Our contribution. In this paper, we present our software ENSnano which introduces a 3D
editable view working together with a (s)cadnano-like 2D view. As in cadnano, our helices are
attached to grids organizing the helices, next to each other, in parallel subsets. We extend
this grid concept in three ways:

-   first, the grids are now freely and precisely placed and oriented in space in the 3D view;
-   second, grids can be any 1D or 2D lattice, for now: the classic square and hexagonal grids, but also circular lattices to design nanotubes;
-   third, we take advantage of this lattice structure to introduce a geometry-aware copy-

fpaste-&-repeat process, which allows to build in the blink of a eye a complete set of
staples by duplicating repetitively the selected pattern (a subset of strands or crossovers)
according to the initial translation, along the helices and across the grid lattice, of the
firstly pasted copy (see Fig 9 in Section 3.4). Note that this process is geometry-based
and works regardless of the numbering of the helices.

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  Is Copy paste and repeat different than scadnanos copy and paste?


#### Features {#features}

-   GUI, with 2D and 3D editable views,
-   handles editing of large 2D/3D structures smoothly
-   and imports from the most common solutions.

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  Check if they specify what large 2D/3D structures are and what specs they have


#### List of features of interest found in current software {#list-of-features-of-interest-found-in-current-software}

-   High-level description
-   Live (editable) 3D view
-   Fine tuning and editing
-   Design versatility
-   Automation
-   Programmable designs
-   Simulation
-   Intuitive fast-responding interface
-   Reliability
-   Distribution
-


#### ENSnano concepts {#ensnano-concepts}

-   2D and 3D editable views
-   Grids
-   Group-based organization of the design
-   Design Helpers
-   Crossover suggestions
-   Crossover length color shading
-   Helices (auto)roll.


#### Sequence Optimization {#sequence-optimization}

"When asked to optimize, ENSnano tries to minimize
the risk of error in the strand synthesis, by finding the position that minimizes the number
of problematic patterns such as C n⩾4 , G n⩾4 or (A|T ) n⩾7 . The higher the n, the heavier
the weight of the problem. Once optimized, ENSnano reports on the number of remaining
problematic patterns as shown in Fig. A.4. This position is retained and saved for later reuse.
This optimization phase allows usually to avoid any C 5+ or G 5+ pattern in no time."


#### Scratch Notes {#scratch-notes}

-   "DNA geometry is very peculiar and hard to grasp."

-   3D→2D parallax effect reference

-   "Rotating the array representations as in [38, 7] allows an even more convenient rendering of the design"
    -   What did they do here?

-   Missing Refs? "oarse grain or thermodynamic physics simulation, e.g.: oxDNA [9], MrDNA [24], Snupi [21], Nupack [37], ViennaRNA [23],..."

-   "As a thumb rule, untyped programming languages should thus be ruled out to develop reliable design

softwares."

-   Figure 1 needs a better caption and size

Merge fig 1 and 2?

-   Fig 2b needs better color display if

-   File format, import and export: bad language

-   "Grids are internally implemented as a mapping Z 2 7→ R 2 . This flexible representation makes it easy to add new grid types in the future, and could be easily extended to arbitrary Cayley graphs."

<!--listend-->

-   "ENSnano is, for now, “DNA origami-oriented” (this will change in the future)."


#### Quotes useful to me {#quotes-useful-to-me}

    "Fine tuning and editing: As mentioned above, 3D views are not well adapted for editing or
fine tuning [12], especially when the 3D view is provided by a “mother” software (Matlab,
Maya, or Samson) which was not designed for the specific needs of DNA nanostructures.
As it turns out, almost all the softwares, including the all-automated ones, e.g. [15],
recommend to export to (s)cadnano for checking and fine tuning their designs. As a
matter of fact, the 2D representation of a helix as a double array, initially proposed in
cadnano, remains the most practical for editing"

". In spite of its imperfection in terms of DNA geometry (incorrect turn/bp [34] and absence of roll of helices), cadnano is still the reference for fine tuning a design."

"Few of them allow to edit various types. Even fewer of them provide an abstraction for dealing with all of them, e.g.: MagicDNA [15]" proposes a common framework for classic and wireframe DNA origami. The most versatile remain (s)cadnano, which allows indifferently any type of designs, but provides almost no specific automation."

    "Automation: When designing a DNA origami, many tasks are repetitive and dull, such
as “stapling” a rectangle. On the opposite, some tasks require a high technical level, such
as routing a scaffold in a wireframe design, or designing 3D staples in a 3D bulk. Both of
these types of tasks befenit a lot from automation. Algorithms have been designed to
complete these tasks and designers can save a lot of time and avoid mistakes by using
them, e.g. [4, 33, 16, 15]."

   Fei Zhang, Shuoxing Jiang, Siyu Wu, Yulin Li, Chengde Mao, Yan Liu, and Hao Yan.
Complex wireframe DNA origami nanostructures with multi-arm junction vertices. Nature
Nanotechnology, 10(9):779–784, 2015. <10.1038/nnano.2015.162>.

   "In ENSnano, we propose to give up on dependable physics simulations of the resulting shape of a
design, but just to focus on its immediate stability. Indeed, the commonly accepted motto of
DNA nanostructures design is that DNA helices can be abstracted as rigid shapes (cylinder
or curves) if correctly tied up together. Dependable physics engines are used to check the
correctness of this assumption."


## Peer Review {#peer-review}


### Instructions {#instructions}

In reviewing submissions for DNA27, we expect you to consider and respond to at least the following points:

1.  Briefly summarize the research being presented in at least a few sentences, as you understood it as a reviewer. What are the main points being addressed by this research, and are they relevant to the DNA27 conference?

2.  For Track A, do the proofs and discussions fully support the claims for all results, and do they appear complete and correct? (If there is a technical appendix, is it necessary for understanding the results?) For Track B, do the conclusions and/or experiments presented in the work support ALL of the claims that are made in both the title and abstract? Is the supporting document sufficient to support the claims?

3.  Is the paper well written? Is it clear to read?

4.  How original is the work? For Track A, all results must be novel and unpublished. For Track B, the material being presented must be at least 67% new content over what was presented in previous years.

5.  Substantiate your final reviewer score with AT LEAST a paragraph of description. This way members of the PC can properly evaluate your review during the days allotted for review discussions (June 8-14).

6.  If you intend to seek subreviewers for some papers, we strongly recommend reading through your assigned papers' introductions and "related work" section (a good source of potential subreviewers) within the next few days and contacting potential subreviewers as soon as possible. Please make sure that your subreviewers remain on schedule and that their reviews are adequate and follow the above guidelines. Additionally, you should be prepared to discuss any paper assigned to you, whether you have a subreviewer or not. This year, subreviewers may participate in discussions if they wish.  Requesting a subreviewer in EasyChair can be confusing.  After clicking the button to request a subreviewer, you must (once again) confirm that you want your request to be sent.  You can verify your requests by clicking the 'Subreviewers' item under the 'Reviews' menu.
