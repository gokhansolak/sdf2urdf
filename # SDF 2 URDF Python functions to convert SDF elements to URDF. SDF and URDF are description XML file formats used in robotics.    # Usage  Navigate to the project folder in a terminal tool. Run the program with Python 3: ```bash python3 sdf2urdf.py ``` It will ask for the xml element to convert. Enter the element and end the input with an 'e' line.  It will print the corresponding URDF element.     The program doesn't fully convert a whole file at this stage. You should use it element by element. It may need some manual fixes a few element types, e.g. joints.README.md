# SDF 2 URDF
Python functions to convert SDF elements to URDF. SDF and URDF are description XML file formats used in robotics.  

# Usage

Navigate to the project folder in a terminal tool. Run the program with Python 3:
```bash
python3 sdf2urdf.py
```
It will ask for the xml element to convert. Enter the element and end the input with an 'e' line.

It will print the corresponding URDF element. 

![Usage example][usage-img]


The program doesn't fully convert a whole file at this stage. You should use it element by element. It may need some manual fixes a few element types, e.g. joints.


[usage-img]: docs/sdf2urdf-usage.png "Usage example"
