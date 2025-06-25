# Automate away friction

When it comes to friction, I have in the past used got used to it instead of doing
something about it. However, after switching over to uv instead of using conda 
exclusively I found out activating environments seem to be a hassle. So I 
wrote a quite simple fish function to just activate the environment if a *.venv*
directory is present:

```fish
function activate
    set -l env (find -name activate.fish)
    set -l c (count $env) 

    if test $c -gt 1 
        echo "More than one environment found. Select which to activate by the index below"
        for i in (seq $c)
            echo $i:  $env[$i]
        end
        read index
        source $env[$index]
    else
        source $env
    end
end

```

I also took interest in using *eza*, after I asked Daniel what he used for listing files and directories.
However, using it as it is without writing some kind of function for it would absolutely case friction so 
I wrote I very simple fish function for it:


```fish
function l 
    command eza --long --icons always --group --git --all --header
end
```

Conclusively, this lecture and the examples I have seen have made me prone to actually do something about 
things that can cause friction instead just accepting it.


