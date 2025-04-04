# Documentation

This exercise serves the purpose to learn about documentation of packages and 
miscellaneous notes. To start out I used the python library `mkdocs` installed 
within the environment and later I also employed `mkdocstrings` library.

## MkDocs

This library is installed in the environment using pip. I also installed the 
*material* theme, since mkdocs only come with two default themes, and *material*
is not one of them. I installed all of this with the following:

```bash
pip install mkdocs mkdocs-material
```

To initialize the documentations I navigated to my project and gave the following command:
```bash
mkdocs new .
```
This creates a `docs` directory in the root of my project. In here I then place all of my markdown
files that I want rendered. When initializing is also a `mkdocs.yml` file created, which is where 
I point markdown files to certain tags. This is the structure I opted for:

```yaml
site_name: Software Development Notes 
nav:
  - Home: index.md
  - Homeworks: 
    - Assignment 0: Homework/hwa0.md
    - Assignment 1: Homework/hwa1.md
    - Assignment 2: Homework/hwa2.md
    - Assignment 3: Homework/hwa3.md
    - Assignment 4: Homework/hwa4.md
    - Assignment 5: Homework/hwa5.md
theme: material

```

## mkdocstrings 

`mkdocstrings` is another library that make your documentation even more detailed. This library takes 
advantage of the docstrings written for functions and classes. I also have a neovim plugin that generates
my doc strings automatically, called [DOGE](https://github.com/kkoomen/vim-doge). Below is my lua code 
to install and configure DOGE for Python:

```lua
return {
	{
		"kkoomen/vim-doge",
		build = ":call doge#install()",
		ft = { "python" },
		keys = {
			{
				"<leader>ds",
				function()
					vim.cmd("DogeGenerate")
				end,
				desc = "Generate Docstring",
				mode = "n",
			},
		},
		config = function()
			vim.g.doge_doc_standard_python = "google"
			vim.g.doge_enable_mappings = 1
		end,
	},
}
```
With this plugin I auto generate a docstring with Googles styling guide. Comes quite handy since It detects
arguments, returns and raises automatically. To install mkdocstrings for Python, I gave the following command:

```bash
pip install mkdocstrings-python
```

To make use of this library I had to put in the following in my `mkdocs.yml` configuration file:
```
plugins:
  - mkdocstrings
```

To render the docstrings I had to point to the module I wanted to have rendered with the Identifier `:::`. This 
is for example how the information from the docstring in for [Homework Assignment 4](/Homework/hwa4)

```
::: src.course_package.bifurcation
```


