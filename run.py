import os

def main():
    path = os.path.abspath(os.path.dirname(__file__))
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
    prefixs = ['aux', 'blg', 'out', 'log', 'toc', 'bbl', 'pdf']
    files = os.listdir(path)
    for f in files:
        prefix = f.split(".")[-1] 
        exists = prefix in prefixs
        if (exists):
            remove_file(path, f)
        else:
            pass


def remove_file(path, filename):
    file = os.path.join(path, filename)
    if (os.path.exists(file)):
        os.remove(file)
    else:
        pass
    
main() 