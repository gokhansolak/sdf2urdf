# SDF 2 URDF
Python program and Vim plugin to convert SDF elements to URDF format. SDF and URDF are XML file formats used in robot description.  

# Usage

Navigate to the project folder in a terminal tool. Run the program with Python 3:
```bash
python3 sdf2urdf.py
```
It will ask for the xml element to convert. Enter the element and end the input with an 'e' line.

It will print the corresponding URDF element. 

![Usage example][usage-img]


The program doesn't fully convert a file at this stage. You should use it element by element. It may need some manual fixes for a few element types, e.g. joints.

# Vim Plug-in
You can use the same function in vim as a plugin. 

## Installing

You can obtain it with a package manager like Vundle:

* Add the line ``Plugin 'gokhansolak/sdf2urdf'`` between
```vim
call vundle#begin()
...

call vundle#end()
```
* Run ``:PluginInstall`` in Vim.

Also, if you have Pathogen installed, you can clone this repo under ~/.vim/bundle:

* ``git clone git@github.com:gokhansolak/sdf2urdf.git ~/.vim/bundle/sdf2urdf``

## Usage

![Vim usage gif][vim-usage-gif]

* Select the SDF element to convert in visual mode ``v``.
* Call the conversion command ``:S2u``
* Selected element will be replaced with its URDF counterpart.

[usage-img]: doc/sdf2urdf-usage.png "Usage example"
[vim-usage-gif]: doc/vim-usage-01.gif "Vim usage gif"
