import vim
import sys
import xml.etree.ElementTree as etree

sys.path.append(vim.eval("a:path"))
import vim_tools as vt


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
    # pose nodes have a special treatment
    if root.tag == "pose":
        return pose2origin(root)
    # terminal nodes are just converted
    if root.tag in ["box","sphere","cylinder","inertia","limit"]:
        return children2attributes(root)
    # complex nodes are iterated over
    if root.tag in ["joint","link","robot","geometry","inertial","visual","collision"]:
        new_root = etree.Element(root.tag, attrib=root.attrib)
        children = root.getchildren()
        for c in children:
            new_root.append(convert_sdf2urdf(c))
        return new_root
    # otherwise put a warning and return as it is
    warn_comment = etree.Comment(root.tag + " element is not recognized and left unchanged.")
    root.insert(0, warn_comment)
    return root

# take the input
str_lines = vt.get_selected_text()

# parse xml
root = etree.fromstring(str_lines)

new_root = convert_sdf2urdf(root)

# override the selected lines in buffer
new_str = etree.tostring(new_root).decode("utf-8")
vt.replace_selected_text(new_str)

print("done")
