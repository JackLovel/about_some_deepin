import os 

# 作者: JackLovel
# 邮箱: gogkatsu@outlook.com
# 描述: 用于linux安装字体

fonts_list = ["font/consola.ttf", 
              "font/思源宋体.otf"] 

project_dir = os.path.abspath(os.path.dirname(__file__))

font_target_dir = "/usr/share/fonts/"

def copyFont(source_path):
    s, t = source_path, font_target_dir 

    os.system("sudo cp {0} {1}".format(s, t))

def refreshFont():
    os.system("sudo fc-cache -fv") 
      
if __name__ == "__main__":
    for font in fonts_list:
        path = os.path.join(project_dir, font)
        copyFont(path)

    refreshFont()

    print("{0}字体安装成功{0}".format("="*3))
