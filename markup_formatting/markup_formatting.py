import regex as re
def format(fp:str) -> None:
    '''
    Takes in a file path to a markup file, and formats it to be more human readable/editable.
    Creates new file with the format changes

    Parameters:
        fp:str -> filepath as a string
    '''
    try:
        directory, file = fp.rsplit(sep="\\",maxsplit=1) #gets the directory and file separately
    except:
        file = fp
    
    with open(file=(directory + '\\' + "formatted_" + file), mode='w') as f:
        lines = separate_lines(fp)
        indent_count = 0
        for line in lines:
            line = line.lstrip()
            if(line != ""):
                do_indent = indent_needed(line) #1 = True, 0 = False, -1 = remove indent
                if(do_indent == 1):
                    f.write("\t"*indent_count + line + '\n') #start of block, so write before indenting
                    indent_count += 1
                elif(do_indent == -1 and indent_count > 0):
                    indent_count -= 1
                    f.write("\t"*indent_count + line + '\n') #end of block, so write after decreasing indent
                else:
                    f.write("\t"*indent_count + line + '\n') #no change, just write

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
    opening = r'<[^/].*[^/]>' #block opener
    closing = r'</[a-zA-Z0-9]*>' #closing line that does not create a block
    oneliner = r'<.*/>' #block is opened AND closed in the same line
    comments = r'<!--.*-->' #Comments
    
    #return 1 if we are opening a block
    if(len(re.findall(pattern=comments, string=line)) > 0): #Comment, so no need to change 
        return 0
    elif(len(re.findall(pattern=opening,string=line)) > 0):
        return 1
    #return -1 if we are closing a block
    elif(len(re.findall(pattern=closing,string=line)) > 0):
        return -1
    #return 0 if we open and close in the same line
    elif(len(re.findall(pattern=oneliner,string=line)) > 0): #we open and close block on same line
        return 0
    else: #usually text in things like <p> or <h1>
        return 0
    
def separate_lines(file:str) -> list[str]:
    with open(file=file, mode='r') as f:
        lines = []
        line = ""
        for character in f.read():
            if(character == "<"):
                lines.append(line)
                line = character
            elif(character == ">"):
                line += character
                lines.append(line)
                line = ""
            else:
                line += character
        return lines


format("tests\\urmum.html")