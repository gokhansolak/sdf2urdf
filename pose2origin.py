import vim
import sys
import xml.etree.ElementTree as etree

sys.path.append(vim.eval("s:path"))
import vim_tools as vt

str_lines = vt.get_selected_text()

# parse xml
root = etree.fromstring(str_lines)
# root = tree.getroot() 

if root.tag != "pose":
    print( "not a pose element")
    exit()

pose = root.text
pose_list = list(pose.split())

new_root = etree.Element("origin")
new_root.attrib["xyz"] = " ".join(pose_list[:3])
new_root.attrib["rpy"] = " ".join(pose_list[3:])

# override the selected lines
new_str = etree.tostring(new_root).decode('utf-8')
vt.replace_selected_text(new_str)

print("done")
