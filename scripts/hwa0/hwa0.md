# Development environment

1. I had git installed since before and is using version 2.39.5 from `git --version` 
2. I have a repository for this course in [GitHub repository](https://github.com/richarderikjohansson/software_development_for_researchers)
3. I use `mamba` which can be installed from [Miniforge3](https://github.com/conda-forge/miniforge)


## Mamba cheet sheet

1. Creating empty environment:
```bash
mamba create -n my_env
```
With that command you are creating an empty environment with the name *my_env*.

2. Creating environment from *environment* yaml file:
```bash
mamba env create -f environment.yml
```
With that command is a environment created from the environment `environemnt.yml` file with the -f
flag, indicating that a enviroment should be created from a file. The name of the environment is
indicated in the file itself.

3. List enviroments:
```bash
mamba env list
```
That command gives you a list of all environments installed on your system and the path to where
they are installed.

4. Activate/deactivate enviroments:
```bash
mamba activate my_env
mamba deactivate
```
With the first command you activate a environment called *my_env*, which has to be in your list of
installed environments. The second command you deactivate the environment return you to the *base*
environment.

## Editor shortcuts, etc.

My workflow when coding actually relay on more than only editor shortcuts. On my personal system I
mainly work with tiling window managers, such as *i3* or *hyprland* on Arch linux, btw (xD). I pair
this with *tmux* and *neovim* to control most of what I want to do to my keybord. However on my work
system I use a MacBook Air, but there are applications that you can install to make the system work
as an tiling window manager. I use a application called *Aerospace* and it can be configured to
work similar to i3.

### Aerospace

I usually only have dedicated applications on single workspaces. I have two separate terminal
windows in workspace 1 and 2, on for a terminal locally and one terminal that I am connected to a
remote sever via ssh. On workspace 3 I usually have a browser opened, so I easily can browse for
example code documentation. Workspace 5 is dedicated to communication so on this I have my email
application and Slack opened and on workspace 6 I usually have Spotify opened. See below how I
switch between the workspaces:

* `super+1` $\rightarrow$ Local terminal
* `super+2` $\rightarrow$ Remote terminal
* `super+3` $\rightarrow$ Browser
* `super+5` $\rightarrow$ Communication 
* `super+6` $\rightarrow$ Spotify 

### Tmux

[Tmux](https://github.com/tmux/tmux/wiki) is a terminal multiplexer, meaning that you can have several terminal instances within one
single terminal in different panes and windows. I am probably not using the full power of this
awesome tool, but how I work with it works very good for the work I do. I usually try to keep it as
clean as possible with maybe 2 active windows and usually just one pane within each window. Tmux
have a multitude of available plugins to choose from, and the one I use for workflow is
[Vim-Navigaton](https://github.com/christoomey/vim-tmux-navigator) which enables me to navigate the
panes I have within tmux using vim movement, without the need of using the original prefix `Ctrl+b`.
Below is the majority of the shortcuts I use:

* `Ctrl + "` $\rightarrow$ Create a new horizontal pane
* `Ctrl + %` $\rightarrow$ Create a new vertical pane
* `Ctrl + l` $\rightarrow$ Move to the pane right of the active one
* `Ctrl + h` $\rightarrow$ Move to the pane left of the active one
* `Ctrl + k` $\rightarrow$ Move to the pane above of the active one
* `Ctrl + j` $\rightarrow$ Move to the pane below of the active one
* `Ctrl + b + c` $\rightarrow$ Create a new window 
* `Ctrl + b + ,` $\rightarrow$ Rename window
* `Ctrl + b + w` $\rightarrow$ Get a list of widows which I can navigate and choose from 
* `Ctrl + b + l` $\rightarrow$ Select previous window
* `Ctrl + b + $` $\rightarrow$ Prompt to rename the current session

One really nice feature of tmux is that you can also detach your tmux session, meaning that
whatever process you have running in that tmux session can be run only within tmux. I use this when
running really time consuming scripts, for example when I run my retrievals. I usually do this on a
dedicated server I use for these calculations over ssh. So I can start the retrieval with in a local
tmux session on the server. I can then detach that session on the server and then log out from the
ssh. This ensures that the process is continuing locally on the server within tmux and I do not
longer have to be connected to it from my local system. I detach and attach a session with the below
shortcuts and commands:

* `Ctrl + b + d` $\rightarrow$ Detach session
* `tmux ls` $\rightarrow$ List tmux sessions
* `tmux ls` $\rightarrow$ List tmux sessions
* `tmux attach-sessions -t session_name` $\rightarrow$ Attach session with the name *session_name*

### Neovim

[Neovim](https://neovim.io/) is a very customizable editor which utilizing the movement from vim and
its predecessor vi. Neovim, or for short, nvim have several different modes that you can choose from
and each have their own usage

**Navigation (Normal mode)**

* `l` $\rightarrow$ Move cursor right
* `h` $\rightarrow$ Move cursor left 
* `k` $\rightarrow$ Move cursor up 
* `j` $\rightarrow$ Move cursor down 

You can also use a commands to navigate your code: You enter command mode by pressing `:`. Below is
a list of commands I use to navigate my code:

* `/substring` $\rightarrow$ Searches to the *substring* that you want to navigate to. If it appears
  by more than one time in the code you jump to the next instance of it by pressing `n`
* `num` $\rightarrow$ Jumps to line *num* where num is an integer

**Editing:**
The next mode is the *Insert* mode which is for writing and editing code. You get into that mode by
pressing `i` and return to normal mode again by pressing `Esc`. If you want to perform a multiline
edit you can do so by first enter *Visual Blocke* mode with `Ctrl + v` you then can select where you
want to edit by vim navigation then by pressing `I` you gone in to insert mode for the block you
have chosen. You can then write what you want to have in that block and escape with `Esc` by writing
everything in that block.

You can also do search and replace, the way I usually do it is by first enter into *Visual line*
mode with `Shift + v` I then choose the lines where I want to make the search and replacement by
navigating with vim navigaton. I when enter command mode with `:` and make the following for the
example where I want to replace *foo* with *bar*

* `s/foo/bar/g` $\rightarrow$ Searches the visual block I have selected for foo and replace it with
  bar

I sometimes also do this without selecting in Visual line mode and this can be done with a command

* `.,$s/foo/bar/g` $\rightarrow$ Searches from where the cursor is located to the end of the file
and replaces foo with bar 

To save and quit nvim you do this from commands, which is opened with `:`

* `w` $\rightarrow$ Write to file
* `wa` $\rightarrow$ Write to all files in all buffers
* `wqa` $\rightarrow$ Write to all files in all buffers and quit nvim

**Plugins:**
nvim have a multitude of very helpful plugins, written mainly in lua. Many of them are for aesthetics,
such as color schemes. However, there are many extremely helpful plugins which I use that speeds up
my workflow. One of them are for example linters and formatters. In my configuration for nvim I have
setup that I have a specal key that I use as a prefix, called a *Leader*. Mine is *Spacebar*.
For my linting and formatting I use the very strict linter *pylint* for my linting and *ruff* for formatting
in Python. See below shortcuts:

* `Leader gf` $\rightarrow$ Formats my code with ruff
* `Leader ca` $\rightarrow$ Gives me code actions, where I get a list of actions, I can for
  example format my imports and other things.

I Also have a very useful plugin to navigate between files called *Telescope*. This plugin utilizes
fuzzy search to find files. See below for shortcuts

* `Leader Leader` $\rightarrow$ Opens up a list with previous opened files with a preview og the
content
* `Ctrl + p` $\rightarrow$ Lists all the files in the current working directory


### Conclusion

The workflow system I work with currently work pretty good for me. There is always new things In
learn about the system I use (especially) in nvim. I find new glugins all the time that enhances my
experience and I find new ways of doing things in nvim all the time. I have heard that people that
worked with vim and neovim for 10-20 years all still learn new stuff. So it is a continuous learning
working with nvim.

