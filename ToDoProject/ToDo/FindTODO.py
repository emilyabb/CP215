import os
import sys
from todoInfo import todoInfo

def findsource():
    pyfiles = []
    for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            if file[-2:] == "py":
                print file
                pyfiles.append(str(root + os.sep + file))
    print pyfiles
    return pyfiles




def get_todos(files):
    """Create a list of TODO information based on the given files.

@param files: List of paths to Python source files.
@return: List of (person, date, file, line, text) tuples corresponding to TODO comments in the given sources.
"""
    comments = []
    for source_filename in files:
        source_file = open(source_filename, "r")
        line_number = 0
        for line in source_file:
            line_number += 1
            line = line.strip()
            line = line.lstrip("#")
            line = line.strip()
            if line.startswith("TODO"):
                elements = line.split(":")
                if len(elements) >= 4:
                    todo_info = todoInfo(elements[2],
                                         elements[1],
                                         source_filename,
                                         str(line_number),
                                         elements[3].strip())
                         
                    comments.append(todo_info)
    return comments

def sortStuff(in_list):
    in_list.sort()
    print in_list
    return in_list


def outputHTML(sorted_list):
    f = open('todo.html','w')
    startFile(f)
    person = sorted_list[0][0]
    f.write('<li>'+person+'\n<ul>\n')
    for item in sorted_list:
        if not item[0] == person:
            person = item[0]
            f.write('</ul></li>\n<li>'+person+'<ul>\n')
        f.write('<li>'+str(item[1])+' '+item[2]+' '+str(item[3])+' '+item[4]+'</li>\n')
    f.write('</ul></ul></body></html>')
    f.close()

def startFile(f):
    f.write('<html>\n<body>\n<ul>\n')
    

if __name__ == '__main__':
    files = findsource()
    data = get_todos(files)
    sorted_list = sortStuff(data)
    outputHTML(sorted_list)
