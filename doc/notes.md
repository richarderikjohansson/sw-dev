# Document containing various notes

## Lectures notes 

## Homework assignment: Development enivironment

1. Create a small python package. 
2. Install your package into your virtual environment.
3. Create 2 functions in two separate modules inside 
   your package. One function should reverse a list and
   the other should take two lists as input, reverse the  
   first list and then interleave every other argument of 
   two lists outputting a single new list. You should import
   the list-reveral function from the other module 
   (hint: intra-package-references).
4. Create a scripts in a different location than were the 
   package is that uses this function from the package to interleave
   the following two strings: 'VOG!lo olH' and 'el,Wrd ROY'.
5. Implement a function in your package that uses the following: 
   f-strings, with, and encode / decode to save or load an input string
   in a binary file.
6. Install matplotlib into your environment.
   Implement one of the [https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_alpha.html#sphx-glr-gallery-lines-bars-and-markers-fill-between-alpha-py](examples).
   Run the code and get the plot to show.

### notes

Installed *course_package* with setup.py and pip. It is working greatly. 
Maybe write a bash script to install environment and also install 
*course_package* within this environment.

The two functions were created in two different modules and could successfully
be imported both within the package, and also outside this package. The reverse
list function manipulates the list in place with:

```python
lst[::-1]
```
The second function import this function and reverse the first list. I then kept 
it simple by looping through the two lists with `zip()` and appending a new list 
with the lists method. Very easy and maybe not the fastest and most reliable thing 
to do this since the lists must be of equal length.

Created two functions, one to write a string to a binary file, and one to read a binary file.
The string is encoded with utf-8 encoding by default.


## Miscellaneous notes


