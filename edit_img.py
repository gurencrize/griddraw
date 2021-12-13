from tkinter import Tk,ttk,filedialog,StringVar,Spinbox,PhotoImage
from PIL import Image,ImageDraw
import os
tate=8
yoko=8
class griddraw:
    img=None
    imgpass=""
    width=0
    height=0
    bordercolor=(255,0,0)
    def readimg(self, imgpass):
        self.imgpass=imgpass
        self.img = Image.open(imgpass)
        self.width,self.height = self.img.size
        self.updatelabel1()

    def create_white(self):
        # オリジナル画像と同じサイズの画像を生成
        img_white = Image.new('RGBA',(self.width,self.height))
        img_white.putalpha(0)
        draw_white = ImageDraw.Draw(img_white)
        self.draw_vertical(int(sptxt1.get()),draw_white)
        self.draw_horizonal(int(sptxt2.get()),draw_white)
        img_white.save('white_grided.png','PNG')
        print("created white image!")

    def updatelabel1(self):
        img = Image.open(self.imgpass)
        drawimg = ImageDraw.Draw(img)
        # 画面に線を引く
        self.draw_vertical(int(sptxt1.get()),drawimg)
        self.draw_horizonal(int(sptxt2.get()),drawimg)
        self.draw_outline(drawimg)
        img.save('original_grided.png','PNG')
        #画像出力処理ぼ どこに出力できるかを選べたほうがいいかもしれない
        photoim=PhotoImage(file='original_grided.png')
        label1.configure(image=photoim)
        label1.image=photoim

    def draw_vertical(self,n:int,draw):
        width=self.width
        height=self.height
        for i in range(1,n):
            a=int(width/n)
            draw.line([(a*i,0),(a*i,height)],fill=self.bordercolor,width=1)

    def draw_horizonal(self,n:int,draw):
        width=self.width
        height=self.height
        for i in range(1,n):
            a=int(height/n)
            draw.line([(0,a*i),(width,a*i)],self.bordercolor,width=1)

    def draw_outline(self,draw):
        # 座標がゼロスタートなので、サイズの数値より1px低い値が縁になる
        width=self.width-1
        height=self.height-1
        draw.line([(0,0),(width,0),(width,height),(0,height),(0,0)],self.bordercolor,width=1)

image=griddraw()
root = Tk()
root.title('補助線描画')

frame1 = ttk.Frame(root)
frame1['height'] = 200
frame1['width'] = 400
frame1.grid()

label1=ttk.Label(frame1)
label1.grid(row=2,column=0,columnspan=5)

label2=ttk.Label(frame1,text="縦")
label2.grid(row=0,column=0)

label3=ttk.Label(frame1,text="横")
label3.grid(row=0,column=1)

def redrawline():
    image.updatelabel1()
sptxt1=StringVar()
sptxt1.set(tate)
spinbox1=Spinbox(frame1,from_=0,to=1000,textvariable=sptxt1,command=redrawline)
spinbox1.grid(row=1,column=0)

sptxt2=StringVar()
sptxt2.set(yoko)
spinbox2=Spinbox(frame1,from_=0,to=1000,textvariable=sptxt2,command=redrawline)
spinbox2.grid(row=1,column=1)

def button1():
    fTyp = [("Image Files",('.jpg','.png'))]
    iDir = os.path.abspath(os.path.dirname(__file__))
    imgpath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    image.readimg(imgpath)
button1=ttk.Button(frame1,text="画像を読み込み",command=button1)
button1.grid(row=1,column=3)

def button2():
    image.create_white()
button2=ttk.Button(frame1,text="白紙を生成",command=button2)
button2.grid(row=1,column=4)


root.mainloop()
