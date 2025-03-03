# Notes

Installed *course_package* with setup.py and pip. It is working greatly. 
Maybe write a bash script to install environment and also install 
*course_package* within this environment.

The two functions were created in two different modules and could successfully
be imported both within the package, and also outside this package. The reverse
list function manipulates the list in place with:

```python
list_to_reverse[::-1]
```
The second function import this function and reverse the first list. I then kept 
it simple by looping through the two lists with `zip()` and appending a new list 
with the lists method. Very easy and maybe not the fastest and most reliable thing 
to do this since the lists must be of equal length.

Created two functions, one to write a string to a binary file, and one to read a binary file.
The string is encoded with utf-8 encoding by default.
