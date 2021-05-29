+++
title = "glaser21_art_desig_dna_nanos_with_cad_softw: The art of designing dna nanostructures with cad software"
author = ["John Doe"]
draft = false
+++

tags
: [DNA Origami](../dna_origami.md)

keywords
:


## The art of designing dna nanostructures with cad software {#the-art-of-designing-dna-nanostructures-with-cad-software}

:Custom_ID: glaser21\_art\_desig\_dna\_nanos\_with\_cad\_softw
:URL: <https://doi.org/10.3390/molecules26082287>
:AUTHOR: Glaser, M., Deb, S., Seier, F., Agrawal, A., Liedl, T., Douglas, S., Gupta, M. K., …


### Notes {#notes}


#### Useful Quotes {#useful-quotes}

Where available, readily accessible design software catalyzes our ability to bring techniques to researchers in diverse fields and it has helped to speed the penetration of methods, such as DNA origami, into a wide range of applications from biomedicine to photonics.

As an example, creating a precise design for one of the most conceptually simple
two-dimensional DNA origami structures, the so-called Rothemund Rectangle, involves
the linking of 171 four-way Holliday junctions, and the assignment of 6912 bases according
to the sequence of the underlying scaffold and its topological path through the overall
structure. More intricate designs that are based on this or other methods drastically compli-
cate the process, particularly since this requires the daunting task of visually mapping the
three-dimensional network of interconnected junctions onto a two-dimensional schematic.

Nevertheless, a steady stream of CAD software
packages for designing different types of simple and complex DNA nanostructures has
emerged with increasingly user-friendly graphical user interfaces and abilities for creating
complex designs from scratch. Whether by coincidence or otherwise, the same timeframe
has also corresponded to a rapid expansion of the DNA nanotechnology from being an
interesting niche oddity, to making inroads in fields from nano-photonics to medicine and
healthcare. For these applications, the DNA origamis are of particular interest, since they al-
low for the precise positioning of molecules and structures for specific applications [17,18].

many different design strategies for
creating DNA origami structures have been introduced, including densely packed two-
and three-dimensional structures based on parallel helices [12,19,20], structures containing
precise twists and curves [21], thin-edged wireframes [22–25], geometrically-inspired
polyhedra [26–28], enclosed boxes [29], structures that are folded and cut into topological
architectures [30], pre-stressed tensegrity structures [31], and countless others.

"When considering the numerous and diverse strategies for architecturally designing a
DNA origami structure, there is no one-size-fits-all software package that is suitable for
every possibility. Rather, a collection of CAD programs, each of which fits a specific niche in
design methodology, have gradually filled the space over the last decade."

Even though they often require too much computation power and/or time to be
feasible for direct integration into standalone CAD software, like those described above,
these tools are valuable to researchers for the preliminary validation of a particular design,
made before incurring the cost of purchasing several hundred or more oligonucleotides.
Indeed, even the best in silico simulations of a complex DNA origami or brick structure
are not equivalent to rigorous experimental confirmation by agarose gel electrophoresis,
electron microscopy, or atomic force microscopy. Nevertheless, they can often tip the
designer to some subtle problems in the design, which can ultimately mean doom for the
self-assembly of the structure.

    It is worth mentioning that
    the acceptance of a new technology is not only based on its usefulness, but also on the ease
of use [110]. One of the reasons that subfields, like DNA-enabled nano-plasmonics, have
gained rapid prominence is that the experts in those fields can embrace and successfully
use the different techniques of DNA nano-fabrication, often DNA origami, to answer some
of their most fundamental questions. Therefore, we suggest that robust and easy-to-use
software provides that key inflexion point.

    Even if successfully implemented, all of the aforementioned CAD software design
and analysis tools are, of course, no substitute for tedious and rigorous experimental
verification, and only give information regarding the final target structure, rather than the
highly complex process by which it is formed. As numerous experimental and analytical
studies have shown, folding and assembly pathways can be equally decisive for the proper formation of a particular design [65,112–114]. These can be highly impacted by ionic condi-
tions in the surrounding buffer, or alternatively thermal annealing protocols implemented
by careful design or brute-force screening of thermal annealing protocols [57,115].


#### Aim: {#aim}

Here, we review the historical and current state of CAD software to enable a variety of methods that
are fundamental to using structural DNA technology. Beginning with the first tools for predicting
sequence-based secondary structure of nucleotides, we trace the development and significance of
different software packages to the current state-of-the-art, with a particular focus on programs that
are open source.

Therefore, this review covers some of the most important milestones in the rapid de-
velopment of semi- or fully automated design software for both: either scaffold-based DNA
or tile-based DNA structures, pointing out their applicability for an anticipated application.


#### <span class="org-todo todo TODO">TODO</span> Turing Completeness of DNA {#turing-completeness-of-dna}

in 1995 Erik Winfree showed that the self-assembly of DNA is Turing universal [10], meaning that, in principle, rather than by trial and error, one can systematically design any arbitrary shape or perform any computation using DNA

Winfree, E. Algorithmic Self-Assembly of DNA. In Proceedings of the 2006 International Conference on Microtechnologies in
Medicine and Biology, Okinawa, Japan, 9–12 May 2006; p. 4. [CrossRef]


#### Overcoming size barriers of M13 {#overcoming-size-barriers-of-m13}

These discrete size limits that are imposed by this choice
of scaffold (typically several hundred nanometers for a thin rod or approximately one
hundred nanometers for a more rigid block) have been increasingly circumvented by using,
or genetically modifying, longer scaffold strands [32,33], or alternatively binding together
multiple structures into a large aggregate structures [34–38].


#### Other Software {#other-software}

<!--list-separator-->

-  Tiamat

    Tiamat takes the randomness factor into
    account. The sequence generator also adds reliability to the tool, as it avoids secondary
    structures. This software also recognizes different factors, such as uniqueness on subse-
    quence existence, restriction on homopolymer runs (symbol repetitions), and GC-content
    constraint

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  vHelix

    -   Autodesk maya
    -   Polyhedral mesh wireframes

    "Furthermore, previ-
    ous approaches usually folded the circular single-stranded scaffold DNA into a tree-like
    shape, and connected segments via so-called “helper joins”, which are short single DNA
    strands forming links between two disconnected “blunt end” scaffold loops. However,
    this design method for wireframe meshes would require hundreds of these helper join
    strands per structure, which lead to aggregation problems [24]. The main advantage of this
    method is that the algorithm optimizes the path of the scaffold in a way that it transverses
    every edge once. Mathematically, this is closely linked to the ‘route Inspection problem’
    in graph theory, which goes back to an old question that is known as ‘the Seven bridges
    of Königsberg’ [43]. The problem revers to the question: if seven bridges connect the
    central part of the city with the three surrounding parts—is it possible to visit all four parts
    of the city and cross each bridge only once? It was shown by Euler that no such route
    exists [44] and that in a more general sense such loop walks require an even degree at
    each vortex, edges in the case of wireframes. In vHelix, after drawing the desired mesh
    with Maya, the algorithm pairs odd-degree vertices (in a certain proximity) in order to
    eliminate them by introducing double edges (Figure 4b,c). This allows for the scaffold
    to travel through any desired wireframe structure, which is then brought into the final
    shape by staple strands. The algorithm finds this routing with a very short computing time.
    Before the final output, torsional strain is also equally distributed in the structure by the
    software. The main advantage of this construction technique is that most three-dimensional
    shapes can be broken down into polygon meshes, particularly made up of triangular tiling,
    which have a high rigidity, and these can now be implemented despite having an odd
    vertex degree. Furthermore, the final outcome only consists of DNA double helices, which
    circumvents the problem of unphysiologically high salt concentrations that are necessary
    for closed-packed bundles of helices that are found in most previous DNA origami designs"

<!--list-separator-->

-  DAEDALUS, PERDIX, TALOS, METIS

    DAEDALUS is specialized for creating
    DNA origami renderings of polyhedral networks. The desired shape can either be directly
    entered into the software by assigning the vertices, connecting edges and corresponding
    faces, or input through a number of CAD file formats that specify polygonal geometry (e.g.,
    PLY, STL, or WRL format). This software then calculates a two-dimensional representation
    of the three-dimensional object with the scaffold DNA running through this entire tree
    (Figure 5a). The staple strands are chosen in a manner that interconnected edges consist of
    two duplexes that are joined by antiparallel double crossovers. One of the main advances
    of this approach is that the desired shape does not need to be topologically equivalent
    to a sphere, which broadens the possibility for more arbitrary architectures (e.g., a torus,
    whereas vHelix assembled a nicked torus) [28]. The software provides the full set of staple
    strands for either a given scaffold strand by the user or it generates a default scaffold
    strand. Additionally, it returns a PDB (“Protein Data Bank”) file, which contains a complete
    three-dimensional structural model down to the atomic scale

    PERDIX overcomes the limitation of DEADALUS
    in rendering two-dimensional objects. It uses a similar approach, but it can now account
    for planar geometries and arbitrary network edge lengths and vertex angles [45]. It also
    requires a CAD input file and returns a list of the staple strand fitting to the scaffold strand.
    The source code is freely available in Fortran.

    Later, TALOS was developed, which uses
    this approach to construct three-dimensional objects with edges that are based on “6-helix
    bundle” (6HB) designs [46]. As a further addition,

    METIS was established to specifically
    generate two-dimensional wireframe origami by stacking three layers on top of each other
    (Figure 5b) [47]. Choosing 6 HB edges over double crossover edges significantly increases
    the mechanical stability due to the higher number of involved helices at each edge, thus
    giving it a broader applicability.

    ATHENA [48]. It provides the user with an intuitive GUI, which drastically increases
    the easy usability of each of the previous algorithms, so that any wireframe DNA origami
    in two- or three dimensions using either 2 HB or 6 HB edges can be created.

<!--list-separator-->

-  DNA Tile and Bricks

    When compared to the DNA origami technique, the DNA brick strategy in particular
    has the advantage of not being constrained by the number of base pairs in the underlying
    scaffold strand, or its typically circular topology.

    It is also straightforward to create arbitrar-
    ily large structures either by simply using an expanded set of component oligonucleotides
    bricks [52], or by using a repetitive design that assembles into mesoscopic crystalline
    surfaces [53]. Finally, since all individual components are short, synthetically produced
    oligonucleotides, it is possible, by direct chemical synthesis, to create a denser matrix of
    functional elements than origami can create, where 50% of the structure is comprised of
    the more difficult to modify central scaffold strand.

    These features make this method an attractive strategy for industrial nanofabrication,
    where nanoscale precision over distances approaching wafer sizes are invaluable. Indeed,
    one of the most promising studies based upon this technique demonstrates unprecedented
    long-range spatial control over the placement of carbon nanotubes, pointing towards a
    potential real-world future in nano-circuitry [54].

    The hurdles to
    its wider dissemination are two-fold:

    1.  While offering the aforementioned design advantages, the lack of a central scaffold

    strand to template the assembly means that the self-assembly process is dependent
    upon a nucleation-and-growth mechanism [65]. Here, the local structure, topolog-
    ical connectivity, kinetic traps, and even stoichiometry between the hundreds or
    thousands of components are critical parameters and each can impact yields.

    1.  Particularly for three-dimensional bricks, the process of translating an arbitrary design

    into a collection of hundreds or thousands of unique DNA oligonucleotide sequences
    is extraordinarily complex. The target structure is first rendered as a collection of
    voxels, each corresponding to an eight base pair segment of double stranded DNA,
    then connections between the voxels under the constraints of DNA geometry are
    applied, before each strand is populated with appropriate sequences, according to the
    original report from Ke et al. [50]

    "notably, no all-in-
    one design suite equivalent to Cadnano in terms of built-in features and corresponding
    experimental validation exists to date."

<!--list-separator-->

-  3DNA

    The software platform 3DNA [79] was developed to model, edit, and visualize com-
    plex three-dimensional brick-based structures, using the strategy that was introduced by
    Ke et al. in 2012 [50], and later expanded to larger structures by Ong et al. in 2017 [52]. The
    conceptual approach to this design strategy is that every voxel in the abstract structural
    representation corresponds to a double-stranded, eight base pair domain interaction (be-
    tween different 32 bases long DNA bricks), which defines a voxel size to dimensions of
    approximately 2.5 × 2.5 × 2.7 nanometers. Each oligonucleotide brick, typically 32 bases
    in length, except for on the structure boundaries, spans four voxels, and interacts with
    four other unique bricks.

    NanoBricks Software. Available online: <http://molecular.systems/software> (accessed on 1 February 2020).

<!--list-separator-->

-  Analysis

    This ignores the finer thermodynamic or mechanical impacts of certain
    design motifs, which can additively lead to global faults when summed over the entire
    structure. These faults can arise from a number of easily overlooked factors, such as,
    for example, a high local density of short hybridized segments between crossovers [84],
    or small amounts of torque built up over broad parallel arrays of double-helices. These
    can lead to structural instability of the structure stemming from local dominance of the
    self-repulsion between neighboring double-helices, or unwanted global deformations, as
    shown, for example, in the sheet-like structure shown in Figure 9.

    In some cases, multiple, sequence-dependent isoforms can also arise from a single
    topological design [85]. Therefore, we briefly highlight several freely available simulation
    and modeling tools for DNA nanostructures, which can potentially aid in the design pro-
    cess.

<!--list-separator-->

-  List of simulation and modeling tools

    See text and table 3.

<!--list-separator-->

-  Recommendations

    We still see room for further development in the seamless integration of companion
    tools and modules for the analysis of structural designs directly into DNA-based CAD
    programs. Nevertheless, we do recognize that the computational resources that are required
    for any kind of detailed simulations are often unrealistic for what is available on the
    typical laptop or desktop used by academic researchers. One approach towards seamlessly
    combining design and rudimentary in silico validation could be direct integration of in-
    program portals for uploading to established online analysis tools, like Cando, MrDNA,
    or others. This, of course, would require close coordination between development teams,
    and it might also lead to the side-effect increased server load and according wait times,
    since integrated submission for analysis within the program would almost certainly lead
    to increased use.

<!--list-separator-->

-  Adenita

    While it can be used to create some de novo designs that are
    based on relatively simple motifs, such as single-stranded or double-crossover tiles, it is
    still limited as a design suite that is suitable for assisting with the creation of structures
    with any complexity, such as three-dimensional DNA origami or brick objects. Rather, its
    strength resides in its ability to span multiple platforms, and integrate the precise output
    files from each. Thus, we see this sort of “nanostructure-collage” approach as an important
    step forward towards robust and widely-encompassing DNA nano-fabrication options.


#### Refs to read {#refs-to-read}

10:
Winfree, E. Algorithmic Self-Assembly of DNA. In Proceedings of the 2006 International Conference on Microtechnologies in Medicine and Biology, Okinawa, Japan, 9–12 May 2006; p. 4. [CrossRef]

17:
Tapio, K.; Bald, I. The potential of DNA origami to build multifunctional materials. Multifunct.  Mater. 2020, 3, 032001. [CrossRef]

54:
Sun, W.; Shen, J.; Zhao, Z.; Arellano, N.; Rettner, C.; Tang, J.; Cao, T.; Zhou, Z.; Ta, T.; Streit, J.K.; et al. Precise pitch-scaling of
carbon nanotube arrays within three-dimensional DNA nanotrenches. Science 2020, 368, 874–877. [CrossRef] [PubMed]

{{< figure src="/ox-hugo/test.png" >}}

83:
NanoBricks Software. Available online: <http://molecular.systems/software> (accessed on 1 February 2020).

    Nowadays,
    large, often intricately complex, structures consisting of several hundred or more strands,
which can template the positions of large collections of accessory molecules, are used for
applications that range from synthetic vaccines [105] to the nanofabrication of inorganic
materials and substrates [54,95,106–109], or measurements of molecular forces that are
exerted by single proteins [107].

Davis, F.D. Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology. MIS Q. 1989, 13, 319–340. [CrossRef]

    Even if successfully implemented, all of the aforementioned CAD software design
and analysis tools are, of course, no substitute for tedious and rigorous experimental
verification, and only give information regarding the final target structure, rather than the
highly complex process by which it is formed. As numerous experimental and analytical
studies have shown, folding and assembly pathways can be equally decisive for the proper formation of a particular design [65,112–114]. These can be highly impacted by ionic condi-
tions in the surrounding buffer, or alternatively thermal annealing protocols implemented
by careful design or brute-force screening of thermal annealing protocols [57,115].
