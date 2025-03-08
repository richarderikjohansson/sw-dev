# Notes

As the instructions read I created a function that calculated $x_{n+1}$
for a given $x$ and $r$ in $x_{n+1}=rx_{n}(1-x_{n})$. The iterative part
it took some to to wrap my head around how to solve this. As any developer
do, I took some inspiration from stackoverflow. Reading some code where 
people have done similar things I finally managed to come up with a solution.

I created another another function in my `bifurcation` module where I specify
number of points and iterations as parameters I then create two numpy arrays,
one for $r$ values that linearly increase  in the range [0,4] with the numbers 
of points which was given as a parameter. I then created the $x$ values randomly
in the range [0,1], also this with the number of points that was given as an parameter



