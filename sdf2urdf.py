import sys
import xml.etree.ElementTree as etree



def pose2origin(root):

    pose = root.text
    pose_list = list(pose.split())

    new_root = etree.Element("origin")
    new_root.attrib["xyz"] = " ".join(pose_list[:3])
    new_root.attrib["rpy"] = " ".join(pose_list[3:])
    
    return new_root

def children2attributes(root):

    children = root.getchildren()

    # same tag
    new_root = etree.Element(root.tag)
    # add attribs for each child
    for c in children:
        # if this child has children then it is unsuitable
        if len(c.getchildren()) > 0:
            print("element is too deep")
            exit()
        new_root.attrib[c.tag] = c.text
    return new_root


def convert_sdf2urdf(root):
    if root.tag == "pose":
        return pose2origin(root)
    if root.tag in ["box","sphere","cylinder","inertia","limit"]:
        return children2attributes(root)
    if root.tag in ["joint","link","robot","geometry","inertial","visual","collision"]:
        new_root = etree.Element(root.tag, attrib=root.attrib)
        children = root.getchildren()
        for c in children:
            new_root.append(convert_sdf2urdf(c))
        return new_root
    print(root.tag + " element is not recognized.")

print("Please enter the sdf element. Write \'e\' to complete the input.") 

str_lines = ""
current_line = ""
while current_line != "e": 
    str_lines += current_line
    current_line = input()

# parse xml
root = etree.fromstring(str_lines)

new_root = convert_sdf2urdf(root)

# override the selected lines
new_str = etree.tostring(new_root).decode("utf-8")
print(new_str)

