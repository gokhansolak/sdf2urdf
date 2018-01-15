# SDF 2 URDF
Python functions to convert SDF elements to URDF. SDF and URDF are XML file formats used in robot description.  

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
You can use the same functions in vim with the plugin file under 'vim/' folder. 

## Plugin usage

![Vim usage gif][vim-usage-gif]

* Source the 'sdf2urdf.vim' script in vim ``:source path/sdf2urdf.vim``.
* Select the SDF element to convert in visual mode ``v``.
* Call the conversion command ``:S2u``
* Selected element will be replaced with its URDF counterpart.

[usage-img]: docs/sdf2urdf-usage.png "Usage example"
[vim-usage-gif]: docs/vim-usage-01.gif "Vim usage gif"
