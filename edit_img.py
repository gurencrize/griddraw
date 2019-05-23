import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageDraw,ImageTk
tate=8
yoko=8
imgpass="original.jpg"
def main(tate:int,yoko:int,imgpass:str):
  global img,width,height,draw#無いとダメらしい
  # 元となる画像の読み込み
  img = Image.open(imgpass)
  # オリジナル画像の幅と高さを取得
  width, height = img.size
  draw = ImageDraw.Draw(img)
  draw_vertical(tate)
  draw_horizonal(yoko)
def create_white(tate:int,yoko:int):
  global draw_white
  # オリジナル画像と同じサイズの画像を生成
  img_white = Image.new('RGBA',(width,height))
  img_white.putalpha(0)
  draw_white = ImageDraw.Draw(img_white)
  draw_vertical_w(tate)
  draw_horizonal_w(yoko)
  img_white.save('white_grided.png','PNG')
#縦線を引く
def draw_vertical(n:int):
  n+=1
  for i in range(1,n):
    a=int(width/n)
    draw.line([(a*i,0),(a*i,height)],fill=(255,0,0),width=1)
#横線を引く
def draw_horizonal(n:int):
  n+=1
  for i in range(1,n):
    a=int(height/n)
    draw.line([(0,a*i),(width,a*i)],fill=(255,0,0),width=1)
#縦線を引く(白紙に対して)
def draw_vertical_w(n):
  n+=1
  for i in range(1,n):
    a=int(width/n)
    draw_white.line([(a*i,0),(a*i,height)],fill=(255,0,0),width=1)
#横線を引く(白紙に対して)
def draw_horizonal_w(n):
  n+=1
  for i in range(1,n):
    a=int(height/n)
    draw_white.line([(0,a*i),(width,a*i)],fill=(255,0,0),width=1)
def saveimg():
  img.save('original_grided.png','PNG')#場所を選べるように書き直したい
  #白紙画像も同じように保存できるようにしたい
  
main(tate,yoko,imgpass)
root = Tk()
root.title('補助線描画')

frame1 = ttk.Frame(root)
frame1['height'] = 200
frame1['width'] = 300
frame1.grid()

img_tk=ImageTk.PhotoImage(img)
label1=ttk.Label(frame1,image=img_tk)
label1.grid(row=0,column=0,columnspan=3)

label2=ttk.Label(frame1,text="縦")
label2.grid(row=1,column=0)

label3=ttk.Label(frame1,text="横")
label3.grid(row=1,column=1)

sptxt1=StringVar()
sptxt1.set(tate)
spinbox1=Spinbox(frame1,from_=0,to=1000,textvariable=sptxt1)
spinbox1.grid(row=2,column=0)

sptxt2=StringVar()
sptxt2.set(yoko)
spinbox2=Spinbox(frame1,from_=0,to=1000,textvariable=sptxt2)
spinbox2.grid(row=2,column=1)

def button1():
  global img_tk
  main(int(sptxt1.get()),int(sptxt2.get()),imgpass)
  img_tk=ImageTk.PhotoImage(img)
  label1.configure(image=img_tk)
button1=ttk.Button(frame1,text="線を引き直す",command=button1)
button1.grid(row=2,column=2)
def button2():
  create_white(int(sptxt1.get()),int(sptxt2.get()))
button2=ttk.Button(frame1,text="白紙を生成",command=button2)
button2.grid(row=2,column=3)


root.mainloop()
