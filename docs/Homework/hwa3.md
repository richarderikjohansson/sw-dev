# Tools and environment

## Debug a python program

As I mentioned in Homework assignment 0 I am using neovim as an editor. Before this assignment I
actually never bothered installing a debugger in neovim since I usually have written less complex
pieces of software. However, lately I have been writing more and more complex software (relatively)
and in some cases I could have benefited from using one.

Therefore I installed [dap](https://github.com/mfussenegger/nvim-dap) and [dap-python](https://github.com/mfussenegger/nvim-dap-python) in my neovim environment according to this setup: [nvim-dap-python](https://github.com/NeuralNine/config-files/blob/master/.config/nvim/lua/plugins/nvim-dap.lua). 
This did not work out of the box for me, since I am using conda/mamba as a environment handler I had to
tweak this setup a little bit since `debugpy` have to be installed for the dap to work in neovim.
The configuration I used assumed that debugpy was installed globally and I want debugpy to work from
my environment.

This meant that I had to change the path from where neovim reads the python binary:

```lua
local python_install_path = vim.fn.exepath('python')
dap_python.setup(python_install_path)
```

That change ensured that neovim used the path for my active environment when I started neovim. Using
this debugger was quite easy below is some of the keyboard shortcuts that I use:

* `Space + db` &rarr; Toggle breakpoint
* `Space + dc` &rarr; Start the debugger
* `Space + dc` &rarr; Start the debugger
* `Space + di` &rarr; Step into 
* `Space + do` &rarr; Step over 
* `Space + dO` &rarr; Step out 
* `Space + dq` &rarr; Terminate
* `Space + du` &rarr; Toggle UI 

I tested the debugger on the `interleave` assignment and it worked great.


## Inventory of tools

### Aerospace

Aerospace is a tiling window manager made for MaxOS and I have it configured similarly as how my i3
setup is working on my personal Linux system.
I usually only have dedicated applications on single workspaces. I have two separate terminal
windows in workspace 1 and 2, on for a terminal locally and one terminal that I am connected to a
remote sever via ssh. On workspace 3 I usually have a browser opened, so I easily can browse for
example code documentation. Workspace 5 is dedicated to communication so on this I have my email
application and Slack opened and on workspace 6 I usually have Spotify opened. See below how I
switch between the workspaces:

* `super+1` &rarr; Local terminal
* `super+2` &rarr; Remote terminal
* `super+3` &rarr; Browser
* `super+5` &rarr; Communication 
* `super+6` &rarr; Spotify 

### Tmux

[Tmux](https://github.com/tmux/tmux/wiki) is a terminal multiplexer, meaning that you can have several terminal instances within one
single terminal in different panes and windows. I am probably not using the full power of this
awesome tool, but how I work with it works very good for the work I do. I usually try to keep it as
clean as possible with maybe 2 active windows and usually just one pane within each window. Tmux
have a multitude of available plugins to choose from, and the one I use for workflow is
[Vim-Navigaton](https://github.com/christoomey/vim-tmux-navigator) which enables me to navigate the
panes I have within tmux using vim movement, without the need of using the original prefix `Ctrl+b`.
Below is the majority of the shortcuts I use:

* `Ctrl + "` &rarr; Create a new horizontal pane
* `Ctrl + %` &rarr; Create a new vertical pane
* `Ctrl + l` &rarr; Move to the pane right of the active one
* `Ctrl + h` &rarr; Move to the pane left of the active one
* `Ctrl + k` &rarr; Move to the pane above of the active one
* `Ctrl + j` &rarr; Move to the pane below of the active one
* `Ctrl + b + c` &rarr; Create a new window 
* `Ctrl + b + ,` &rarr; Rename window
* `Ctrl + b + w` &rarr; Get a list of widows which I can navigate and choose from 
* `Ctrl + b + l` &rarr; Select previous window
* `Ctrl + b + $` &rarr; Prompt to rename the current session

One really nice feature of tmux is that you can also detach your tmux session, meaning that
whatever process you have running in that tmux session can be run only within tmux. I use this when
running really time consuming scripts, for example when I run my retrievals. I usually do this on a
dedicated server I use for these calculations over ssh. So I can start the retrieval with in a local
tmux session on the server. I can then detach that session on the server and then log out from the
ssh. This ensures that the process is continuing locally on the server within tmux and I do not
longer have to be connected to it from my local system. I detach and attach a session with the below
shortcuts and commands:

* `Ctrl + b + d` &rarr; Detach session
* `tmux ls` &rarr; List tmux sessions
* `tmux ls` &rarr; List tmux sessions
* `tmux attach-sessions -t session_name` &rarr; Attach session with the name *session_name*

### vim movement

I know that some of the basics still is not in my repertoire when it comes to vim motions,
especially when it comes to moving within a line. I still am spamming hjkl way to much, when I
instead can use some built in functionality. What I learn when watching the some of the vim videos
seen in the handout is that I will now incorporate `w`, `b` and `f` much more. With `w` you jump
forward a word and with `b` you jump backward. `f` is used with the addition with the character you
want to jump forward to.
