import numpy as np
from tkinter import *
from tkinter import ttk,filedialog
from PIL import Image,ImageDraw,ImageTk
import os
tate=8
yoko=8
#画像処理に関するクラスをひとつ作ってしまうのが丸い気がする
def readimg(imgpass:str):
  #global img,width,height#無いとダメらしい
  photoim=PhotoImage(file=imgpass)
  label1.configure(image=photoim)
  label1.image=photoim
  img = Image.open(imgpass)
  width, height = img.size
  draw = ImageDraw.Draw(img)
  print(draw)
  draw_vertical(tate,draw)
  draw_horizonal(yoko,draw)
def create_white(tate:int,yoko:int):
  # オリジナル画像と同じサイズの画像を生成
  img_white = Image.new('RGBA',(width,height))
  img_white.putalpha(0)
  draw_white = ImageDraw.Draw(img_white)
  draw_vertical(tate,draw_white)
  draw_horizonal(yoko,draw_white)
  img_white.save('white_grided.png','PNG')
#縦線を引く
def draw_vertical(n:int,draw):
  n+=1
  #widthとheightを何らかの手段で手に入れる
  for i in range(1,n):
    a=int(width/n)
    draw.line([(a*i,0),(a*i,height)],fill=(255,0,0),width=1)
#横線を引く
def draw_horizonal(n:int,draw):
  n+=1
  
  for i in range(1,n):
    a=int(height/n)
    draw.line([(0,a*i),(width,a*i)],fill=(255,0,0),width=1)
def saveimg():
  img.save('original_grided.png','PNG')#場所を選べるように書き直したい

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
  #global img_tk
  readimg(imgpass)
  img_tk=ImageTk.PhotoImage(img)
  label1.configure(image=img_tk)
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
  readimg(imgpath)
button2=ttk.Button(frame1,text="画像を読み込み",command=button1)
button2.grid(row=1,column=3)

def button2():
  create_white(int(sptxt1.get()),int(sptxt2.get()))
button2=ttk.Button(frame1,text="白紙を生成",command=button2)
button2.grid(row=1,column=4)


root.mainloop()
