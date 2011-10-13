import ToDo, sys

if __name__ == '__main__':
    f = ToDo.FindSource()
    files = f.findsource(sys.argv[1],sys.argv[2])
    todos = ToDo.FindTODO.get_todos(files)
    html = ToDo.output.TODOs_to_html(todos)
    f = open(output.html, 'w')
    t.write(html)
