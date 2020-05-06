import os

class Run:
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(__file__)) 

    def change_dir(self, path):
        os.chdir(path)

    def compile(self):
        path = self.path 
        self.change_dir(path)
        
        compile_str, bib_str = 'xelatex main.tex', 'bibtex main.aux'

        os.system(compile_str)
        os.system(bib_str)
        os.system(compile_str)
        os.system(compile_str)

    def clear(self):
        path = self.path 
        prefixs = ('aux', 'blg', 'out', 'log', 'toc', 'bbl', 'pdf')
        filenames = os.listdir(path)
        names = [name for name in filenames if name.endswith(prefixs)]
        for n in names:
            self.remove_file(path, n)

    def remove_file(self, path, filename):
        file = os.path.join(path, filename)
        if (os.path.exists(file)):
            os.remove(file)
    
    def list_dir(self):
        path = self.path 
        print("=========项目下的文件或目录========")
        for f in os.listdir(path):
            print(f)
        print("============================")

    def debug(self):
        pass 

if __name__ == "__main__":
    r = Run() 
    p = r.path 

    prompt = """
             输入 1、2或者3 来执行下面的操作，输入 q 退出
             1.编译项目
             2.清除多余文件
             3.查看项目下的文件
            """
    while True: 
        i = input(prompt)
        if i == 'q': 
            break 
        if i == '1': 
            r.compile()
        if i == '2': 
            r.clear()
        if i == '3':
            r.list_dir() 