import os
from tkinter import filedialog
from PIL import Image,ImageDraw

def fileopen(vertical:int,horizonal:int):
    fTyp = [("Image Files",('.jpg','.png'))]
    iDir = os.path.abspath(os.path.dirname(__file__))
    imgpath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    return imagefile.loadImageFile(imgpath,vertical,horizonal)

class griddraw:
    img=None
    imgpass=""
    width=0
    height=0
    bordercolor=(255,0,0) #これは変更可能にしてもいいかも

    def loadImageFile(self,imgpath,vertical:int,horizonal:int):
        self.imgpass=imgpath
        self.img = Image.open(imgpath)
        self.width,self.height = self.img.size
        return self.updateImage(vertical,horizonal)

    def createWhiteImage(self,vertical:int,horizonal:int):
        # オリジナル画像と同じサイズの画像を生成
        imgWhite = Image.new('RGBA',(self.width,self.height))
        imgWhite.putalpha(0)
        drawWhite = ImageDraw.Draw(imgWhite)
        self.drawCutLine(drawWhite,vertical,horizonal)
        imgWhite.save('white_grided.png','PNG')
        print("created white image!")

    def updateImage(self,vertical:int,horizonal:int):
        img = Image.open(self.imgpass)
        drawimg = ImageDraw.Draw(img)
        self.drawCutLine(drawimg,vertical,horizonal)
        #todo: 画像出力処理ぼ どこに出力できるかを選べたほうがいいかもしれない
        img.save('original_grided.png','PNG')
        return 'original_grided.png'

    def drawCutLine(self,draw,vertical:int,horizonal:int):
        self.drawVertical(draw,vertical)
        self.drawHorizonal(draw,horizonal)
        self.drawOutline(draw)

    def drawVertical(self,draw,vertical:int):
        width=self.width
        height=self.height
        for i in range(1,vertical):
            a=int(width/vertical)
            draw.line([(a*i,0),(a*i,height)],fill=self.bordercolor,width=1)

    def drawHorizonal(self,draw,horizonal:int):
        width=self.width
        height=self.height
        for i in range(1,horizonal):
            a=int(height/horizonal)
            draw.line([(0,a*i),(width,a*i)],self.bordercolor,width=1)

    def drawOutline(self,draw):
        # 座標がゼロスタートなので、サイズの数値より1px低い値が縁になる
        width=self.width-1
        height=self.height-1
        draw.line([(0,0),(width,0),(width,height),(0,height),(0,0)],self.bordercolor,width=1)

imagefile = griddraw()