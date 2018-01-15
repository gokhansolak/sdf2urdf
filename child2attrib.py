import vim
import sys
import xml.etree.ElementTree as etree

sys.path.append(vim.eval("s:path"))
import vim_tools as vt


str_lines = vt.get_selected_text()

# parse xml
root = etree.fromstring(str_lines)

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

# override the selected lines
new_str = etree.tostring(new_root).decode('utf-8')
vt.replace_selected_text(new_str)

print("done")
