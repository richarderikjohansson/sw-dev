# Motivation

For the code I am currently working with I relay on quite few libraries on my day to day work. I
have also written some modules that handle fetching data, visualizing, and writing and saving data
from various sources

## Libraries I use

* [NumPy](https://numpy.org/doc/stable/), which I use for dealing with arrays and matricies. Also
for reading paths to files which I sometimes save in .txt files.
* [matplotlib](https://matplotlib.org/), which I use for visualizing data.
* [PyARTS](https://atmtools.github.io/arts-docs-2.6/index.html), Used for advanced radiative
transfers calculations.
* [requests](https://requests.readthedocs.io/en/latest/), written some modules that relay on the
requests library where I fetch data from various targets.
* [h5py](https://docs.h5py.org/en/stable/), Used for reading and writing to .hdf files.


## Code I have developed

* [KIMRA/dbase](https://gitlab.irf.se/kimra/dbase/-/tree/main/utils?ref_type=heads), Code that I run on
our server where we save the raw data from our radiometers. It is still under development, but the
main function of it is to read raw data from the measurement and place it in more manageable format.
Where I have chosen in .hdf5 format. It also relays on a module I have written to fetch the
temperature from IRF's weather station at the start of the measurement

* [magscrape](https://gitlab.irf.se/richardj/magscrape), A module that I created to fetch data from
  IRF's magnometers in various time periods. Also under development

* [KIMRA/ARTS](https://gitlab.irf.se/kimra/ARTS), Code I started writing right away when I started
my Ph.D. where I mainly use PyARTS for various calculations, such as inversions from our
measurements. This is very much an unfinished product and I will work with it throughout my current
position.

## Code I am going to write

* I will take what I have learned from this course to refine my current repositories and maybe at a
later stage merge all these smaller repositories into a larger one that can handle all of the things
from each. This since they are all related to my current work. The goal when I end my Ph.D. is that
everything will be automated, all the way from parsing the raw data files to visualizing the
retrieval data at some internet endpoint.

* I am also quite interested in learning lua to develop plugins for nvim
* I also want to become better att low level stuff such as C++ and Rust to deal with low level
coding and maybe write some cool teminal applications in the future in Rust.



