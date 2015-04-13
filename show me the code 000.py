#"GeeGee"
#第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
class HeadPhoto(object):
    def __init__(self,photoPath='',drawNum=-1,font='Arial.ttf'):
        self.photoPath=photoPath
        self.font=font
        self.drawNum=drawNum
    def openPic(self):
        path=self.photoPath
        try:
            im=Image.open (path)
            self.photo=im
            return True
        except IOError:
            return False
    def draw(self):
        if self.drawNum==-1:
            while True:
                try:
                    self.drawNum=int(raw_input("请输入上标数字："))
                    break
                except ValueError:
                    print"输入类型错误！"
        drawNum=self.drawNum
        text=str(drawNum)if drawNum<100 else "99+"
        while self.openPic():
            
            width,height=self.photo.size
            tagSize=max(width,height)/10
            font=ImageFont.truetype (self.font,tagSize/2)
            draw=ImageDraw.Draw (self.photo)
            draw.ellipse ((width-tagSize,0,width,tagSize),fill=(255,0,0))
            
            draw.text ((width-0.5*tagSize-0.5*font.getsize(text)[0],0.5*tagSize-0.5*font.getsize(text)[1]),text,font=font)
            picName,picMode=self.photoPath.split(".")
            self.photo.save(picName+'(1).'+picMode)
            break
        else :
            self.photoPath=raw_input("在路径下没有找到此文件，请重新重新输入图片路径：")
            
            
            

#主程序
head=HeadPhoto('1.jpg')
head.draw()


