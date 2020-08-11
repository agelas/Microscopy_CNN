# `About`

If someone wants to go about creating a very strong metal, one common method is via the use of Severe Plastic Deformation (SPD) techniques, which aim to produce ultra fine grain materials with extremely refined microstructures. Within the SPD class of deformation techniques there's something called Equal Channel Angular Extrusion (ECAE), which works by extruding your sample around a corner, inducing significant strain without reducing cross-sectional area. Because of this, a sample can be extruded multiple times, producing a finer microstructure each pass through the channel. In order to confirm your ECAE runs are doing what they're supposed to, you can perform a variety of mechanical tests to see if the strength has actually increased compared to an un-extruded sample of the same material you started out with. If you want to look at the microstructure of the sample, then you have to go grab a microscope and look at a small slice of your sample at the scale of hundreds of micrometers. Of particular interest is the percent amount of your sample that has recrystallized, which will show up as distinct domains under a microscope. It's pretty easy to just manually classify a region as recrystallized or not, but I thought it might be a fun endeavour to try and train a CNN to do it for me while covid19 has me couped up at home. Unfortunately, there's no huge labeled dataset of metallurgical microscopy samples so I have to generate my own synthetic data set, which is frankly the hardest part of this process.

# `Voronoi Diagrams` 
I don't even remember how I stumbled across these, but I took a look at these things and figured that I could use them to create images that look very similar to what an alloy sample would look like under a microscope. In Cartesian coordinate systems, the distance between two points p and q is simply the square root of the difference in x-coordinates squared plus the difference in y-coordinates squared, ie dist(p, q) = &radic;(p<sub>x</sub>-q<sub>x</sub>)<sup>2</sup>+(p<sub>y</sub>-q<sub>y</sub>)<sup>2</sup>. In a plane, the Voronoi diagram Vor(P) is the subdivision of the plane into n cells, one for each site in a set of points P, with the property that each point q lies in the cell of P<sub>i</sub> if and only if dist(q, P<sub>i</sub>) &lt; dist(q, P<sub>j</sub>) for P<sub>j</sub> &isin; P and j &ne; i. 

## Fortune's Algorithm
The most efficient way of constructing a Voronoi diagram is using Fortune's Algorithm, which gets the job done in <i>O</i>(<i>n</i>log<i>n</i>) time. What follows is a brief description of the algorithm's steps.

Input: A set P={P<sub>1</sub>,...,P<sub>n</sub>} of sites in a plane
Output: Vor(P) given inside a boudning box in a doubly-connected linked list <i>D</i>.

1. Initialize priority queue Q with all site events, initialize empty status structure &tau;, initialize empty doubly-connected linked list <i>D</i>

    &nbsp;&nbsp;while Q != empty<br>
        &nbsp;&nbsp;&nbsp;&nbspdo Remove event with highest y-coordinate from Q<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if event == site event at P<sub>i</sub><br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HandleSiteEvent(P<sub>i</sub>)<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HandleCircleEvent(&gamma;), &gamma; is a leaf of &tau; representing an arc that disappears<br>

2. Internal nodes in &tau; are half-infinite edges, compute bounding box and attack edges to bounding box
3. Traverse half-edges of doubly-connected edge list to add the cell records and pointers to and from them. 

## Resources Used:
Berg, Mark de. <i>Computational Geometry: Algorithms and Applications</i>. Berlin: Springer, 1997
https://github.com/Yatoom/voronoi
