import os 

# 作者: JackLovel
# 邮箱: gogkatsu@outlook.com
# 描述: 用于linux安装字体

fonts_list = ["consola.ttf", 
              "思源黑体/SourceHanSansCN-Normal.otf"] 

base_dir = os.path.abspath(os.path.dirname(__file__))
font_target = "/usr/share/fonts/"

def copyFont(source_path):
    source = source_path 
    target = font_target 

    os.system("sudo cp {0} {1}".format(source, target))

def refreshFont():
    os.system("sudo fc-cache -fv") 
      
if __name__ == "__main__":
    for f in fonts_list:
        path = os.path.join(base_dir, f)
        copyFont(path)

    refreshFont()

    print("{0}字体安装成功{0}".format("="*3))
