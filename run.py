import os

def main():
    path = project_path() 
    prompt = """
             输入 1 或者 2 来执行下面的操作，输入 q 退出
             1.compile project 
             2.clear project
            """
    while True: 
        i = input(prompt)
        if i == 'q': 
            break 
        if i == '1': 
            compile(path)
        if i == '2': 
            clear(path)
        if i == 'd':
            debug(path) 

project_path = lambda : os.path.abspath(os.path.dirname(__file__)) 

def debug(path):
    pass
        
# 编译项目
def compile(path):
    os.chdir(path)
    compile_str, bib_str = 'xelatex main.tex', 'bibtex main.aux'

    os.system(compile_str)
    os.system(bib_str)
    os.system(compile_str)
    os.system(compile_str)


# 清理项目
def clear(path):
    prefixs = ('aux', 'blg', 'out', 'log', 'toc', 'bbl', 'pdf')
    filenames = os.listdir(path)
    names = [name for name in filenames if name.endswith(prefixs)]
    for n in names:
        remove_file(path, n)


def remove_file(path, filename):
    file = os.path.join(path, filename)
    if (os.path.exists(file)):
        os.remove(file)
    else:
        pass
    
main() 