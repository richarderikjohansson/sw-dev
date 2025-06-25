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

## Editor shortcuts

My workflow when coding actually relay on more than only editor shortcuts. On my personal system I
mainly work with tiling window managers, such as *i3* or *hyprland* on Arch linux, btw (xD). I pair
this with *tmux* and *neovim* to control most of what I want to do to my keyboard. However on my work
system I use a MacBook Air, but there are applications that you can install to make the system work
as an tiling window manager. I use a application called *Aerospace* and it can be configured to
work similar to i3. which I will talk more about in Homework assignment 3


### Neovim

[Neovim](https://neovim.io/) is a very customizable editor which utilizing the movement from vim and
its predecessor vi. Neovim, or for short, nvim have several different modes that you can choose from
and each have their own usage

**Navigation (Normal mode)**

* `l` &rarr; Move cursor right
* `h` &rarr; Move cursor left 
* `k` &rarr; Move cursor up 
* `j` &rarr; Move cursor down 

You can also use a commands to navigate your code: You enter command mode by pressing `:`. Below is
a list of commands I use to navigate my code:

* `/substring` &rarr; Searches to the *substring* that you want to navigate to. If it appears
  by more than one time in the code you jump to the next instance of it by pressing `n`
* `num` &rarr; Jumps to line *num* where num is an integer

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

* `s/foo/bar/g` &rarr; Searches the visual block I have selected for foo and replace it with
  bar

I sometimes also do this without selecting in Visual line mode and this can be done with a command

* `.,$s/foo/bar/g` &rarr; Searches from where the cursor is located to the end of the file
and replaces foo with bar 

To save and quit nvim you do this from commands, which is opened with `:`

* `w` &rarr; Write to file
* `wa` &rarr; Write to all files in all buffers
* `wqa` &rarr; Write to all files in all buffers and quit nvim

**Plugins:**
nvim have a multitude of very helpful plugins, written mainly in lua. Many of them are for aesthetics,
such as color schemes. However, there are many extremely helpful plugins which I use that speeds up
my workflow. One of them are for example linters and formatters. In my configuration for nvim I have
setup that I have a specal key that I use as a prefix, called a *Leader*. Mine is *Spacebar*.
For my linting and formatting I use the very strict linter *pylint* for my linting and *ruff* for formatting
in Python. See below shortcuts:

* `Leader gf` &rarr; Formats my code with ruff
* `Leader ca` &rarr; Gives me code actions, where I get a list of actions, I can for
  example format my imports and other things.

I Also have a very useful plugin to navigate between files called *Telescope*. This plugin utilizes
fuzzy search to find files. See below for shortcuts

* `Leader Leader` &rarr, Opens up a list with previous opened files with a preview og the
content
* `Ctrl + p` &rarr; Lists all the files in the current working directory

## Update 

Since this course I started using *uv* exclusively when working with Python projects,
except when working with PyARTS, since it requires me to install via conda.
