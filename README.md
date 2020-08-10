# `About`

If someone wants to go about creating a very strong metal, one common method is via the use of Severe Plastic Deformation (SPD) techniques, which aim to produce ultra fine grain materials with extremely refined microstructures. Within the SPD class of deformation techniques there's something called Equal Channel Angular Extrusion (ECAE), which works by extruding your sample around a corner, inducing significant strain without reducing cross-sectional area. Because of this, a sample can be extruded multiple times, producing a finer microstructure each pass through the channel. In order to confirm your ECAE runs are doing what they're supposed to, you can perform a variety of mechanical tests to see if the strength has actually increased compared to an un-extruded sample of the same material you started out with. If you want to look at the microstructure of the sample, then you have to go grab a microscope and look at a small slice of your sample at the scale of hundreds of micrometers. Of particular interest is the percent amount of your sample that has recrystallized, which will show up as distinct domains under a microscope. It's pretty easy to just manually classify a region as recrystallized or not, but I thought it might be a fun endeavour to try and train a CNN to do it for me while covid19 has me couped up at home. Unfortunately, there's no huge labeled dataset of metallurgical microscopy samples so I have to generate my own synthetic data set, which is frankly the hardest part of this process.

# `Voronoi Diagrams` 
I don't even remember how I stumbled across these, but I took a look at these things and figured that I could use them to create images that look very similar to what an alloy sample would look like under a microscope. In Cartesian coordinate systems, the distance between two points is simply the square root of the difference in x-coordinates squared plus the difference in y-coordinates squared, ie dist(p, q) = &radic;(p<sub>x</sub>-q<sub>x</sub>)<sup>2</sup>+(p<sub>y</sub>-q<sub>y</sub>)<sup>2</sup>. In a plane, the Voronoi diagram Vor(P) is the subdivision of the plane into n cells, one for each site in a set of points P, with the property that each point q lies in the cell of P<sub>i</sub> if and only if dist(q, P<sub>i</sub>) &lt; dist(q, P<sub>j</sub>) for P<sub>j</sub> &isin; P and j &ne; i. 
