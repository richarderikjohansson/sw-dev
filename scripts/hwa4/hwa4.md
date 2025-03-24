# Notes

As the instructions read I created a function that calculated $x_{n+1}$
for a given $x$ and $r$ in $x_{n+1}=rx_{n}(1-x_{n})$ and are defined as `logistic_equation` 
in the *bifurcation* module. The iterative part took some to to wrap my head around how to 
solve this. As any developerdo, I took some inspiration from stackoverflow. Reading some 
code where people have done similar things I finally managed to come up with a solution.

I created another another function named `make_logistic_map` in my bifurcation module 
where I specify number of points and iterations as parameters I then create two numpy arrays,
one for $r$ values that linearly increase  in the range [0,4] with the numbers 
of points which was given as a parameter. I then created the $x$ values randomly
in the range [0,1], also this with the number of points that was given as an parameter.
The function then iterates through the logistic equation and is returning the $r$ values and 
the $x_{n+1}$ after it has gone through the iteration.

I also created a function called `plot_map` that use the `make_logistic_map` function to 
create a still image. I also wanted to make a animation, which I never have done before. It was
somewhat challenging to understand how the animation feature work in matplotlib. By reading lots of
documentation and also, again turning my head to stackoverflow I came up with a solution that at
least works. I created another function in the bifurcation module defined as `animate_map` 
that took the number of points and iterations that the animation should show. I then defined the
figure without any data and styled it to my liking. Further more, I created a function called
`update` which really is the engine here. This function creates the data for each frame in the
animation. For each frame I called the make_logistic_map function to create the logistic map. Since 
I want to show how the map evolves for how many iterations it goes through I used the frame
parameter as the iteration parameter in my make_logistic_map function creating a frame for each case
in the range [0, iterations]. 
