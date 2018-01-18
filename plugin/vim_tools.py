import vim 


def get_selected_text():
    buf = vim.current.buffer
    (lnum1, col1) = buf.mark('<')
    (lnum2, col2) = buf.mark('>')
    lines = vim.eval('getline({}, {})'.format(lnum1, lnum2))
    lines[0] = lines[0][col1:]
    lines[-1] = lines[-1][:col2]

    return "\n".join(lines)


def replace_selected_text(new_str):

    buf = vim.current.buffer
    (lnum1, col1) = buf.mark('<')
    (lnum2, col2) = buf.mark('>')

    lines = vim.eval('getline({}, {})'.format(lnum1, lnum2))

    # first line
    new_str = lines[0][:col1] + new_str + lines[-1][col2+1:]

    # split into multiple lines
    new_str_list = new_str.split('\n')

    # delete old lines
    del buf[lnum1-1:lnum2]

    # insert new lines by reverse iteration
    # for i in range(len(new_str_list)-1, -1, -1):
        # buf.append(new_str_list[i], lnum1)
    buf.append(new_str_list, lnum1-1)
        

