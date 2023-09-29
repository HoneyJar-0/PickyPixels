def format(fp:str) -> None:
    '''
    Takes in a file path to a markup file, and formats it to be more human readable/editable.
    Creates new file with the format changes

    Parameters:
        fp:str -> filepath as a string
    '''
    directory, file = fp.rsplit(sep="\\",maxsplit=1) #gets the directory and file separately
    
    with open(file=(directory + '\\' + "formatted_" + file), mode='w') as f:
        lines = separate_lines(fp)
        
        indent_count = 0
        for line in lines:
            line = "\t"*indent_count + line
            f.writelines(line)
            do_indent = indent_needed(line) #1 = True, 0 = False, -1 = remove indent
            if(do_indent == 1):
                indent_count += 1
            elif(do_indent == -1):
                indent_count -= 1

def indent_needed(line:str) -> int:
    '''
    Checks to see if a line needs to be indented following markup formats.

    Parameters:
        line:str -> a line from a markup file
    
    Returns:
        int: 1 -> line ends in ">", thus we are starting a new block
             -1 -> line ends in "/>", thus we are closing a block
             0 -> line ends with something else, thus we are still in block
    '''
    if(line[-2:-1] == "/>"):
        return -1
    elif(line[-1] == ">"):
        return 1
    else:
        return 0