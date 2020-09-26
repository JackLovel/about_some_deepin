# 运行：python3 run.py

import os

class Run:
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(__file__)) 
        
        # kde 下的 pdf 查看工具
        # self.pdfTool = "okular"

        # ubuntu pdf tools
        self.pdfTool = "evince"
        
        # 编译之后的 pdf
        self.pdfFile = "main.pdf"

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

        # os.system(compile_str)


    def clear(self):
        # path = self.path 
        # prefixs = ('aux', 'blg', 'out', 'log', 'toc', 'bbl', 'pdf', 'fls', 'fdb_latexmk')
        # filenames = os.listdir(path)
        # names = [name for name in filenames if name.endswith(prefixs)]
        # for n in names:
        #     self.remove_file(path, n)
        os.system("latexmk -C")

    def remove_file(self, path, filename):
        file = os.path.join(path, filename)
        if (os.path.exists(file)):
            os.remove(file)
    
    def list_dir(self):
        path = self.path 
        print("{0}项目下的文件或目录{0}".format("="*5))
        for f in os.listdir(path):
            print(f)
        print("="*20)
    
    def view_pdf(self):
        pdfFilePath = os.path.join(self.path, self.pdfFile)
        fileExist = os.path.exists(pdfFilePath)

        if fileExist: 
            os.system("{0} {1}".format(self.pdfTool, self.pdfFile))
        else: 
            print("="*22)
            print("警告{0} 不存在".format(self.pdfFile))
            print("="*22)

    def debug(self):
        pass 

if __name__ == "__main__":
    run = Run() 

    prompt = """
             输入 1、2、3、4来执行下面的操作，输入 q 或 Q 退出
             1.编译项目
             2.清除多余文件
             3.查看项目下的文件
             4.查看 pdf 
            """
    while True: 
        i = input(prompt)
        if i == 'q' or i == 'Q': 
            break 
        if i == '1': 
            run.compile()
        if i == '2': 
            run.clear()
        if i == '3':
            run.list_dir() 
        if i == '4':
            run.view_pdf()
